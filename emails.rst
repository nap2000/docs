.. _email-concepts:

Emails: Unsubscribe, Subscribe, Opt in
======================================

.. contents::
 :local:
 
Emails
------

Subscriptions work at the organisation level.  Hence if you have unsubscribed from one organisation you can still get emails from another.  

.. warning::

  Automatic sending of emails for email campaigns and tasks is turned off by default in all organisations and can only be turned on
  by the organisation administrator.

Unsubscribe
------------

Every email sent has an unsubscribe link. If the email recipient does not want to receive emails they can click on this which will take
them to a page with an unsubscribe button.  If they click on that button they will not receive any more emails.

It is not possible to wake up one morning and decide to unsubscribe.  An unsubscribe link is needed in an email.

Subscribe
---------

If someone wants to receive emails again they can go to the home page of the server and select subscribe.  They will then be asked to enter
their email address and validate it.  If they are unsubscribed from 1 or more organisations then those organisations will be listed and the
person can select the ones they want to subscribe to again.

They will then receive an email asking them to confirm the subscription.

Opt in
------

Before mailouts, tasks or notifications are sent to an email address the recipient needs to "opt in".  More accurately we just want them to 
confirm their email address.  Until the user opts in other emails are held in a pending state.

For email mailouts the opt in email is the first email that the person is sent.  If they complete the requested survey then the user is marked as 
opted in.

For notifications a special opt in email is sent allowing the user to confirm their email address.

Troubleshooting
---------------

There can be several reasons why an email is not sent.  The recipient may never have responded to an opt in email, or they have unsubscribed or perhaps the 
email address is wrong.  To investigate these issues you can.

Review the status of contacts
+++++++++++++++++++++++++++++

Select the ``modules`` menu then ``Campaigns`` and then contacts.  This will show the status of all email addresses that you are using.  Key statuses are:

*  Pending.  The person at the email address has not responded to an opt in message
*  Unsubscribed.  The person has unsubscribed from receiving email messages.

In the first case you can go to the monitoring page and resend the opt in message.  In the second case you will need to contact the person through some other
channel as Smap will not send an email to an unsubscribed address. (other than an invitation to logon to a new account).  The person who owns the email address
can then go to the server home page and select "Subscribe" to resubscribe to emails.

Review opt in messages
++++++++++++++++++++++

Select the ``modules`` menu and then ``monitoring`` and then set the source to ``opt in messages``.  If you specify "Show" as "last 200".  Then the 
last 200 sent outstanding optin email messages will be shown.  You can select "retry" to resend them.

Review Notifications
++++++++++++++++++++

Also on the monitoring page set the source to "notifications".  You can then see the status of each email notification and can retry failed ones.
