.. _cm-references:

References
==========

Available with Smap Server version 26.06+.

.. contents::
 :local:

A *reference* gives one or more users **read-only** access to a record. Unlike
an assignment (or escalation), which hands a single owner the right to update a
case, a reference simply lets people see a record. Many users can reference the
same record at once, and adding or removing a reference never changes who the
record is assigned to.

Use a reference when somebody needs to *watch* a case rather than work on it -
for example a supervisor who wants visibility of a case owned by a field worker,
or every member of a unit who should be able to read a record that one of them
will eventually action.

References versus assignments
-----------------------------

+---------------------------+-------------------------------+-------------------------------+
|                           | Assignment                    | Reference                     |
+===========================+===============================+===============================+
| Number of holders         | One owner at a time           | Many users at once            |
+---------------------------+-------------------------------+-------------------------------+
| Access                    | Read and update               | Read only                     |
+---------------------------+-------------------------------+-------------------------------+
| Changes the case owner    | Yes                           | No                            |
+---------------------------+-------------------------------+-------------------------------+
| Typical use               | Do the work on a case         | Watch / have visibility       |
+---------------------------+-------------------------------+-------------------------------+

Behind the scenes a reference is recorded against the record and is written to
the record's history, so you can always see when access was granted or removed
and by whom.

Creating a reference
--------------------

In the console
++++++++++++++

Open the :ref:`console` and select a single record. If you do not already
reference it, a **Reference** button is shown; click it to give yourself
read-only access. Records you reference are indicated in the assignment column
of the record table so they are easy to pick out.

To give yourself access to several records, reference each one in turn.

Automatically with a reference notification
+++++++++++++++++++++++++++++++++++++++++++

References can also be granted automatically, in the same way that cases are
assigned automatically. Add a **Reference** target to a :ref:`notification
<notifications>`, or add a **Reference** step on the :ref:`workflow` page. The
reference is then granted whenever the notification is triggered - for example on
submission of a new record, on an update, or after a case alert.

When configuring the reference, choose who should receive read-only access:

*  A **named user**.
*  The **submitter** of the record.
*  A user named in the **data** - the value of a question on the form.
*  All members of a **role**. Because a reference can be held by many users, the
   role is expanded to every one of its members at the time the notification
   fires.

The reference target reuses the same assign-by-user or assign-by-role controls
as escalation, but because it only grants read access it sends no email.

Working with references
-----------------------

Console
+++++++

Records you reference are highlighted in the record table. Selecting a record you
reference shows a **De-reference** button in place of **Reference** (see
`Removing a reference`_ below).

WebForms (My Work)
++++++++++++++++++

Records referenced to a user appear in a separate, read-only list on the user's
*My Work* page, distinct from the tasks and cases they have been assigned.
Opening a referenced record opens it read only.

FieldTask
+++++++++

On the device, references are kept apart from actionable work. When you have any
references, a **Tasks / References** toggle appears at the top of the Tasks tab;
switch to **References** to see them. Referenced records are shown in their own
colour, open read only, and have none of the accept / reject / release actions of
a task or case. References do not count towards the badge on the Tasks tab.

Where the underlying record is assigned to someone, the reference shows who it is
assigned to (or that it is unassigned), so a watcher can see who is working on it.

Removing a reference
--------------------

Removing a reference is called *de-referencing*. It only removes read-only
access; it does not affect the record or its assignment.

*  **Console** - select a record you reference and click **De-reference**.
*  **FieldTask** - swipe a reference off the list. The reference is removed
   immediately and an undo is offered; it is committed when the undo is
   dismissed. Dereferenced records are hidden from the list. When the device next
   submits, the de-reference is sent back to the server so the reference is
   removed there too.

A reference notification can also remove access: when it resolves to no users, no
reference is granted.
