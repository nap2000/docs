Problem Resolution
==================

.. contents::
 :local:

Submitted Data does not appear in the console or analysis module
----------------------------------------------------------------

The first place to look is :ref:`admin_monitor`,   Select the "submitted" tab and see if your survey has
anything in the "Errors" column.

.. figure::  _images/prob1.jpg
   :align:   center
   :alt:     The monitoring page showing an error in a submission

   Monitoring Page Showing an Error

To view the reason for the error; change "Show" to "Last 200".  This will show details on each
submission.  You can filter to only show Errors if you want to zero on the errors.

.. figure::  _images/prob2.jpg
   :align:   center
   :alt:     Showing the error details

   Error Details

In the above image, the error is caused by an answer of type "text" (character varying) being written
to a column of type integer in the database.  The column name is "id".  When you are editing a survey you cannot
change a question of type integer to text.  If you come across this follow the instruction in
:ref:`prob_type_change` to resolve it.

.. _prob_type_change:

Question type has changed to an incompatible value
--------------------------------------------------

The easiest way to fix this is to :ref:`analysis-delete-restore` the survey in the analysis module.

.. warning::

    Restore first deletes the old data including its table then recreates it with the latest
    survey definition, so the latest question types, it then reapplies all of the submissions.
    However this won't always work.  **Firstly** if you have changed the data since it was submitted then
    you will lose all of those changes.  **Secondly** if you changed the data type from say "text" to "integer" and
    if some of the early submitted data was values like "Only One" then that will now fail when the submissions
    are reapplied.  However changing integer to text should always work. In both of these cases you will
    need to use one of the other methods described below..

Fixing incompatible types with backup restore
+++++++++++++++++++++++++++++++++++++++++++++

#.  First backup the existing data
#.  Then delete the data using the analysis module (:ref:`analysis-delete-restore`)
#.  Then restore the backed up data
#.  Finally using the monitoring page re-apply the failed submissions (:ref:`admin_monitor_reapply`)

Fixing incompatible types using SQL statements
++++++++++++++++++++++++++++++++++++++++++++++

#.  Get the table name using the online editor and selecting the menu "File" and then "Info"
#.  Open the "results" database
#.  Get the column name, this will be similar to the question name but all lower case.  in psql use \d {table name}
#.  Alter the column type in PSQL: alter table {table name} alter column {column name} type {new type}
#.  Types could be text, integer, timestamp with timezone or double precision
#.  If there is incompatible data already in the table you will have to do some conversions to new valid data
#.  Then go to the monitoring page, select the survey and click on "Re-apply Failed Uploads"
