.. _sms_case:

Message Conversations
=====================

Overview
--------

Message conversations let you communicate with people via SMS or WhatsApp directly through Smap. This is useful for:

* **Customer support** - Respond to inquiries via text message
* **Case management** - Track ongoing conversations with clients
* **Information gathering** - Collect data through text exchanges

All messages are organized into "cases". Think of a case as containing a conversation thread with one person on one subject, similar to a text message thread on your phone. This keeps all messages from the same person related to a subject grouped together so you can see the full conversation history.

.. note::
   **Before you begin:** The setup steps below require server owner permissions. If you're not the server owner, ask your administrator to complete the setup first. Regular users can skip to the :ref:`replying-to-messages` section.

Prerequisites
-------------

To use message conversations, you'll need:

* An SMS or WhatsApp number from a cloud provider (such as Vonage)
* Server owner access to connect the number to Smap
* A survey configured to receive and organize messages

Setup (For Server Owners Only)
-------------------------------

Complete these steps to enable message conversations on your server:

#.  **Set up your SMS/WhatsApp provider**

    Create an account with a messaging provider and configure it for use with Smap. Follow the detailed instructions:

    * For SMS: :ref:`sms-server-admin`
    * For WhatsApp: :ref:`whatsapp-server-admin`

#.  **Connect the provider to your Smap server**

    In the Admin module, go to **Settings > Server** tab and enter your Vonage Application ID and Vonage Webhook secret.

#.  **Link your phone number to a survey**

    In the Admin module, go to **Users** and select the **Conversations** tab. Here you can connect your SMS or WhatsApp number to the survey that will receive messages.

#.  **Enable cases in your survey**

    In the online editor for your survey, set up a status question. This question determines when a conversation is complete. Specify what value will mark the case as closed (for example, "Resolved" or "Complete").

How Message Conversations Work
-------------------------------

**What are cases?**

Cases are something you are working on such as a complaint, while a case is open all messages from the same phone number are
added to single conversation thread in the open case. Without cases enabled, each message would appear as a separate, unrelated entry in your survey.
With cases, you can see the full conversation history with each person, making it easy to track ongoing interactions.

**What happens to incoming messages?**

* When cases are disabled: Each message creates a new record in your survey
* When cases are enabled: Messages from the same number are added to an ongoing conversation (case)

Receiving Incoming Messages
----------------------------

When someone sends a message to your Smap-connected number:

**First message from a number:**

* A new case is automatically created containing the message
* The case is linked to that phone number

**Subsequent messages from the same number:**

* Messages are added to the existing case for that number
* You can see the full conversation history in one place
* Messages from different phone numbers each get their own separate case

**When there are multiple open cases:**

If a phone number has more than one open case, incoming messages will be added to all open cases for that number. You can configure an automatic reply to help the sender specify which case they're referring to (see :ref:`multiple-open-cases` below).

.. _replying-to-messages:

Replying to Messages
--------------------

To reply to a message conversation:

#.  **Open the case** - Find and click on the case you want to respond to

#.  **Click "Edit"** - This allows you to make changes to the case

#.  **Click "Send notification"** - Opens the notification dialog

#.  **Select "Message Conversation"** as the target

#.  **Type your response** in the message field

#.  **Click "Send"** to send your reply

Your response will be sent via SMS or WhatsApp to the phone number associated with the case. The message will also be added to the case record so you can see the full conversation history.

.. tip::
   If your question type is set to "conversation", the messages will be formatted for easy reading, showing each message in the thread clearly.

.. figure::  _images/sms5.png
   :align:   center
   :width:   600px
   :alt:     A conversation showing the initial received message and a response

   A conversation

Any response from the sending number will also be added to the conversation.

Closing a Case
--------------

When you close a case (by setting the status question to the "closed" value you defined during setup):

* The case will no longer receive new messages from that phone number
* If the same number sends another message, a new case will be created
* This works like starting a fresh conversation

This is useful when an issue is resolved and you want to keep old and new conversations separate.

Advanced Features
=================

.. _multiple-open-cases:

Handling Multiple Open Cases
-----------------------------

**Understanding case references:**

When you reply to a message, Smap automatically adds a reference number to your message, like "#123". This helps the sender identify which conversation they're responding to.

**Automatic reply for multiple cases:**

If a person has more than one open case with you, you can set up an automatic reply that helps them specify which case they're commenting on.

To set this up, create a custom reply message in the Conversations tab. You can use these placeholders:

* **%s1** - Will be replaced with the number of open cases
* **%s2** - Will be replaced with a list of cases and their reference numbers

**Example:**

If you write this automatic reply::

    Hello, thank you for your message. You currently have %s1 open cases (%s2).
    Please include a # and the reference number to identify which case you're commenting on, or add #0 to create a new case.

Someone with 2 open cases might receive::

    Hello, thank you for your message. You currently have 2 open cases (#123: Appointment request, #124: Question about hours).
    Please include a # and the reference number to identify which case you're commenting on, or add #0 to create a new case.

**Directing messages to specific cases:**

If a sender includes a reference number (like "#123") in their message, it will be sent only to that specific case, even if they have multiple open cases.

Creating a New Case from the Same Number
-----------------------------------------

Sometimes a person wants to start a completely new conversation while they still have an open case. They can do this by adding **#0** to their message.

When you include #0 in a message, it will always create a new case, regardless of any existing open cases.

Moving a Message to Its Own Case
---------------------------------

**The situation:**

Sometimes while working on a case, the sender will send a message about a completely different topic. For example, you might be helping someone with an appointment request, and they suddenly ask about store hours. That new topic should be in its own separate case.

**How to move a message:**

#.  **Open the case** in the console (viewing mode in version 25.01 and later, editing mode in earlier versions)

#.  **Click on the message** that should be moved to a new case

    .. figure::  _images/sms6.png
       :align:   center
       :width:   600px
       :alt:     A conversation showing a new message unrelated to the original case

       A conversation with a message that needs moving to its own case

#.  **Add a comment** (optional) - This will be included in the notes of the new case to explain why it was separated

#.  **Confirm** - Click to move the message, or cancel if you change your mind

The message will be removed from the current case and placed in a new case of its own. This keeps conversations organized by topic.
