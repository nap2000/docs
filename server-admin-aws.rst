AWS
===

.. contents::
 :local:

Access to S3
------------

As ubuntu type::

  For Ubuntu 24.04 and later: sudo snap install aws-cli --classic
  Older Ubuntu versions: sudo apt install awscli

Get Credentials
---------------

::

  Using the AWS console select IAM
  Select create user
  Specify the access type as programmatic
  Select create group
  Add the security policies that you want.  For example transcribe, translate, rekognition.  S3 access will also be required.
  Download the csv file containing the credentials for your user

Create a credentials file called "credentials" and place it in ~ubuntu/smap/deploy/version1/resources/properties with the following format::

  [default]
  aws_access_key_id = ....
  aws_secret_access_key = ....

Also create a script file called setcredentials.sh that contains 2 lines::

  export AWS_ACCESS_KEY_ID= .....
  export AWS_SECRET_ACCESS_KEY = .....

run patchdb.sh to copy the credentials file to the locations that it is used.

Setting up the AWS Command Line Interface
-----------------------------------------

For example if you want to copy backup files to AWS you can use the bu.sh script in the postgres home directory.
However you will need to configure the AWS CLI as the postgres user and set the credentials::

    aws configure

Using Transcribe, Translate and Rekognition
-------------------------------------------

You will need to update the limits on usage for these in the organisations tab of the users page.

S3 Bucket
+++++++++

Create a bucket in S3 to store backups of uploaded media files.  The files in this bucket will also be used for transcribe::

  Create the bucket in your S3 account.  This bucket should be dedicated to your server.
  Create a file in the settings directory where smap was installed called 'bucket'.  The default location would be /smap/settings/bucket
  Specify the S3 bucket name in this file
  Create another file in the ubuntu home directory called 'region'
  Specify the AWS region in this file.  For example: ap-southeast-2
  run deploy.sh to restart the subscriber so that it now uses the bucket

AWS Properties File
-------------------

A properties file is required. This is really only used for automatic synchronisation of fieldTask but it needs
to be present for other AWS services as well.  Create the file at /smap_bin/resources/properties/aws.properties.
Add the lines::

  userDevices_table={the dynamodb table you set up to contain the list of connected fieldTask instances}
  userDevices_region={the aws region in which you have set up dynamodb}
  fieldTask_platform={the platform ARN as required by AWS SNS}

Automatic Device Synchronisation
--------------------------------

When a task is assigned, or a survey, project or shared resource changes, the server can tell the
affected devices to refresh straight away instead of waiting for the user to pull down the task
list.  This is optional.  Without it FieldTask still refreshes on login, on an organisation change
and whenever the user refreshes by hand, and that is normal behaviour rather than a fault.

The refresh itself carries no data.  The server sends a content free wake up through Firebase Cloud
Messaging, and the device then fetches from the server over its normal authenticated connection.

What you will need
++++++++++++++++++

* A Firebase project, for Cloud Messaging
* An AWS account with DynamoDB, Cognito and SNS
* Your own build of the FieldTask app.  The app in Google Play is built for Smap's own AWS account
  and registers devices in Smap's table, so it cannot be pointed at your DynamoDB table.

Step 1 - Firebase Cloud Messaging
+++++++++++++++++++++++++++++++++

Create a Firebase project and add your FieldTask application to it, then download the
``google-services.json`` file into the app source.

In Firebase, open Project settings, then Service accounts, and generate a new private key.  Keep the
JSON file it produces, it is needed in step 5.

Older instructions describe enabling the Cloud Messaging API (Legacy) and copying a Server Key.  That
API was withdrawn by Google in June 2024 and no longer works.  Use the service account key above.

Step 2 - AWS IAM user
+++++++++++++++++++++

Create an IAM user for the server, and grant it only what the server actually uses.  For device
notifications that is::

  dynamodb:Query on your devices table and its index
  dynamodb:DeleteItem on your devices table
  sns:CreatePlatformEndpoint
  sns:DeleteEndpoint
  sns:Publish

Scope the resource to the table and platform application you create below rather than using "*".

Download the access key CSV and keep it safe.  It is used in step 6.

Step 3 - DynamoDB table
+++++++++++++++++++++++

Create a table to hold the association between a user, a server and a device.

Attributes::

  registrationId  string, the Firebase token, PARTITION KEY
  smapServer      string, the host name the device is configured with
  userIdent       string, the user name
  registeredTime  number, when the registration was last written

Add a global secondary index so the server can find a user's devices::

  Index name      userIdent-smapServer-index
  Partition key   userIdent
  Sort key        smapServer
  Projection      All

The index name matters, the server looks it up by that name.

On demand capacity is appropriate, the table is small and the traffic is bursty.

