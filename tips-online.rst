Looking up data Online
======================

.. contents::
 :local:
 
Situatution
-----------

You may find yourself using large reference files to lookup choices using the search() function; or individual data items using the pulldata() function.
If these files become large and they are updated often then you may experience the following issues:

*  Every time a user of fieldTask opens a form that uses the reference data then all of that data has to be loaded into memory which can be slow.
*  When the reference data is changed it has to be downloaded onto all the enumerator phones.  So if the file was say 5 MB in size and you had
   100 enumerators that would be 500MB of data downloading.  This will become a major issue if the reference file is updated multiple times per
   day.

Solution
--------

Use online search and lookup::

  search()  =>  lookup_choices()
  pulldata()  =>  lookup()

You just need to change the function name, the parameters remain the same.

Comments
--------

#.  There is a minor delay when looking up the data however overall performance should be faster as all the data does not need to be loaded when the form
    is opened.
#.  The enumerator has to be online and will need a data sim in the phone


This solution will suit a dynamic survey with large reference files that are constantly being updated and that is conducted in an areas with a mobile
data network.   

If your project requires work to be done offline then you should design is so that updates to the reference data are not too frequent and are managed to minimise
the impact of downloading the data.  For example you could schedule updates to the reference data when the data collectors are all at the base location with good
wifi.


