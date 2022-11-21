Server Administration
=====================

.. contents::
 :local:

These notes apply if you have installed your own version of the Smap Server.  If you are using one of our hosted servers then you do not need to worry
about this page.

Server Requirements
-------------------

*  One of the following Ubuntu LTS Server

   *  22.04
   *  20.04
   *  18.04

*  2GB of Memory
*  10GB of disk

Server configuration for Performance
++++++++++++++++++++++++++++++++++++

Small Server (2 GB RAM)
#######################

Max connections in postgresql.conf: 400

/var/lib/tomcat[x]/conf/context.xml

*  Max Active Survey Definitions: 60
*  Max Active Results: 60

/etc/default/tomcat[x]  

*  JAVA_OPTS="-Djava.awt.headless=true -Xms512m -Xmx768m"

Medium Server (4 GB RAM)
########################

Max connections in postgresql.conf: 600

/var/lib/tomcat[x]/conf/context.xml

*  Max Active Survey Definitions: 100
*  Max Active Results: 100

/etc/default/tomcat[x]  

*  JAVA_OPTS="-Djava.awt.headless=true -Xms2048m -Xmx3072m"

Large Server (8 GB RAM)
#######################

Max connections in postgresql.conf: 800

/var/lib/tomcat[x]/conf/context.xml

*  Max Active Survey Definitions: 120
*  Max Active Results: 120

/etc/default/tomcat[x]  

*  JAVA_OPTS="-Djava.awt.headless=true -Xms4096m -Xmx4096m"


Installing
----------

If your version of ubuntu does not have the multiverse and universe repositories then you will need to add them::

  sudo add-apt-repository universe
  sudo add-apt-repository multiverse

::

  wget {link to tar file}
  tar -zxf {tar file}
  cd smap/install
  sudo ./install.sh

After the installation script finishes you should be able to logon with your browser using::

  ident: admin
  password: admin

If you have not set up an https certificate yet then the connection will be via http and you will be asked to enter your password 3 times.  
Using https you will not have that problem.

Using a different location
++++++++++++++++++++++++++

By default all files are installed under /smap in the root directory.  

To use a different location, or a
different drive, you can either add a symbolic link from /smap to that location or you do not want to put
anything in the / directory then you can specify a different location at install time.

Logical link::

  Before running install, or you can do it after installing and copy the contents of /smap to the new location
  ln -s /smap /new location

Install to a custom location::

  Before running install edit the install.sh script and set "filelocn" to the location that you want to use
  Then run install.sh

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
  sudh ./deploy.sh

patchdb will update the database.  deploy.sh will replace the programs.  When you run deploy it will cause an outage of around 20 seconds for your users.

Configuring for remote database
-------------------------------

#.  Add export DBHOST={remote database address} to /etc/environment
#.  Find the "context.xml" file for tomcat.  It should be at /etc/tomcat[version]/context.xml. Then set the URL for the 2 datasources to match the URL of
    your remote database
#.  Rerun deploy.sh

Sample /etc/environment::
  
  export DBHOST=remote_db_server.myorg.com

Sample url for resource in context.xml::

  url="jdbc:postgresql://remote_db_server.myorg.com:5432/survey_definitions"

Configuring a second application server
---------------------------------------

If you are using a remote database you can add additional application servers for redundancy and performance.  However currently only one of these can
run the subscriber batch job that applies nore submissions to the database.  Otherwise a lot of false update errors will be reported as multiple subscribers
clash.

Hence in all but one of your application servers specify in /etc/environment::

  SUBSCRIBER=no

This should be specified before you install Smap into the new application server.

Backups
-------

#.  Archive the contents of /smap.  In particular /smap/media.  The remaining folders under /smap do not contain critical data.
#.  Backup the two databases: **survey_definitions** and **results** from the postgresql server

Restore
-------

The database will contain all data submitted to the server with the exception of attachments such as images.  These are stored on the file system.
To restore the system you will need to:

#.  Copy the archived files from the /smap folder to /smap on the new machine
#.  Restore the databases from backup