Step 4 - Cognito identity pool
++++++++++++++++++++++++++++++

FieldTask writes its own registration, so it needs credentials.  Create a Cognito identity pool with
unauthenticated (guest) access enabled, and note the identity pool id for step 7.

Grant the guest role only these actions, scoped to your devices table::

  dynamodb:GetItem
  dynamodb:PutItem
  dynamodb:UpdateItem
  dynamodb:DeleteItem

Do not grant DynamoDB full access, and in particular do not grant ``Scan``, ``Query`` or
``ListTables``.  The identity pool id is embedded in the app, so anyone who has the app has these
permissions.  With ``Scan`` they can read every registration in the table, which means every user
name and every server host name it holds.  Older instructions attached DynamoDB Full Access here;
that is not safe.

Note that the guest role can still write.  The partition key is the device's Firebase token rather
than the Cognito identity, so a condition cannot restrict a caller to its own rows.  Keep the table
dedicated to device registrations and put nothing else in it.

Step 5 - AWS SNS platform application
+++++++++++++++++++++++++++++++++++++

Under Mobile push notifications create a platform application.

* Push notification platform: Firebase Cloud Messaging
* Authentication: token, and upload the service account JSON from step 1

Make a note of the platform application ARN, it is needed in step 6.

Step 6 - Configure the server
+++++++++++++++++++++++++++++

Install the AWS CLI and create the credentials file as described under `Get Credentials`_ above,
using the key from step 2.

Create a properties file at ``/smap_bin/resources/properties/aws.properties`` containing::

  userDevices_table={your dynamodb table name}
  userDevices_region={the region the table is in, for example eu-west-1}
  fieldTask_platform={the sns platform application arn from step 5}

The file must be readable by both tomcat and the subscriber.  Without it the server does not send
device notifications at all.

If your server answers to more than one host name, list every name your devices are configured with,
one per line, in ``/smap/settings/device_hostnames``.  Devices record the host name from their own
server URL, and the server looks each of them up.  Without the file the server works the names out
from recent submissions, which is usually right, so this is only needed for a host that serves
downloads but never receives submissions, or one that differs in case or port from what the devices
have.

Then update and restart::

  cd smap/deploy
  sudo ./patchdb.sh
  sudo ./deploy.sh

Step 7 - Build FieldTask
++++++++++++++++++++++++

Add a ``secrets.properties`` file under ``collect_app`` specifying your own values::

  AMAZON_COGNITO_REGION=
  AMAZON_COGNITO_IDENTITY_POOL_ID=
  AMAZON_DYNAMODB_REGION=

Set your DynamoDB table name in ``AWSConfiguration.DYNAMODB_DEVICES_TABLE``, place your
``google-services.json`` in the app, and build.

Testing
+++++++

Log in on a device, then assign a task to that user.  Device notifications are sent in batches
rather than immediately, so allow about ten minutes.

The device should refresh by itself.  If automatic sending is turned off in the app it shows a
"Changes on server - refresh to update" notification instead, which is expected.

A device that has never been opened since being configured will not have registered yet, so open the
app once before testing.

Monitoring
++++++++++

Each run records how much of the fleet it reached, in the subscriber log and in the ``log`` table.
The difference between the users a change affected and the users actually reached is the proportion
of your fleet that is not registered::

  select log_time, note from log
  where event = 'device refresh'
  order by log_time desc limit 20;

Over time::

  select date_trunc('day', log_time) as day, count(*) as runs, sum(measure) as devices
  from log where event = 'device refresh'
    and log_time > now() - interval '60 days'
  group by day order by day;

To see which host names the server will look devices up under::

  select server_name, count(*) from (
    select server_name from upload_event order by ue_id desc limit 10000
  ) recent where server_name is not null
  group by server_name order by 2 desc;

Every host name your devices use should appear.  Anything missing needs to go in
``/smap/settings/device_hostnames``.

Note that this counts devices that are registered, not notifications that were delivered.  A device
that has been wiped or had the app removed stays in the table until Firebase reports the endpoint as
disabled.

Troubleshooting
+++++++++++++++

The subscriber log is at ``/var/log/subscribers/subscriber_default_forward.log``.

"Skipping Message Processing. No aws properties file"
  The server has no ``aws.properties``, so device notifications are switched off.

"Device host names from ... falling back to the server name of the last upload"
  There is no ``device_hostnames`` file, so the names are being worked out from submissions.  Usually
  fine, but check the derived list against the host names your devices actually use.

"Token not found"
  The user has no device registered under that host name.  Either the device has not been opened
  since it was configured, or it is configured with a host name the server is not looking up.

Devices refresh when the app is open but not otherwise
  Check that the device is not being stopped by the manufacturer's battery optimisation, and that
  notifications are permitted for FieldTask.

