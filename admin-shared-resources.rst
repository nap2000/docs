.. _shared-resources:

Shared Resources
================

.. contents::
  :local:

To get to shared resources select the **Admin** module and then **Shared Resources**.

Shared resources are made available to all surveys in an organisation.  They conist of:

*  Images, Video, Audio that can be included in questions and choices
*  CSV files that contain reference data accessed using the search() function and the pulldata() function
*  Maps used on the server for analysis
*  Locations

Media / CSV Files
-----------------

Maps
----

Locations
---------

Select the **Location** tab.

.. figure::  _images/sharedResources1.jpg
   :align:   center
   :alt:     Locations
   
   Locations
   
Locations identify where a task should take place.  They consist of GPS Coordinates and/or the ID of an NFC chip that will
launch the task.  The use of NFC chips allows a much greater precision in identify the task location as the NFC chip may
be on a particular peice of equipment that needs to be maintained or control access to a room where the survey needs to take
place.

When :ref:`editing-adding-tasks` you can select a named location rather than specifying the GPS coordinates / NFC chip. However
you can also create new named locations while adding tasks.

Locations are stored in Groups which are defined in a spreadsheet.  One group per worksheet.  

Editing / Adding Groups
+++++++++++++++++++++++

Click the download button.  This will download all the groups of locations into a spreadsheet.  If there are no existing
locations then this spreadsheet will have a single default worksheet called **Group**.  The headings are::

  UID - Enter the ID of the NFC chip here
  name - name of the location
  lat - Latitude of the location
  lon - longitude of the location
  
Rename the group worksheet.  Add additional groups if required.  Add locations to these groups and then to upload and replace
the existing locations:

1.  Click on Add Files
2.  Click on Upload