.. note::

  The first step is not necessary if you are archiving attachments and other files to cloud storage and serving attachments directly from there.

Databases
+++++++++

Restore the **survey_definitions** database and the **results** database into the postgresql instance on the new server.

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

Network Encryption
------------------

Generally I use certbot.

install Certbot as per https://certbot.eff.org 
If there are any issues then install certbot-auto https://certbot.eff.org/docs/install.html 

Then::

  sudo certbot --apache certonly

Apache > 2.4.7  

  SSLCertificateFile    /etc/letsencrypt/live/{domain name}/fullchain.pem
  SSLCertificateKeyFile /etc/letsencrypt/live/{domain name}/privkey.pem

Create directory /var/log/certbot

Setup Renewal
+++++++++++++

As root Crontab::

  44 19 * * * certbot renew >> /var/log/certbot/renew.log 2 >&1

Check for logs in /var/log/letsencrypt/letsencrypt.log

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

A properties file is required. This is really only used for automatic synchronisation of fieldTask but it needs 
to be present for other AWS services as well.  Create the file at /smap_bin/resources/properties/aws.properties. 
Add the lines::  

  userDevices_table={the dynamodb table you set up to contain the list of connected fieldTask instances}
  userDevices_region={the aws region in which you have set up dynamo =db}
  fieldTask_platform={the platform ARN as required by AWS SNS}

Disk Storage
------------

Files are stored in /smap by default although this can be changed at install time.  The subfolders contain the 
following directories:

*  **uploadedSurveys**.  This is the raw XML files and attachments submitted to complete a survey form.
*  **attachments**.  After processing attachments submitted with a survey form are stored here.
*  **media**.  Media files that are part of survey forms.  For example, images shown as choices.
*  **templates**.  Uploaded XLS files and PDF templates
*  **temp**.  Temporary files generated for downloads.  
*  **settings**.  Settings files used to manage the system.

Reducing disk usage
+++++++++++++++++++

temp
####

Temporary files older than a day can be deleted as the download will have well and truly completed by then.

uploadedSurveys
###############

After a submitted survey form has been sucessfully processed the contents of the XML file will be in the database
and any attachments will be in the attachments folder.  So deleting old files in uploadedSurveys will free u
significant disk space.  There are some issues to consider though:

*  If there is a problem applying the submitted file to the database then you may need to fix that problem and then re-process.  So if you are confident that you will monitor and resolve all issues within say a week then you could set an automatic script to delete files from uploadedSurveys that are older than that.  Of course if you miss that timeframe you could lose some data.

*  Recovery.  The survey submissions may have been sucessfully processed but you might delete all of that data.  No problem you can undelete.  However you might then go further and erase all of your data.  At this point you have 100 days to "restore" using the data in uploadedSurveys to re-appy the submissions.  If this data has been deleted then you cannot do that and you will need to restore from backups.

Archiving files to long term storage
####################################

Files in uploadedSurveys can be replicated to a long term low cost storage solution such as Azure Blob, or
AWS S3.  Then they can be deleted. Then when you need to recover they can be replicated back.

Files in attachments can also be replicated to long term storage and deleted.  You can then configure the
Apache web server to serve the attachments from the long term storage location.  For example with AWS S3::

  SSLProxyEngine on
  ProxyPass         /attachments https://{region}.amazonaws.com/{bucket}/attachments
  ProxyPassReverse  /attachments https://{region}.amazonaws.com/{bucket}/attachments


Development
-----------

FieldTask
+++++++++

*  Source code:  https://github.com/smap-consulting/fieldTask4     
*  Platform:  Android
*  Software:  Java, Kotlin

Smap Server
+++++++++++

*  Source code: https://github.com/smap-consulting/smapserver2
*  Platform:  Ubuntu Linux
*  Database: Postgresql
*  Application Server: Tomcat
*  Software:  Java

Web Client
++++++++++

*  Software:  HTML, Javascript, JQuery, Bootstrap
