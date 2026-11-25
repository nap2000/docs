.. _complete_case:

Cases
=====

A status question and the value of that status question that indicates a case is complete can be specified for a survey. Completed
records, that are not assigned to a user, are then hidden by default in the console although they can be shown if the "Include Completed Cases" option is selected.
(:ref:`case-management-config`)

.. _case_reopen:

Closing and Reopening
---------------------

Requires Smap Server version 26.12+.

Several status values can close a case, for example resolved, withdrawn and duplicate.  Choose them in **Closed statuses**
in the case settings.  When the status question is a select one question its answers are listed to select from; hold
Ctrl, or Cmd on a Mac, to select more than one.  For any other status question enter the values separated by commas.

A case closes and reopens because of its data.  There is no separate action:

*  When a change to a record sets its status to one of the closed values, the case closes.  The date it closed is
   recorded, the history shows who had the case, and they are all taken off it.  Changing to another closed value
   leaves it closed, with the date it first closed.
*  When a change sets the status of a closed case to any other value, the case reopens.  The history records it, the
   people who had the case when it closed get it back, unless they can no longer be given it, in which case the history
   lists them.  Its alerts can fire again, timed from when it reopened, and a notification with the **Case reopened**
   trigger is sent, see :ref:`notifications`.

The change can be a submission, including from a later survey in the bundle that does not ask the status question, an
update in the console, a bulk update, or an update through the API.  A case can also be closed by the submission that
creates it, or by importing data, and the history records that too.  An imported case keeps the closed date it brings
with it.

In Operations, record lists show how many times each case has been reopened.

.. _criticality_case:

Criticality
-----------

A question in a form can be specified as representing criticality.  You can then create charts showing the 
criticality of the cases currently in the console.
(:ref:`case-management-config`)

.. _case_alerts:

Alerts
------

Alerts can be added to cases.  These are triggered a specified period of time after the case is first created. 
The alert is then shown in the console and can also be used to trigger notifications or escalations of the case. In 
the console you can view the current alert on a record in the table view and create a chart in the chart view to 
show a summary of current alerts.
(:ref:`case-management-config`)
