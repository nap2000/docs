
.. _console:

Console
=======

.. contents::
 :local:  
 
The console provides a view of the individual records so that they can be managed.  It is a key component of the Case Management 
capability but is also useful when tracking
submitted result for an Evaluation. 

To get here select the menus *Modules* and then *Console*.

.. figure::  _images/console.jpg
   :align:   center

   The Console
   
Records are shown in order with most recent at the top.  
   
Changing the records displayed
------------------------------

The top half of the page contains the filters.  These are:

* **Project:** Choose the project containing the survey.
* **Survey:** Select the primary survey, that is the one whose data you want to view.
* **Oversight Survey:** Choose a second survey containing questions that you want to add or edit in the primary survey.
* **Form:** The name of a subform whose data you want to view.  This defaults to "none" which means show the data from the main form.
* **Date Question:** If you only want to see data within a date range then use this to choose the date question that you want to filter by. For example the Upload time, start time of the survey or any other date question in the survey.
* **From Date:** The start date of the filter.
* **To Date:** The end date of the filter. This date range is inclusive, so all date that falls on the selected dates and any date between will be shown.
* **Include Deleted:** Select this if you want to see records that have been deleted.
* **My records:** Records that you have selected for editing.
* **Unassigned Records:** Records that no one has selected for editing.
* **Other Records:** Records being edited by other people.
* **Filter:** This is the advanced filter. For help on how to use this click on the (i) info symbol.  An example might be: ${age} < 25.  This would then only show records where the answer to the question "age" was less than 25.
* **Max Records:** The maximum number of records you want to load.  If you set this to 0 then all records will be loaded.  By default this is set to 1,000 so that loading does not take too long when you have a lot of data.  If you have a lot of records you may want to apply other filters to find the ones you are interested in.
* **Show Entries:** Show records in pages with the specified number of rows.  This filter is found just above the table on the left.
* **Search:** Only show records which have the specified text somewhere within them.

Select Filters
++++++++++++++

A drop down select is automatically created for each question of type select_one and placed underneath the colum that it filters.

.. figure::  _images/filter.jpg
   :align:   center

   A select filter on gender

Sorting
+++++++

Clicking on a column heading will sort on that column.  Clicking again will change the sort direction.

Editing a record
----------------

Using an Oversight Surveys
++++++++++++++++++++++++++

Restricting editing of records to using oversight surveys provides a lot of control over what can and cannot be changed.
For example you may have a survey that is used to record customer feedback.  The back office staff are allowed to change
the original status and add comments and resolution but they cannot change any other information collected in the original
feedback.  In this case the oversight form will just have the questions that the back office staff can change.

1.  Select the oversight survey that has the questions to be changed,  the available oversight surveys are those
    surveys in the same group as the main survey
2.  Select the record to be edited
3.  Lock the record.  Only the person who has locked a record, and therefore assigned it to themselves, can
    edit the record.  Administrators can assign records, including those currently locked, to someone else.
4.  Click on the edit button

.. figure::  _images/console2.jpg
   :align:   center
   :alt: The console Edit Page

   Console Edit Page
   
On the console edit page questions are placed in 2 columns. The ones shown on the left are read only. They are the questions in the
main survey where there is no question in the oversight survey with the same name.  The questions on the right are the questions
form the oversight survey and can have their answer changed.  

Hence if you want to be able to change the answer to a question in the main survey then you will need to have a question of the same
name in the oversight survey. To add data to the main survey the question in the oversight survey would not be in the main survey.

Using a webform
+++++++++++++++

If the user has the **enum** security privilege then they can click on the green webform button at the top of the page.  This will 
open the main survey populated with data from the record.  The user can then make changes and submit in the normal webform way.

History Tab
-----------

Clicking on the history tab will show the changes that have been made to the record.  

.. figure::  _images/console3.jpg
   :align:   center
   :alt: Record History

   ord History
   
In the case above there has been one change to the record.  That change only affected a single question.

If you click on the button labelled "1 Changes" then the change is shown.  In this case the work area was adjusted, The old work
area being the blue square while the new work area is the red square.  

.. note::

  Of course if more than one value in the survey had changed then the label of the button would indicate the number of changes.

.. figure::  _images/console4.jpg
   :align:   center
   :alt: Record Change Detail

   Record Change Detail
   
The history tab show changes, tasks and notifications associated with a record.  You can select **sliders** at the top left
of the history page to filter / show these event types.

Assigning Tasks
---------------

When editing a record the user can request that somebody else update the record by assigning a task.   To do this click on 
the **Add Task** button.  A dialog will be shown with similar options as for adding an ad-hoc task.  (:ref:`editing-adding-tasks`).

The differences compared to the task management page are:

1.  The task is automatically set to update the existing record.
2.  The list of surveys that you can select for the task are restricted to those in the current survey group.  All of these surveys
    can work on the current record wheras other surveys not in the survey group cannot.
3.  A task group with the same name as the selected survey will be created automatically to hold this task.

Tasks assigned to a record will be shown in the History tab where you can see their status and edit them.

Sending Notifications
---------------------

An email notification can be sent with an attached PDF or a link to a Webform containing the record data. This notification
will also be shown in the record history.  Next to the notification will be shown a button labelled "Resend" that can be clicked
to resend a notification.