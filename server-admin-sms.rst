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
    #.  Press the next button
    #.  Link your number to this application
#.  If you select the application that you created then you will see the application id which you will need to enter into the
    server settings page on smap. (You will need the server owner privilege to do this).
#.  Rename the private key created by Vonage as Vonage_private.key and update your deployment scripts to
    place this in /smap_bin/resources/properties/ on the server.  If you place this file in 
    smap/deploy/version1/resources/properties folder in the deployed tar file then it will be automatically 
    copied to the correct location.
#.  You will also need to get a "Signature secret" from the API settings page so that you can use "signed web hooks" to receive SMS
    messages.  The server will check the
    secret included with each inbound request to verify that it has come from Vonage. Enter this secret into the server
    settings page on Smap.  (You will need the server owner privilege to do this).

.. figure::  _images/sms6.png
   :align:   center
   :width:   600px
   :alt:     The Vonage application details page showing the application id

   Vonage Application Details Page showing the application (obscured)

   .. figure::  _images/sms7.png
      :align:   center
      :width:   600px
      :alt:     The Vonage API Settings page showing the web hook signature secret

      Vonage API Settings Page showing showing the web hook signature secret