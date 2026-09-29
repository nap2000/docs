.. _analysis-uploading-saved-submissions:

Uploading saved submissions
===========================

.. contents::
 :local:
 
Motivation
----------

Sometimes you may not be able to upload submissions from a phone or tablet by using the refresh button.  
Perhaps because the phone is broken.  One solution may be to remove the sd card from that phone and put
it into another phone that also has fieldTask installed.  It should then be possible to refresh the data and 
send it to the server.

If the phone cannot send, you can copy the raw submissions off it and send them to the server from a computer
using the :doc:`submission API <form-submission-api>`.  There is no page in the browser for uploading them.

Getting the data from the phone
-------------------------------

Connect the phone to a computer with a USB cable and allow file transfer.  The completed instances are in::

  Android/data/org.smap.smapTask.android/files/projects/<folder>/instances

There is only one folder under ``projects``.  Its name is a random identifier created when fieldTask was
installed, so it is different on each phone, and it contains an empty file called ``Default``.  If you use a
variant of fieldTask then ``org.smap.smapTask.android`` will be different.

Each submission is a folder containing the submission XML file and any attachments such as photos.  Copy the
folders you need onto your computer.

Upload the instances
--------------------

Send each submission as a multipart POST to ``/submission``.  The XML file is sent in a part called
``xml_submission_file`` and each attachment in a part named after its file name.  For example using curl::

  curl -u <user name> \
    -F "xml_submission_file=@<instance>.xml;type=text/xml" \
    -F "1718012345678.jpg=@1718012345678.jpg" \
    "https://<your server>/submission?deviceID=recovered"

curl asks for your password.  The user must be allowed to submit results for the survey.  A response of 201
means the submission was accepted.  Sending the same submission twice is safe, the server recognises the
instance ID and does not add the record again.
