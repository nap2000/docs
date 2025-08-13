.. _admin_monitor:

Monitoring
==========

.. contents::
 :local:

The monitoring page can be used to track down problems with submissions of data or notifications. 
To access it select the `admin` module and then the `monitoring` menu option. 

The page has multiple tabs each of which show events from a different source.

Submissions
-----------

Totals
++++++

By default monitoring will show submission totals.

.. figure::  _images/monitor-submissions.jpg
   :align:   center
   :alt:     The monitoring page showing submission totals

   Submission Totals

Details
+++++++

Show show details on each submission including error messages select

.. figure::  _images/monitor-submissions-detail.jpg
   :align:   center
   :alt:     The monitoring page showing submission details

   Submission Details

Select "last (200)" to see details on the last two hundred submissions. If you have a lot of submissions or the problem happened a significant
amount of time ago then you can:

*  page through these submissions using the buttons labelled ">>>" and to get the previous 200 "<<<"
*  restrict the details to a single survey by selecting the project and then the survey
*  uncheck the status values that you are not interested in.  For example you may not want to see successful submissions so unchecking that will hopefully remove a lot of the unneeded details

.. _admin_monitor_reapply:

Re-apply failed uploads
+++++++++++++++++++++++

This button will be shown if you select a specific survey and it will be enabled if submissions have failed to be applied to the database.  Unless the underlying
reason for the failure has been resolved there will be little point in clicking the button however, if you believe the problem may have been fixed then press the button.
The submissions in error should immediately be removed from the list.  They will either reappear as "success" or as an "error" again, after they have been processed.

Notifications
-------------

This shows the notifications that have been sent. When viewing the last 200 of these, you can select a retry 
button to resend a failed notification.

Opt in messages
---------------

Opt in messages are sent once to an email user before they are sent email tasks or email notifications.  You can view the status of these messages here. You
can request a resend of an opt-in message but you should check first with the recipient that they do actually want to opt in to email messaging.

Cases
-----

Shows number of new cases created per day and the number closed for the selected survey.

.. figure::  _images/monitor-cases.jpg
   :align:   center
   :alt:     The monitoring page showing cases created and closed per day as a bar chart

   Cases
