.. _disk-storage:

Disk Storage
============

.. contents::
 :local:

Files are stored in /smap by default although this can be changed at install time.  The subfolders contain the
following directories:

*  **uploadedSurveys**.  This is the raw XML files and attachments submitted to complete a survey form.
*  **attachments**.  After processing attachments submitted with a survey form are stored here.
*  **media**.  Media files that are part of survey forms.  For example, images shown as choices.
*  **templates**.  Uploaded XLS files and PDF templates
*  **temp**.  Temporary files generated for downloads.
*  **settings**.  Settings files used to manage the system.

Reducing disk usage
-------------------

temp
++++

Temporary files older than a day can be deleted as the download will have well and truly completed by then.

uploadedSurveys
+++++++++++++++

After a submitted survey form has been sucessfully processed the contents of the XML file will be in the database
and any attachments will be in the attachments folder.  So deleting old files in uploadedSurveys will free u
significant disk space.  There are some issues to consider though:

*  If there is a problem applying the submitted file to the database then you may need to fix that problem and then re-process.  So if you are confident that you will monitor and resolve all issues within say a week then you could set an automatic script to delete files from uploadedSurveys that are older than that.  Of course if you miss that timeframe you could lose some data.

*  Recovery.  The survey submissions may have been sucessfully processed but you might delete all of that data.  No problem you can undelete.  However you might then go further and erase all of your data.  At this point you have 100 days to "restore" using the data in uploadedSurveys to re-appy the submissions.  If this data has been deleted then you cannot do that and you will need to restore from backups.

Archiving files to long term storage
++++++++++++++++++++++++++++++++++++

Files in uploadedSurveys can be replicated to a long term low cost storage solution such as Azure Blob, or
AWS S3.  Then they can be deleted. Then when you need to recover they can be replicated back.

Files in attachments can also be replicated to long term storage and deleted.  You can then configure the
Apache web server to serve the attachments from the long term storage location.  For example with AWS S3::

  SSLProxyEngine on
  ProxyPass         /attachments https://{region}.amazonaws.com/{bucket}/attachments
  ProxyPassReverse  /attachments https://{region}.amazonaws.com/{bucket}/attachments
