.. _sms_case:

SMS Conversations
=================

If you have an SMS number from an SMS cloud provider and attach it to a survey then you can receive and send SMS messages. See details
 here on how to set this up :ref:`sms`. Without cases each inbound message will create a new record in your survey.  However by setting up a
 case you can create a conversation within the case.

Inbound SMS
-----------

If there is no currently open case for the sending number then a new case will be created containing the message. Subsequent messages
from the same sending number will be added to the case.  SMS messages from different numbers will go into their own separate case.

Replying
---------

#.  Lock the case for editing then select "Edit".
#.  Select send notification
#.  Select the target "Message Conversation"
#.  Type your response and click send

Your response will be sent to the number that created the case and will be added to the question that holds the message.
If the type of the question is set to "conversation" then the messages
will be formatted for easy reading

.. figure::  _images/sms5.png
   :align:   center
   :width:   600px
   :alt:     A conversation showing the initial received message and a response

   A conversation

   Any response from the sending number will also be added to the conversation.

   Closing the case
   ----------------

   Once the case is closed it will not receive any additional messages.  Instead if a new message is received from the same number it will
   create a new case as if it was the first time that person had sent a message.

