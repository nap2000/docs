Launching Apps from a Survey
============================

.. _contents:
  :local:

To Answer a single Question
---------------------------

Other Android applications can be launched from within FieldTask in order to answer a text, integer or decimal question. The information required to
start the other Android app is placed in the appearance column and consists of::

  ex:the_android_intent(parameters)

For example::

  ex:org.xxxx.myapp(param1='a', param2='b')

You should be able to find the **intent** required and also any parameters in the documentation for the external app.  This app will need to be
installed on the android..

To Answer Multiple Questions
----------------------------

Multiple questions can be answered by a more complex external application.  The set up for this is a little different than for answering a 
single question. 

Firstly you have to set the appearance of the group to field-list.  Then in a new column **body::intent** you specify the android
intent and parameters to launch the external application.  This time however you do not need to include "ex:" at the beginning of the 
intent!

.. csv-table:: External Multiple Answers:
  :width: 240
  :widths: 30,30,30,30,120
  :header-rows: 1
  :file: tables/extgroup.csv
  
The external application should return a bundle of contains keys. If these match the type and the name of the questions in the group, then the values 
of the keys will be written to the questions.

Specifying a URI
----------------

The parameter name uri_data can be used by many common external android applications such as those that send emails or SMS messages.  The intent can
be one of the `Android Standard Activity Actions <https://developer.android.com/reference/android/content/Intent#standard-activity-actions>`_. For
example::

  ex:android.intent.action.DIAL(uri_data='tel:1111111111')
  ex:android.intent.action.SENDTO(uri_data='smsto:1111111111', sms_body=${message to send})
  ex:android.intent.action.SENDTO(uri_data='mailto:xxxx@yyyyy.zzz?subject=${email subject}&body=${email body})

Automatically launching
-----------------------

External applications can be automatically launched as soon as the user gets to the question. To do this specify the parameter::

  auto=yes
  
This will launch the application automatically if navigating in the foward direction (ie not swiping back) and if a value
has not already been returned by the external app.

