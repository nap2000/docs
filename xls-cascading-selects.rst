Choice Filters and Cascading Selects
====================================

.. contents::
 :local:

Sometimes the options you need to present to a user will depend on previous choices that they have made. 
One common case is the selection of a community name from a list. You may want to first select a “region” and 
then select one of the communities in that region.  Hence the “select_one” question for the community should only 
show the communities that are in the selected region

Cascading Selects
-----------------

Choices Worksheet
+++++++++++++++++

*  Firstly you need to add some filters to the choices worksheet
*  These are additional columns where you specify the values that will make an option relevant
*  Each filter must have a name that goes into row 1
*  Each option that is to be filtered then has a value in that filters column
*  The value in the filters column should match the value returned by a previously asked select question

.. figure::  _images/cascade1.jpg
   :align:   center
   :width: 	 600px
   :alt:     Filters in choices worksheet

   Filters in choices worksheet
   
Survey Worksheet
++++++++++++++++

For the select questions that you want to filter you need to specify the selection rule in a column called choice_filter

The filter rule looks like this::

  sc_filter=${sub_county}
  
You can use “and” to refer to multiple filters::

  sc_filter=${sub_county} and parish_filter=${parish}
  
.. note::

  Referring to multiple filter columns in a cascading select is rarely necessary.  You should make all of your codes unique
  irrespective of the actual name of the locality.  For example if you have a parish called "pudo" in both sub county "mucwini"
  and sub county "lagoro" then you should give them different codes such as "pudo_a" and "pudo_b".  In this way as all the parish 
  codes are unique when you specify a choice filter for the village you can just use:
  
  parish_filter=${parish}
  
.. figure::  _images/cascade2.jpg
   :align:   center
   :width: 	 600px
   :alt:     choice filter in survey worksheet

   Choice filter in survey worksheet





