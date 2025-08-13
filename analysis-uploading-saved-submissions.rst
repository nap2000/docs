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

Sometimes you may be able to get the raw submissions from the phone and copy them onto a laptop.  You 
may then want to submit the data from the laptop.  Smap used to provide a java application called smapUploader
for this purpose however this has now been replaced with a much simpler approach where the data is loaded
directly to the server using an internet browser.

Getting the data from the phone
-------------------------------

The approach can vary depending on the type of Android device that you have.  Once you have obtained access
to the sdcard on your phone you will find the completed instances here::

  /sdcard/Android/data/org.smap.smapTask.XXXX/files/instances

Where XXXX is the identifier for your variant of the fieldTask App.

Copy the instances folder onto your computer. Then compress it into a zip file.

Upload the instances
--------------------

*  Logon to the server using your browser.


