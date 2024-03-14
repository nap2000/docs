System Overview
===============

.. contents::
 :local:

.. figure::  _images/overview.png
   :align:   center
   :width: 	 500px
   :alt:     Overview of the system showing the major components

   System Components

Firewall
--------

Servers hosted by Smap are located in AWS data centres behind an Amazon Network firewall.  Three ports are opened:

*  443:  All access to the system is via encrypted HTTP
*  80:   Used by certbot for certificate renewal.  The webserver redirects application requests on port 80 to 443
*  22:   Used for administration.  A private key certificate is required to logon. Generally network access is also restricted to those machines used for administration.

Server
------

The system requires a linux server.  In addition scripts are tuned and tested only for Ubuntu LTS servers. Currently supported versions are:

* 22.04
* 20.04
* 18.04

Web Server
----------

Users are authenticated in the Apache web server prior to accessing the application server.

Application Server
------------------

Authorisation is performed in the Tomcat Application Server.

Database
--------

All data, with the exception of media, is stored in a PostgreSQL database with GIS extensions.

File Storage
------------

In small installations media files are stored on the hard disk.   However for larger installations they are stored in AWS S3,  (or equivalent), and
served directly by the web server from S3.

AWS Services
------------

Access to services such as Rekognition is controlled using AWS IAM.  The services used are:

*  Rekognition.  To identify objects in images.
*  Transcribe.  Convert speech to text.
*  Translate.  Translate text into other natural languages.
*  Comprehend. Sentiment analysis.
*  DynamoDB.  To manage notifications to android apps.

Deployment Configurations
-------------------------

Small
+++++

.. figure::  _images/architecture1.png
   :align:   center
   :width: 	 500px
   :alt:     Configuration of a Small installation consisting of a single server

   Small Single Server

The minimum server configuration is:

* 1 CPU
* 2GB memory
* 10GB Disk

Almost certainly you will need more disk for a production system especially if you are capturing images and video.  However
apart from the disk, for most organisations, using Smap for M&E, this small server will be adequate.

Settings
########

In postgresql.conf::

  Max connections:  400

In /var/lib/tomcat[x]/conf/context.xml::

  MaxActive for survey_definitions and results resources:  60

In /etc/default/tomcat[x]::

  JAVA_OPTS="-Djava.awt.headless=true -Xms512m -Xmx768m"


Large
+++++
