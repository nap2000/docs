Pulldata from Subforms
======================

.. contents::
 :local:
 
You may need to review data from another survey's Sub Form (begin repeat) while working offline. The pulldata function can look up
answers to questions recorded in another survey howver it does not work well with varying numbers of repeats.  For example while 
operating offline you may want to show previous results for the last 3 inspections of a piece of equipment.

.. note::

  `Example Survey <https://drive.google.com/drive/u/0/folders/16dI2RPsMadTQTRLi_pIuZJ8XIJPjqdoA>`_. This survey  shows comments from 
  previous visits and then gets a comment from the current visit.

Specifying Repeating Pulldata
-----------------------------

To look up data from another survey you will need its identifier. (:ref:`survey-ident`). For a normal pull data this identifier just needs
to be specified in a **search** function or **pulldata** function in order to get lookup data in the survey.  However in this case, since 
data from sub forms is also required we need to specify that a csv reference file be generated containing the sub form data grouped
by data in the main form.

This can be done in the online editor by:

#.  Selecting the menu **File** then **Repeating Pulldata**
#.  Enter the survey identifier in the survey field
#.  Enter the data key.  
#.  Then press **Save**

Once this is done you will be able to look up the repeating data by specifiying the data key value and all the repeats matching that
key value will be returned.

.. figure::  _images/sf_pd.jpg
   :align:   center
   :width: 	 400px
   :alt:     Repeating Pulldata

   Specifying Repeating Pulldata

Resultant CSV File
------------------


.. figure::  _images/sf_pd2.jpg
   :align:   center
   :width: 	 400px
   :alt:     A CSV file generated for repeating pulldata

   Repeating CSV File
   
The CSV file has two special columns

#.  _data_key: Contains the value of the key for each record
#.  _count: Contains the number of repeating records for that key

The other columns contain the data that you request in your pulldata() functions

In the _data_key column are the unique keys that the pulldata function can use to extract the data.
Where the record is for data within a begine repeat then these have an “_” and a number appended to the key.  So in the example above the key value of “1” has two repeating records with key values “1_1” and “1_2”

The pulldata function
---------------------

Identify the form using::

  linked_s_pd_{survey identifier}
  
**linked_s** means get the data from another survey and not from a CSV file.  **_pd** means the data will be in the repeating pull data format.

Example::

  pulldata('linked_s_pd_self', 'comment', '_data_key', ${visit_key} )
  This means get the value from the question comment from previous submissions to this survey 
  where the key is the value in the question called 'visit_key'.
  
