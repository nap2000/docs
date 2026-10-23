Installing
==========

.. contents::
 :local:

::

  wget {link to tar file}
  tar -zxf {tar file}
  cd smap/install
  sudo ./install.sh

The installer asks for the domain name of the server, or its IP address if it has no domain name.  The domain does not need to
exist yet.  Apache will then refuse requests for any other host name, which stops a forged host name being used in links in
emails.  To install without being asked set SMAP_DOMAIN first, for example ``sudo SMAP_DOMAIN=smap.example.com ./install.sh``.
Requires Smap Server version 26.11+.

To change it later, for example when a server installed with its IP address is given a domain name, from the install directory::

  sudo ./setDomain.sh {domain name or IP address}

Before version 26.11 you needed to edit smap.conf and smap-ssl.conf in /etc/apache2/sites-available and replace all
occurrences of {hostname} with the domain name, or delete those rows.  Until this was done every request was refused.

If the installer asks "Which services should be restarted", click ok, accepting the default values.

After the installation script finishes you should be able to logon with your browser using::

  ident: admin
  password: admin

.. warning::

  You should change the password of the admin user before loading any data.  Alternatively create a new user with all permissions then delete
  the admin user.

From Smap Server version 26.11+ the console takes you to the change password page when you first logon as admin, and the new
password must be different and meet the minimum password strength, which is 25 on a new server.  See :ref:`password-strength`.
Until it is changed FieldTask and API version 1 will not accept the admin logon.  Upgrading a server to 26.11 does the
same if the admin user still has the password admin.  Other users are not affected.

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
*  Update the configuration of Tomcat and PostgresSQL to tune performance
*  Add a swap file.
