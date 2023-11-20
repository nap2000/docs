Installing
==========

.. contents::
 :local:

If your version of ubuntu does not have the multiverse and universe repositories then you will need to add them::

  sudo add-apt-repository universe
  sudo add-apt-repository multiverse

::

  wget {link to tar file}
  tar -zxf {tar file}
  cd smap/install
  sudo ./install.sh

If the installer asks "Which services should be restarted", click ok, accepting the default values.

After the installation script finishes you should be able to logon with your browser using::

  ident: admin
  password: admin

If you have not set up an https certificate yet then the connection will be via http and you will be asked to enter your password 4 times.
Using https you will not have that problem.  If you can access the server now you should prioritise the addition of an SSL certificate as
using only http some features will not work.

refer to (:ref:`network-encryption`)

Using a different location
--------------------------

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
