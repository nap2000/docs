Deleting and Restoring Data
===========================

There are 4 levels of data deletion each one more final than the previous ones.

#.  Marking as deleted
#.  Deleting all records
#.  Deleting the Survey Template and all its records
#.  Erasing the survey Template and all its records

Marking Deleted
---------------

Records marked as deleted are not actually deleted but they no longer appear in exports and are not used when creating charts.  They are also not visible in 
the console unless you specifically request to see them.

.. note::

  Marking records as deleted is the recommended way to delete records that you don't want.  It leaves a clear audit trail and can easily be reversed if necessary.

.. figure::  _images/delete1.jpg
   :align:   center
   :width: 	 600px
   :alt:     Marking Deleted in the Console

   Marking Records Deleted in the Console
   
The :ref:`console` can be used.  Select the record you want to delete and then click the delete button. You can optionally
enter a reason.

Restoring Records marked as Deleted
+++++++++++++++++++++++++++++++++++

.. figure::  _images/delete2.jpg
   :align:   center
   :width: 	 600px
   :alt:     Marking as Not Deleted in the Console

   Marking Records as Not Deleted in the Console
   
To restore a record toggle the switch "Include Deleted" then select the record you want to restore and click "Undelete".  You can optionally
enter a reason.

Deleting all Records
--------------------

This is still done in a table view of the analysis page.   You can mark records deleted here as well but the console is now the preferred
place to do that.

Create a table view of your survey. To do this click on the table button, then select your survey and press OK. Then click on the aside button "<".

.. figure::  _images/delete3.jpg
   :align:   center
   :width: 	 600px
   :alt:     Deleting All Records

   Deleting All Records
   
You can then click on the button to delete the data.

Restoring All Records
+++++++++++++++++++++

Underneath the "Delete Data" button is the "Restore Data" button.  This will restore the data by replaying all the submissions.

.. warning::

  Because the records are restored from the initial raw submissions, if you have done any data cleaning or updated the data via the console
  then these changes will be lost.
  
Deleting the Survey Template
----------------------------

On the survey management page you can click the checkbox next to surveys you no longer want and then click the "Delete Forms" button at 
the bottom of the page.  The surveys and all their data will be deleted.

Restoring Deleted Surveys
+++++++++++++++++++++++++

Deleted surveys are easily recovered.  Select the checkbox marked "Show deleted forms" at the top of the form management page.  
Deleted surveys will be shown in red with the date and time that they were deleted appended to their name.  Select the ones that
you want to restore and click the "Restore Forms" button.

.. note::

  Deleted surveys will be automatically erased after 100 days.

Erasing Survey Templates
------------------------

Only deleted surveys can be erased.  Follow the steps for restoring deleted surveys but instead of clicking on "Restore Forms" click
on "Erase Forms".  

.. warning::

  Erased surveys can only be restored from data backups which requires work by IT operations.  So it won't happen unless you have a
  support contract.


   
Automatically Deleted Records
-----------------------------

When a record is updated then the old record is marked as deleted.  You will see these with a reason that looks like "replaced by 123".  123 in
this case being the primary key of the new updated record.

