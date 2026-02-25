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
  /var/log/subscribers/subscriber_default_forward.log

.. _log-rotate:

Log Rotation
------------

Tomcat.  /etc/logrotate.d/tomcat[?].  Should be set up a reasonable configuration would be::

    /var/log/tomcat9/catalina.out {
      copytruncate
      daily
      rotate 10
      compress
      delaycompress
      missingok
      notifempty
      create 640 syslog adm
    }

Subscribers.  /etc/logrotate.d/subscribers.  Should be set up a reasonable configuration would be::

    /var/log/subscribers/*.log {
        copytruncate
        daily
        rotate 10
        compress
        missingok
        size 5M
    }

Note the subscribers log directory should be owned by tomcat and have permissions 0750
