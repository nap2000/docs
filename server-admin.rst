Server Administration
=====================

.. contents::
 :local:

These notes apply if you have installed your own version of the Smap Server.  If you are using one of our hosted servers then you do not need to worry
about this page.

Server Requirements
-------------------

*  One of the following Ubuntu LTS Server

   *  20.04
   *  18.04
   *  16.04

*  2GB of Memory
*  10GB of disk

Installing
----------

::

  wget {link to tar file}
  tar -zxf {tar file}
  cd smap/install
  sudo ./install.sh


Updating
--------

::

  rm -rf old
  mv smap old
  rm *.tgz
  wget {link to tar file}
  tar -zxf {tar file}
  cd smap/deploy
  sudo ./patchdb.sh
  sudh ./deploy

patchdb will update the database.  deploy.sh will replace the programs.  When you run deploy it will cause an outage of around 20 seconds for your users.

Logs
----

Most problems can be found in the tomcat application logs. However if there is a problem in submitting data the issue may be recorded in the subscriber logs.
When submitting results the request is made to the application which writes the submitted file to the hard drive.  Any issues here will be in the application log.
Then every few seconds a batch job (the subscriber) will run to apply that submitted file to the database. 

Application logs::

  use journalctl  (Ubuntu2004)
  /var/log/tomcat[x]/catalina.out  (Other versions of Ubuntu)

Subscriber logs::

  /var/log/subscribers/subscriber_default_upload.log

AWS
---

Access to S3
++++++++++++

As ubuntu type::

  sudo apt install awscli

Get Credentials
+++++++++++++++

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

Ubuntu2004
^^^^^^^^^^

Also create a script file called setcredentials.sh that contains 2 lines::

  export AWS_ACCESS_KEY_ID= .....
  export AWS_SECRET_ACCESS_KEY = .....

run deploy.sh to copy the credentials file to the locations that it is used.

Using Transcribe, Translate and Rekognition
+++++++++++++++++++++++++++++++++++++++++++

You will need to update the limits on usage for these in the organisations tab of the users page.

S3 Bucket
#########

Create a bucket to store backups of uploaded media files.  The files in this bucket will also be used for transcribe::

  Create the bucket in your S3 account
  Create a file in the ubuntu home directory of your server called 'bucket'
  Specify the bucket name in this file
  Create another file in the ubuntu home directory called 'region'
  Specify the AWS region in this file.  FOr example: ap-southeast-2
  run deploy.sh to restart the subscriber so that it now uses the bucket

AWS Properties File
+++++++++++++++++++

An properties file is required. This is really only used for automatic synchronisation of fieldTask but it needs to be present for other AWS services as well::  

  Create the file at /smap_bin/resources/properties/aws.properties
  Add the line:  userDevices_region=us-east-1


