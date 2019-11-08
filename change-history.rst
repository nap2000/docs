.. _change-history:

Change History
==============

.. contents::
 :local:

The change history page is part of the :ref:`online-editor`. To get to it, select a survey to edit then 
select **Tools** then **Change History**.

Each time a survey is changed the following information is recorded in the change history.

*  The version number created by the change
*  A description of the change
*  The person who made the changed
*  Date and Time
*  File.  The XLS file if the survey was replaced by another XLS Form.  Or the PDF template if a new template was loaded.
*  Message.  Any errors or other messages from the system about the change.

Example
-------

The diagram below shows the changes page for a survey that has the following history:

*  Initially loaded from an XLS Form (Version 1)
*  Using the online editor two new questions were added, and a label and a relevance were changed. (Version 2)
*  The survey form was exported, modified in a spreadsheet editor and then this updated XLSForm was used to replace
   the Survey (Version 3)
   
.. figure::  _images/changes1.jpg
   :align:   center
   :alt:     Change History

   Change History
   
The changes made in the online editor are shown directly in the change history.  Individual changes such as a 
new question added, are not shown when the changes were made in an XLSForm and then this file replaces the existingHowever
survey.  However a link is provided to the XLSForm that was loaded so that it can be downloaded and inspected.

Relating Results to Survey Versions
-----------------------------------

.. figure::  _images/changes2.jpg
   :align:   center
   :alt:     Survey Version in Results

   Survey Version in Results
   
Exported results include the survey name and version for each record.  In the above example the first record was
submitted using version 1 of the survey, the second using version 3.  

Since version 3 had more questions, the answers to these are missing from the first record. However using the version number
recorded next to each record along with the change history it is possible to assess the impact of using an older version on 
the data quality.
