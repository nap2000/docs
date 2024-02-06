Background Processes
====================

.. contents::
 :local:

The installation script configures two background processes to be run automaticall.  They run the same process but with a
different parameter::

  /smap_bin/subscribers.sh default /smap upload
  /smap_bin/subscribers.sh default /smap forward

The subscribers.sh shell job runs setCredentials.sh and then runs the subscriber jar using the same parameters
it was passed. These parameters:

#.  default.  This is ignored.
#.  /smap.    The absolute base path of the smap folder.  You can change this when installing smap.
#.  upload or forward.  The subscriber type.  Specifies the work to be done by the process.

Manager - main
--------------

If the subscriber type is "upload" starts:

#.  SubscriberBatch(Upload) - Synchronous
#.  AutoUpdateProcessor - Asynchronous (Moved to forward subscriber in 24.01)

If the subscriber type is "forward" starts:

#.  SubscriberBatch(Forward) - Synchronous
#.  MessageProcessor - Asynchronous
#.  StorageProcessor - Asynchronous
#.  ReportProcessor - Asynchronous

Subscriber Batch runs in the main thread and is started as two separate processors with a subscriber type of upload or forward.
Different actions are taken depending on the subscriber type.  These were
the original processes that were called for background processing.  However newer processors have been added
to run as asynchronous threads and these are started by one of the subscriber types.

SubscriberBatch(Upload)
+++++++++++++++++++++++

#.  Get pending upload events from the upload_event table (No Limit!)
#.  For each upload event
  *  Uploads the XML file and applies it to the database (SubRelationalDB::upload)
    #.  Writes the XML to the database
    #.  Processes Foreign Keys  [Move to async process]
    #.  Apply Submission Events (Notifications, Tasks etc connected to a submission) [Move to separate queue]
    #.  Updates Assignment status [minimal load - leave]
  *  Update the uploaded XML files with changes made to media paths
  *  If an S3 bucket is enabled sends the attachments to S3 [The bulk of this is already in a separate queue]

AutoUpdateProcessor
+++++++++++++++++++

#. Checks for pending asynchronous jobs that have completed. This is currently just for audio transcriptions.  Jobs that
have taken longer than 24 hours are marked as timed out. The output of completed jobs is written to the results
database.
#.  Gets a list of questions that have requested auto updates from AWS. (AutoUpdateManager::identifyAutoUpdates)
#.  For each auto update question apply auto updates (AutoUpdateManager::applyAutoUpdates)
  *  For each record get the instance id and question value then apply one of:
  *  AUTO_UPDATE_IMAGE
  *  AUTO_UPDATE_AUDIO
  *  AUTO_UPDATE_TEXT
  *  AUTO_UPDATE_SENTIMENT
#.  Then writes result to database, For audio this is just to write a "Pending" status value into the output question

SubscriberBatch(Forward)
++++++++++++++++++++++++

The name "Forward Subscriber" derives from this service originally being used to forward submissions to other
servers, that functionality is no longer supported but the name has stuck.

#.  Apply case management reminders
#.  Apply periodic notifications
#.  Erase old survey templates
#.  Delete old linked CSV files (new versions of CSV files are generated when they are updated and the old version is retained in case it is being downloaded at that time)
#.  Applies reminder notifications [Move to async process]
#.  Send Campaign Mailouts [Move to async process]
#.  Expire temporary users [Move to async process]
#.  Calculate fingerprint templates

Message Processor
+++++++++++++++++

#.  Apply outbound email messages
#.  Apply pending email messages.  These are messages that have been moved to pending until the user opts in to receive them

Storage Processor
+++++++++++++++++

Report Processor
++++++++++++++++

Queues
------

#.  Submissions (shown in queue service)
#.  S3 upload (shown in queue service)
#.  Messages - topics
  *  TOPIC_SUBMISSION, TOPIC_CM_ALERT
  *  TOPIC_REMINDER
  *  EMAIL_TASK - an email generated for a task
  *  TOPIC_MAILOUT - and email for a mailout
  *  TOPIC_PERIODIC - a periodic event
#.  Pending messages
#.  Sending Mailouts
#.  Foreign Keys