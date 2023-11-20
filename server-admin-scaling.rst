Scaling the Server
===================

.. contents::
 :local:

Configuring for remote database
-------------------------------

#.  Add "export DBHOST={remote database address}" to /etc/environment
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