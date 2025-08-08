.. _notifications:

Notifications
=============

.. contents::
 :local:

To get to the notifications page select the **Tasks** module and then **Notifications**.

.. figure::  _images/notifications1.jpg
   :align:   center
   :alt:     Notifications Page

   Notifications Page
   
Adding
------

Click the **Add** button.

1.  Give the notification a name
2.  Select the trigger
3.  Select the notification target
4.  Leave the checkbox **Enabled** as checked (unless you want the notification to be disabled) 

The remaining settings will vary depending on the selections made for **trigger** and **target**

.. note::

  Notifications can be sent to multiple comma separated email addresses.

Trigger
-------

The following can trigger a notification:

*  A submission.  A result submitted from a survey. Including submission from an oversight form (replaces old console update)
*  A task reminder.  If a task has not been completed within the specified time.
*  A case management alert.
*  A periodic timer. Daily, weekly, monthly, quarterly or yearly.
*  A Server Calculation change

Submission
++++++++++

Settings include:

*  Trigger from any survey in the selected bundle or from a specific survey
*  Survey or bundle whose submission triggers the notifications
*  Filter. Restrict which records will trigger a notification.  For example:  "${age} > 80"

Task Reminder
+++++++++++++

Task reminders can be specified for a task group.  All tasks created in that task group will then
have reminders associated with them.

.. warning::

  Only task groups that contain tasks generated automatically from submissions to a survey can have 
  a reminder.

Settings include:

*  Task Group that contains the tasks that will trigger this notification.
*  Interval.  Duration after the task is created that the reminder will be sent if the task is not completed.

.. note::

  The email address to be used for a reminder can be specified directly in the notification, as it can for any other email notification,
  and this is the most reliable approach to use.  You can optionally specify that the email address comes from a question in the source survey 
  that triggered the task.  However this will only
  work if in the task group for "Initial Data" you specified "Pre-populate form with existing data" or "Update existing results".  
  If you specified "No Initial Data"  then the data for the email question is not retained in the task and it can't be used in a reminder notification.

Console Update
++++++++++++++

In this case the objective is to send a notification when an update is made to the survey via the console.  For example an administrator
might approve a request.  The notification will be sent only when a specific value is set in a specific question.

The settings are:

*  The same triggers as per submission.  That is specify the survey that is being updated and any filters on which records trigger the update.
*  The oversight survey that is making the change.
*  The question in the oversight survey that when updated triggers the notification.
*  The value of the update question.

.. note::

  The filters are evaluated after an update is applied.  Hence if you have an update notification that is triggered when status is set to "critical"
  and you add a filter that this only applies to "region 1".  Then if the user updates a record and sets the status to "critical" and the region to "region 2"
  then the notification will not be triggered.  However if they set the region to "region 1" or it was already "region 1" then the notification will be
  triggered 

Periodic
++++++++

Available with Smap 23.07.

Periodic triggers run reports and automatically send them via email. The data in the report will be filterd by dates
determined by the selected period.

*  Daily: Data from the day before will be included.
*  Weekly: Data from the previous week will be included.
*  Monthly: Data from the previous month will be included.
*  Quarterly: Data from the previous quarter will be included.  (Available in version 25.02+)
*  Yearly: Data from the previous year will be included.

.. note::

  Data submitted the same day that the report is generated will not be included.  So you can set a daily report to be created at 10am every monday and it will include data from the previous 7 days up until midnight on Sunday.

.. note::

  If you have set a start and end date in a report run automatically by a periodic notification, then these will be ignored.  However you can still set date ranges in the advanced filter for a report and these will be applied.

The settings are:

*  Report.  The report to run (only xlsx reports are supported). The report must be set up in the reports module as a public report.
*  Target. Only email is available for periodic notifications
*  Period. Daily, weekly, monthly or yearly
*  Time. The time of day at which the trigger should fire
*  Day of the week. (Only if weekly is set as the period)
*  Day of the month. (Only if monthly or yearly is set as the period)
*  Month.  (Only if yearly is set as the period)
*  Email. A comma separated list of email addresses that should be sent the report
*  Subject. The email subject.
*  Content. The email content.

Server Calculation
++++++++++++++++++

Available with Smap 24.03

In notifications select a trigger of “Server Calculation”. You will also need to specify:

#.  The survey containing the server calculation
#.  The Server Calculation question
#.  The value that will trigger the notification. Note this value should be text and quotes are not required.

Target
------

Notifications can be sent as:

*  An email.
*  An SMS.  Only if SMS has been enabled in the server settings (:ref:`admin-server`)
*  Escalation (assignment) of a case to a user.

Email
+++++

Settings are:

*  Attach.  Attach a PDF of the record or a link to a Webform containing the data. (Not available for periodic triggers).
*  Email.  One or more comma separated email addresses
*  A question that contains the email address. (If the trigger is a submission of a completed survey, not periodic triggrs)
*  Subject.  The subject of the email.
*  Content.  The body content of the email.  
   
.. note::

  Email questions can be of type select multiple or select one.  Enter the email address as the name of the choice

The subject and message content can be customised using data from the submitted results.  Use the following placeholders in either:

*  ${username} :  The user who submitted the results.
*  ${surveyname) : The name of the survey
*  ${hrk} : The key that is created on the server
*  ${instancename} : The instance name that is generated on the server
*  ${device} : The device IMEI used to submit the results
*  ${questionname} : Where questionname is the name of any question in the survey.
*  ${assigned} : The person assigned the record as a case.
*  ${url} : The link to a webform if you specified that a webform should be included in the email

For example::

  ${username} has submitted ${surveyname} with a value of age of ${age}.
  
SMS
+++

Settings are:

*  Phone Number
*  A question that contains the phone number in the submission (If the trigger is a submission of a completed survey)
*  SMS Sender Id.  The ID of the sender that is shown to the user when they receive the SMS message
*  SMS content

Escalation
++++++++++

An escalation assigns a case to a user.  The word usually means that the case has been reassigned to a different
user because it has been "escalated" in importance, however it can be used to assign a user to an unassigned case.

Settings are:

*  User to assign
*  The survey for the user to complete. The survey needs to be in the same bundle as the survey that triggered the notification.

An escalation can be accompanied by emails.  The settings are similar to the "email" target with the addition of a 
checkbox that allows you to send the email to the assigned user

