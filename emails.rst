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

Mail programs such as Gmail, Outlook and Apple Mail can also show their own unsubscribe button next to the sender.  This unsubscribes the
person straight away, without opening the unsubscribe page.  Gmail and Yahoo expect this of organisations that send a lot of email, and
without it people who want no more emails are more likely to report them as spam.  Requires Smap Server version 26.11+.

Subscribe
---------

If someone wants to receive emails again they can go to the home page of the server and select subscribe.  They will then be asked to enter
their email address.  If they are unsubscribed from 1 or more organisations then an email is sent to that address for each of those
organisations, with a link to subscribe to it again.  Clicking the link confirms the subscription.

The page shows the same message whether or not the address has unsubscribed from anything, so it does not reveal which organisations an
address belongs to.  Only one request can be made for an address every 10 minutes.  This applies to Smap Server version 26.11+, earlier
versions listed the organisations on the page.

The subscribe link works once and expires after 30 days.  If it has expired, or has already been used, ask for a new one on the
subscriptions page.  The unsubscribe link in an email cannot be used to subscribe again after unsubscribing.  This applies to Smap Server
version 26.11+.

Opt in
------

Before mailouts, tasks or notifications are sent to an email address the recipient needs to "opt in".  More accurately we just want them to 
confirm their email address.  Until the user opts in other emails are held in a pending state.

For email mailouts the opt in email is the first email that the person is sent.  If they complete the requested survey then the user is marked as 
opted in.

For notifications a special opt in email is sent allowing the user to confirm their email address.  From Smap Server version 26.11 the
link in it works once and expires after 30 days.  If it expires before the person responds, the opt in email can be sent again from the
monitoring page, see `Review opt in messages`_.

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
