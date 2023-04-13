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

Choosing the Form
-----------------

When assigning a user to a record you can specify the form that they will use to update it.   When assigning manually
from the console first select the survey form that you want to use, then select the record and assign it.  When 
assigning automatically using a notification you can specify the form to use in the notification dialog.
