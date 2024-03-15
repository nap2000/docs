
Hosted Server
=============

.. contents::
 :local:

Smap provides a free hosted server at https://sg.smap.com.au for use by individuals, not for profit organisations and any organisation
which is trying the system out.

Overview
--------

.. figure::  _images/hosted.png
   :align:   center
   :width: 	 500px
   :alt:     Setup of the Hosted Server

   Hosted Server



Security
--------

The following security controls are provided with the hosted server.  If you need higher levels of security it is recmommended that you
install your own version of the server.

.. csv-table:: Encryption
  :header: control, done, comment

  Encryption of network data,  Yes, All connections are encrypted. Attempts to connect as HTTP are redirected to HTTPS.
  Encryption of backups, Yes,  Backups are encrypted using PGP.
  Encryption of the database, No,  The database is not encrypted.

.. csv-table:: Integrity Processes
  :header: control, done, comment

  Intrusion Detection,  No,
  Virus Checking, No

.. csv-table:: Service Levels
  :header: control, done, comment

  Availability,  , We will attempt to make the server available continously (24X7).  There are no planned outages, although these may happen.  In addition server faults may occur randomly and we will attempt to restart the server as soon as possible afterwards.
  Backup Recovery Point, 24 hours,  If there is a catastrophic failure of the server then it will be restored from offsite backups.  These backups are moved off site once every 24 hours.  So it is possible that the site will be restored to its state up to 24 hours previously.

.. csv-table:: Privacy
  :header: control, done, comment

  Privacy Policy,  , https://www.smap.com.au/privacy.shtml