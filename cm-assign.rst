.. _create_case:

Assigning a Record
==================

Any record assigned to a user can be managed as a case.  

Manually Create/Escalate
------------------------

Use the console to assign yourself or another user to a record.

#.  Select the record to be assigned
#.  Click on the "Edit" button to assign the record to yourself
#.  If you have admin security privilege, you can also click the button "Assign User" to assign somebody else.  This can be done even if the case is already assigned in order to reassign it.

Manually Close
--------------

Use the console to close a case manually.

#.  Select the record to be un-assigned
#.  Click on release if it is assigned to you
#.  If you admin security privilege you can also click on the button "Assign User" and assign it to "None".

.. _case_escalation:

Case Escalation
---------------

The escalation of a case is its re-assignment to a different person after an event.  This can be done manually
in the console or automatically using a notification.

Automatic Assignment
--------------------

Records can be automatically assigned to users using :ref:`notifications`. The notification could be initiated by:

*  Submission of a new record.  Resulting in the initial assignment of that record.
*  Submission of an update to a record.  Potentially resulting in escalation of the record or an initial assignment if tit is not currently assigned.
*  A case alert.  The Survey has to be defined as a proper case with a status that can be set to closed.  Then if alerts can be created if the record is not closed within a set time and these can trigger a notification to escalate the case.

.. _multiple_assignees:

Multiple Assignees
------------------

Available with Smap Server version 26.12.01+.

By default a case is assigned to one person at a time.  Turn on **Allow multiple assignees** in the bundle's case
settings, see :ref:`case-management-config`, to let a case be assigned to several people at once, all with the same
access to it.  Saves made by different people are merged, see :ref:`console_conflicts`.

With multiple assignees:

*  **Console.**  The **Assign User** dialog lists who has the case.  Choose somebody in **Add user** and save to add
   them.  To add a whole role, pick it in **Show users in role**, choose **Everyone in** the role at the top of
   **Add user**, and save: every member of the role who can be given the case is added.  Each person
   added is checked as a single assignment is.  An administrator can take anyone off with the remove button next to
   their name, or take everybody off with **Unassign all**.
*  **Lock for Editing** adds you to the people who have the case, even if others have it.  **Release** takes only you
   off.
*  **Devices.**  Everyone assigned gets the case.  Rejecting it on a device takes only that person off.
*  **Escalation.**  An escalation adds its people, and takes off the people any earlier escalation added.  People
   assigned in the console stay.  An escalation to a role adds every member of the role who can access the record,
   and one that assigns from a select multiple question adds everyone selected.  See :ref:`notifications`.
*  **Closing a case** takes everybody off it.
*  **Emails** sent to the assigned user go to everyone assigned.
*  The **Assigned** column lists everyone assigned, separated by commas.

If a bundle does not allow multiple assignees, an escalation to a role assigns the first member of the role who can
have the case, and setting up such an escalation shows a warning.  Turning the setting off leaves cases that already
have several people assigned as they are until they are next changed.

Choosing the Form
-----------------

When assigning a user to a record you can specify the form that they will use to update it.   When assigning manually
from the console first select the survey form that you want to use, then select the record and assign it.  When 
assigning automatically using a notification you can specify the form to use in the notification dialog.
