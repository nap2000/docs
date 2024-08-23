.. _sms-server-admin:

Set up SMS Numbers
==================

.. contents::
 :local:

SMS messages can create a new case and within that case you can converse with the original sender of the SMS.  Currently this feature
is only supported using the Vonage platform.  Once you have a number Smap can be configured to use it.  Details can be found here: :ref:`sms`.
Documentation on how to use SMS messages as part of case managmement can be found here: :ref:`sms_case`.
Requires Smap Server version 24.09+.

Vonage
------

#.  Create an account on Vonage
#.  Purchase one or more numbers for inbound requests
#.  On API Settings page under SMS settings select “Messages API” this will support WhatsAppp as well as SMS.  
    Click save changes.
#.  On the applications page, create a new application

    #.  Enable messages
    #.  Specify the inbound URL as https://{your server}/sms/vonage/inbound
    #.  Specify the status URL as https://{your server}/sms/vonage/status
    #.  After pressing next link your numbers to this application
#.  The applications page will display your vonage application id which you will need to enter into the 
    server settings page on smap
#.  Rename the private key created by vonage as vonage_private.key and update your deployment scripts to 
    place this in /smap_bin/resources/properties/ on the server.  If you place this file in 
    smap/deploy/version1/resources/properties folder in the deployed tar file then it will be automatically 
    copied to the correct location.

