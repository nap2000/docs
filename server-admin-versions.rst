.. _change-history:

Application Change History
==========================

.. contents::
 :local:

25.09.11
--------

`Download <https://smap-code.s3.us-east-1.amazonaws.com/os_smap_25_09_11_708.tgz>`_

#.  Fix errors in setup scripts used on a new install
#.  Fix issue with addition of parameters to console queries that may occur if the colums are re-ordered
#.  Automatically release a record after it is closed
#.  Remove the record history entry showing a record has been deleted when this is part of an update transaction

25.09.03
--------

`Download <https://smap-code.s3.us-east-1.amazonaws.com/os_smap_25_09_03_7295.tgz>`_

#.  Set the user name of the user who assigned a case in the history page
#.  Include additional security groups in the form access report
#.  Add row filters to the form access report
#.  Unescape HTML codes when downloading data to XLS from the console
#.  Require specific security groups before allowing bulk update
#.  Store multiple column orders in the console for different combinations of survey and oversight form
#.  Add support for last saved in select questions in webforms
#.  Only send a notification once per record
#.  Fix paging in the console at 100
#.  Close webform tab automatically when opened as a task

25.04.39
--------

`Download <https://smap-code.s3.us-east-1.amazonaws.com/os_smap_25_04_39_3887.tgz>`_

#.  Include support for last-saved in WebForms
#.  Reduce size of WebForm code that needs to be downloaded to browser
#.  Default the user name to the user ident if it is not set when adding a user
#.  Include read only surveys as surveys that can be selected for the application of security roles
#.  Fix a bug that prevented the showing of images in PDFs when those images were stored in AWS S3.
#.  Add support for barcodes in WebForms.  These can now be used in browsers on iOS devices.
#.  Fix a bug in reports which caused multiple issues when the data included server calculations.

