
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
   
Changing the records in the table
---------------------------------

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
