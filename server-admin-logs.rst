Logs
====

.. contents::
 :local:

Most problems can be found in the tomcat application logs. However if there is a problem in submitting data the issue may be recorded in the subscriber logs.
When submitting results the request is made to the application which writes the submitted file to the hard drive.  Any issues here will be in the application log.
Then every few seconds a batch job (the subscriber) will run to apply that submitted file to the database.

Application logs::

  use journalctl  (Ubuntu2004)
  /var/log/tomcat[x]/catalina.out  (Other versions of Ubuntu)

Subscriber logs::

  /var/log/subscribers/subscriber_default_upload.log

