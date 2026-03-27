.. _application-change-history:

Application Change History
==========================

.. contents::
 :local:

26.03.08
--------

Release date: 2026-03-27

`Download 26.03.08 <https://smap-code.s3.us-east-1.amazonaws.com/os_smap_26_03_08_6949.tgz>`_

#.  Add a tab for servers on the monitoring page.  This shows queue activity include whether queues are running or stopped
#.  Removed the logging of "heartbeats" for queues in the subscriber logs.  The number of logs written by default reduced. `The log level for the subscriber can now be specified. <https://www.smap.com.au/docs/server-admin-logs.html#setting-a-log-level>`_
#.  Improve appearance of analysis page
#.  Add Pie Charts as a charting option on the analysis page

25.10.44
--------

Release date: 2026-03-08

`Download 25.10.44 <https://smap-code.s3.us-east-1.amazonaws.com/os_smap_25_10_44_2056.tgz>`_

#.  Make processing of key queue more robust
#.  Add _assigned as a column that can be filled when importing data
#.  Add support for accepting and rejecting self assigned tasks on the webforms page
#.  Fix issue in counting tasks so that self assigned ones are counted
#.  Improve consistency of URLs in email campaign mailouts
#.  Fix an issue preventing the resending of email campaign mailouts
#.  Update the version of the Tomcat application server
#.  Add counts for sub forms in survey lookup

Note this release was patched on 2026-03-13 from version 43 to 44 to fix a bug.

25.10.37
--------

Release date: 2026-02-12

`Download 25.10.37 <https://smap-code.s3.us-east-1.amazonaws.com/os_smap_25_10_37_2155.tgz>`_

#.  Add support for fully multi-threaded subscribers so you should be able to start multiple subscribers on multiple servers to process uploads
#.  Performance improvements to the subscriber, if you have tens of millions of uploads the query duration to find new uploads to apply will drop from 3 seconds or so to a few milliseconds
#.  Additional information included in the server information API query "/api/v1/lookup/survey_ident/{survey_ident}". This includes the number of records submitted to the survey and the date of the first and last submission.
#.  Conserve memory in subscriber.  Previously this was causing out-of-memory errors when large numbers of large PDFs were being generated
#.  Fix a bug in writing CSV labels for resource files when there were spaces in some of the survey languages
#.  Add the ability to set a limit on the number of records returned in an API call
#.  Reorganise some of the settings tabs to put settings in categories for easier navigation and readability
#.  Add support for WebP images


25.10.03
--------

Release date: 2025-10-14

`Download 25.10.03 <https://smap-code.s3.us-east-1.amazonaws.com/os_smap_25_10_03_5919.tgz>`_

#.  Use text-type questions in graphs on the analysis page
#.  Add a bundle access report
#.  Add support in the online editor for the no-collapse appearance

25.09.11
--------

Release date: 2025-09-22

`Download 25.09.11 <https://smap-code.s3.us-east-1.amazonaws.com/os_smap_25_09_11_708.tgz>`_

#.  Fix errors in setup scripts used on a new install
#.  Fix issue with addition of parameters to console queries that may occur if the columns are re-ordered
#.  Automatically release a record after it is closed
#.  Remove the record history entry showing a record has been deleted when this is part of an update transaction

25.09.03
--------

Release date: 2025-09-12

`Download 25.09.03 <https://smap-code.s3.us-east-1.amazonaws.com/os_smap_25_09_03_7295.tgz>`_

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

Release date:  2025-08-21

`Download 25.04.39 <https://smap-code.s3.us-east-1.amazonaws.com/os_smap_25_04_39_3887.tgz>`_

#.  Include support for last-saved in WebForms
#.  Reduce size of WebForm code that needs to be downloaded to browser
#.  Default the user name to the user ident if it is not set when adding a user
#.  Include read-only surveys as surveys that can be selected for the application of security roles
#.  Fix a bug that prevented the showing of images in PDFs when those images were stored in AWS S3.
#.  Add support for barcodes in WebForms.  These can now be used in browsers on iOS devices.
#.  Fix a bug in reports which caused multiple issues when the data included server calculations.

25.04.33
--------

Release date:  2025-08-01

`Download 25.04.33 <https://smap-code.s3.amazonaws.com/os_smap_25_04_33_6357.tgz>`_.

*  Set a limit on uploaded media of 30MB for each file
*  Fix a problem generating PDFs when embedded images do not contain metadata allowing rotation
*  Remove renaming of subscriber logs when deploy script is run.  It is assumed that logrotate will be used instead.
*  Update Spanish translations
