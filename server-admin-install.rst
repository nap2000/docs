Installing
==========

.. contents::
 :local:

::

  wget {link to tar file}
  tar -zxf {tar file}
  cd smap/install
  sudo ./install.sh

If the installer asks "Which services should be restarted", click ok, accepting the default values.

.. note::

  If your server has a domain name, set it as the **Host name used in links sent by email** in the server settings, see
  :ref:`server-settings`.  Links in emails use it, and when the server is next upgraded the web server is set to accept
  requests for that name only.  Until it is set the web server accepts any host name.  To apply it straight away, edit
  smap.conf and smap-ssl.conf in /etc/apache2/sites-available, set ServerName and ServerAlias to the domain name and add
  the following inside each virtual host, then reload Apache::

    <If "req('Host') != 'smap.example.com'">
       Deny from all
    </If>

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
*  Update the configuration of Tomcat and PostgresSQL to tune performance
*  Add a swap file.
