.. _charts:

Charts
======

.. contents::
 :local:
 
An excellent way to provide feedback to a user is by showing charts to present data back to them.  


.. note::

  `Example Survey <https://docs.google.com/spreadsheets/d/19jnl8d86p964IDbEIH3z2pQPoBGep5MJKp_nxA-YhWA/edit#gid=852740487>`_

Adding a Charts
---------------

*  Set the question type to: **chart**
*  Put the data in the **calculation** column.  

Optionally specify the following parameters::

  chart_type=horizontal_bar.  Will show the data as a horizontal bar chart. The default is a line chart
  stacked=yes.  Use with horizontal_bar charts to stack the bars.

Chart Data
----------
The chart data is specified in the calculation column.  Usually you would use yext functions such as the join() function to combine 
answers from questions, or values sources from a CSv file into the correct format.

The rules for constructing data and labels are as follows (Refer to the examples as to how this actually works):

*  Data points are seperated by a single colon  (\:)
*  X Axis Labels are separated by a single colon  (\:)
*  Data is separated from labels using double equals  (==)   Note the labels a placed first.
*  Multiple datasets are seprated using double colon  (\:\:)
*  Labels for data sets are separated from X Axis labels using double colon  (\:\:)  Note the X Axis Labels come before data set labels.

Optionally the X axis numbers can be added to the data.  This can be useful when showing multiple datasets if one of the data sets has missing
data points.  Separate the X Axis number from the value using hash (#).  The X Axis number comes first. Start the X axis numbers from 0.

In this example the second data set does not have a value for the 2nd point in the series (X axis number 1)::

  0#10:1#20:2#30:3#40::0#5:2#7:3#8



Example 1 - Simple Line Chart
-----------------------------

Calculation::

  join(':', '1','2','3', '2')
  
.. figure::  _images/chart1.png
   :align:   center
   :width: 	 300px
   :alt:     Simple Line Chart

   Simple Line Chart

Example 2 - Line Chart with X Axis Labels
------------------------------------------------

In this example the data values are first combined with a colon separator.  Then the X Axis labels are combined again using a colon separator. 
Finally the data is combined with the labels using the double equals separator. 

Calculation::

  data:                 join(':', '26','12','34', '45')
  labels:               join(':', 'A', 'B', 'C', 'D')
  chart calculation:    join('==', ${labels}, ${data})
  
.. figure::  _images/chart2.png
   :align:   center
   :width: 	 300px
   :alt:     Line Chart with X Axis Labels

   Line Chart with X Axis Labels
    
Example 3 - Two Lines with X Axis Labels
----------------------------------------

To show two lines that means showing two data sets.

Calculation::

  dataset_1:            join(':', '26','12','34', '45')
  dataset_2:            join(':', '48','36', '48')
  combined_data:        join('::', ${dataset_1}, ${dataset_2})
  labels:               join(':', 'A', 'B', 'C', 'D')
  chart calculation:    join('==', ${labels}, ${combined_data})

.. figure::  _images/chart3.png
   :align:   center
   :width: 	 300px
   :alt:     Two Lines with X Axis Labels

   Two Lines with X Axis Labels


