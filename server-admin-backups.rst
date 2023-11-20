Backup and Restore
==================

.. contents::
 :local:

Backups
-------

#.  Archive the contents of /smap.  In particular /smap/media.  The remaining folders under /smap do not contain critical data.
#.  Backup the two databases: **survey_definitions** and **results** from the postgresql server

Restore
-------

The database will contain all data submitted to the server with the exception of attachments such as images.  These are stored on the file system.
To restore the system you will need to:

#.  Copy the archived files from the /smap folder to /smap on the new machine
#.  Restore the databases from backup

.. note::

  The first step is not necessary if you are archiving attachments and other files to cloud storage and serving attachments directly from there.

Databases
+++++++++

Restore the **survey_definitions** database and the **results** database into the postgresql instance on the new server.
