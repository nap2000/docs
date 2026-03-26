Logs
====

.. contents::
 :local:

Most problems can be found in the Tomcat application logs. However, if there is a problem submitting data, the issue may be recorded in the subscriber logs.
When submitting results, the request is made to the application, which writes the submitted file to disk. Any issues here will appear in the application log.
Then, periodically (typically every few seconds), a batch job (the subscriber) runs to apply that submitted file to the database.

Application logs::

  Use journalctl (Ubuntu 20.04)
  /var/log/tomcat[x]/catalina.out (other Ubuntu versions)

Subscriber logs::

  /var/log/subscribers/subscriber_default_upload.log
  /var/log/subscribers/subscriber_default_forward.log

Setting a Log Level
-------------------

Application logs::

    Edit the Tomcat conf/logging.properties file and set

    .level = SEVERE or WARNING or INFO or CONFIG or FINE or ALL or OFF

Subscriber logs::

    This option is available with Smap Version 26.03.08+

    Edit the file smap-logging.properties in the directory {base_path}/settings. {base_path} is usually "/smap"
    Set smap.log.level=INFO or SEVERE or WARNING or FINE

.. _log-rotate:

Log Rotation
------------

Tomcat. /etc/logrotate.d/tomcat[?]. A reasonable configuration is::

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

Subscribers. /etc/logrotate.d/subscribers. A reasonable configuration is::

    /var/log/subscribers/*.log {
        copytruncate
        daily
        rotate 10
        compress
        missingok
        size 5M
    }

Note: the subscribers log directory should be owned by tomcat and have permissions 0750.
