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
   
Trigger
-------

The following can trigger a notification:

*  A submission.  A result submitted from a survey.
*  A task reminder.  If a task has not been completed within the specified time.
*  A console update.  When a question is set to a specific value from the console.
*  A case managmeent alert.

Target
------

Notifications can be sent as:

*  An email.
*  An SMS.  Only if SMS has been enabled in the server settings (:ref:`admin-server`)
*  Escalation (assignment) of a case to a user.
*  Forwarding of a submission on to another Smap server. (obsolete)

Adding
------

Click the **Add** button.

1.  Give the notification a name
2.  Select the trigger
3.  Select the notification target
4.  Leave the checkbox **Enabled** as checked (unless you want the notification to be disabled) 

The remaining settings will vary depending on the selections made for **trigger** and **target**

.. note::

  Notifications can be sent to multiple email addresses and SMS phone numbers.

Submission Trigger
++++++++++++++++++

Trigger specific settings are:

*  Survey whose submission triggers the notifications
*  Filter. Restrict which records will trigger a notification.  For example:  "${age} > 80"

Task Reminder Trigger
+++++++++++++++++++++

Task reminders can be specified for a task group.  All tasks created in that task group will then
have reminders associated with them.

.. warning::

  Only task groups that contain tasks generated automatically from submissions to a survey can have 
  a reminder.  Ad-hoc task groups cannot as the tasks can be for multiple surveys.

Trigger specific settings are:

*  Task Group that contains the tasks that will trigger this notification.
*  Interval.  Duration after the task is created that the reminder will be sent if the task is not completed.

.. note::

  The email address to be used for a reminder can be specified directly in the notification, as it can for any other email notification,
  and this is the most reliable approach to use.  You can optionally specify that the email address comes from a question in the source survey 
  that triggered the task.  However this will only
  work if in the task group for "Initial Data" you specified "Pre-populate form with existing data" or "Update existing results".  
  If you specified "No Initial Data"  then the data for the email question is not retained in the task and it can't be used in a reminder notification.

Console Update Trigger
++++++++++++++++++++++

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

Email Target
++++++++++++

Settings are:

*  Attach.  Attach a PDF of the record or a link to a Webform containing the data.
*  Email.  The email address.
*  A question that contains the email address. (If the trigger is a submission of a completed survey)
*  Subject.  The subject of the email.
*  Content.  The body content of the email.  
   
The subject and message content can be customised using data from the submitted results.  Use the following placeholders in either:

*  ${username} :  The user who submitted the results.
*  ${surveyname) : The name of the survey
*  ${hrk} : The key that is created on the server
*  ${instancename} : The instance name that is generated on the server
*  ${device} : The device IMEI used to submit the results
*  ${questionname} : Where questionname is the name of any question in the survey.  

For example::

  ${username} has submitted ${surveyname} with a value of age of ${age}.
  
SMS Target
++++++++++

Settings are:

*  Phone Number
*  A question that contains the phone number in the submission (If the trigger is a submission of a completed survey)
*  SMS Sender Id.  The ID of the sender that is shown to the user when they receive the SMS message
*  SMS content

Forwarding Target
+++++++++++++++++

*  Host.  Where the survey results will be forwarded to. For example https://sg.smap.com.au
*  User.  The user ident on the remote server
*  Password. the password of the above user ident.  (See security warning below)
*  Remote Survey.  The name of the survey on the remote server that the data will be forwarded to.

.. warning::

  The password of the user on the remote server will be stored on the server that you are forwarding from. This password will be
  accessible by the IT systems administrator of this server.  Hence when setting up forwarding it is recommended that you create an
  enum account that only has the security group **enum** to receive the forwarded results.  Do not use an administraot or analyst account.
  
After selecting a target of "Forwarding" a button will be shown labelled "Refresh Form List".  Once you have entered the
host, remote user and remote user password, press this button to get a list of the remote surveys that you can send the data
to. 

.. note::

  The remote survey does not need to be the same as the original survey.  If they are different then only questions in the remote survey
  that have the same name as a question in the source survey will be updated.


