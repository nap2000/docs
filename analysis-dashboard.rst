Dashboard
=========

.. contents::
 :local:
 
The purpose of the dashboard is to give a quick insight into the data for Quality Assurance. They are not a
substitute for an analysis system such as Excel, or a GIS.

Managing Panels
---------------

Adding Panels
+++++++++++++

.. figure::  _images/analysis1.jpg
   :align:   center
   :width:   300px
   :alt:     Adding a Panel
   
   Adding a Panel
   
Click on one of the add panel buttons for graph, table, map or image chart types... _integration:

Resizing a Panel
++++++++++++++++

.. figure::  _images/analysis2.jpg
   :align:   center
   :width:   300px
   :alt:     Resizing a Panel
   
   Resizing a Panel
   
Editing a Panel
+++++++++++++++

.. figure::  _images/analysis3.jpg
   :align:   center
   :width:   300px
   :alt:     Editing a Panel
   
   Editing a Panel
   
Clicking on the settings icon will open the same dialog that was used in creating the panel.  Clicking on the "data view"
will open a side panel that allows selection of map layers or sub forms in a survey.  For a graph created from
select question repsonses, the choices that are shown can be selected.

Panel Settings
--------------

Subject
+++++++

For all panel types the default subject is "data".  However for table and map charts you can select one of:

*  Data
*  User Activity
*  User Locations

**Data** subjects show information collected for a specific survey including the answers to the survey specific question. 

**User Activity** subjects show information about the activities of a specific user for all surveys that they have completed.  This 
information includes meta data about a survey:

*  Location
*  Survey name
*  Upload Time
*  Start Time
*  End Time
*  Device
*  Comments on survey
*  Instance Name 
*  Scheduled Start (For tasks)

**User Locations**

For a map panel this shows the location at which the users last refreshed fieldTask.  Each users location is represented by a colored circle with their name in
red next to it.  The colour of the circle changes depending on the length of time since they refreshed their phone:

*  less than 1 hour - red
*  between 1 and 2 hours - orange
*  between 2 and 3 hours - yellow
*  between 3 and 4 hours - green
*  more than 4 hours - blue

for a table panel the last refresh time is shown  for each user.

.. warning::

  If no location is available with the last refresh then the user will not be shown in either the map panel or the table panel.

Survey
++++++

Select the survey whose data you want to show.

.. note::

  This option is only used with "data" subjects.

User
++++

Select the user whose activity you want to show.

.. note::

  Only for "User Activity" subjects.
