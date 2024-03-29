System Overview
===============

.. contents::
 :local:

.. figure::  _images/overview.png
   :align:   center
   :width: 	 500px
   :alt:     Overview of the system showing the major components

   System Components


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

