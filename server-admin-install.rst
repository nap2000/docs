Installing
==========

.. contents::
 :local:

::

  wget {link to tar file}
  tar -zxf {tar file}
  cd smap/install
  sudo ./install.sh

Edit the Apache config files::

  This needs to be done to enable some security checks.   Edit smap.conf and smap-ssl.conf in /etc/apache2/sites-available.  Replace all
  occurrences of {hostname} with the domain name that you will be using.  Or delete these rows.

If the installer asks "Which services should be restarted", click ok, accepting the default values.

.. note::

  Important!  Due to some security updates you will need to edit the file /etc/apache2/sites-available/smap-ssl.conf.   Replace all
  occurrences of {hostname} with the domain name of your server.  This assumes you are using a domain name.

After the installation script finishes you should be able to logon with your browser using::

  ident: admin
  password: admin

.. warning::

  You should change the password of the admin user before loading any data.  Alternatively create a new user with all permissions then delete
  the admin user.

refer to (:ref:`network-encryption`)

Using a different location for files
------------------------------------

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

Further Administrative Actions
------------------------------

After installation the following further steps may be required:

*  Implement log rotation for tomcat and subscriber logs.  (:ref:`log-rotate`)
*  Add an SSL certificate
*  Add AWS CLI command line
*  Update the configuration of Tomcat and PostgreSQL to tune performance