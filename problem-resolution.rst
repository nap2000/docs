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

The above detailed view shows that the error is caused by "text" answer(character varying) being written
to an integer column in the database.  The column name is "id".  When you are editing a survey you cannot
change a question of type integer to text.  If you come across this follow the instruction in
:ref:`prob_type_change` to resolve it.

.. _prob_type_change:

Question type has changed to an incompatible value
--------------------------------------------------

The easiest way to fix this is to "restore" the survey in the analysis module.