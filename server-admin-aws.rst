AWS
===

.. contents::
 :local:

Access to S3
------------

As ubuntu type::

  For Ubuntu 24.04: sudo snap install aws-cli --classic
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

A PDF containing a detailed description of the process to set up push notifications to devices can
be downloaded from here: https://smap-documents.s3.amazonaws.com/SMAP+AWS+Push+Notification+Set-Up.pdf.
