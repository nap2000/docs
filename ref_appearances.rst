.. _appearances-reference:

.. contents::
 :local:  

Survey Appearances
==================

.. csv-table:: Appearances:
  :width: 90
  :widths: 10,40,40
  :header-rows: 1
  :file: tables/appearances.csv
  
Calling another Android app
---------------------------

Use an appearance starting with **ex:android.intent.action**

Sending an SMS::

  ex:android.intent.action.SENDTO(uri_data='smsto:5555555', sms_body=${message})
  
Sending an Email::

  ex:android.intent.action.SENDTO(uri_data='mailto:example@example.com?subject=${subject}&body=${message})
  
Calling a telephone number::

  ex:android.intent.action.DIAL(uri_data='tel:5555555')
  
More information available in the ODK documentation https://docs.opendatakit.org/launch-apps-from-collect/#specifying-a-uri-as-intent-data
