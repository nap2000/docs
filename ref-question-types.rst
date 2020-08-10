Question Types
==============

.. contents::
 :local:  
 
Smap supports all the ODK question types as well as additional types specific to Smap.

text
----

*  type:  text

**Parameters:**

*  rows:   Set the number of rows of text shown in the form

**Appearances:**

*  numbers:  Shows the numeric keyboard 
*  thousands-sep:  Inserts a separator between thousands when "numbers" is also used
*  hidden:  Hide the widget in fieldTask

**Availability:**

*  FieldTask: yes
*  Webforms:  yes

**Example**

.. csv-table:: 
  :width: 70
  :widths: 10,10,10
  :header-rows: 1
  :file: tables/widget-text.csv 

.. figure::  _images/widget-text.jpg
   :align: center
   :width: 300px

   Text widget with 5 rows

integer
-------

*  type:  integer

**Appearances:**

*  thousands-sep:  Inserts a separator between thousands 
*  hidden:  Hide the widget in fieldTask

**Availability:**

*  FieldTask: yes
*  Webforms:  yes

**Example**

.. csv-table:: 
  :width: 70
  :widths: 10,10,10
  :header-rows: 1
  :file: tables/widget-integer.csv 

Other ODK Question types
------------------------

*  `decimal <https://docs.opendatakit.org/form-question-types/#decimal-widget>`_
*  `date and time and datetime <https://docs.opendatakit.org/form-question-types/#date-and-time-widgets>`_
*  `select and select_one <https://docs.opendatakit.org/form-question-types/#select-widgets>`_
*  `rank <https://docs.opendatakit.org/form-question-types/#rank-widget>`_
*  `geopoint, geotrace and geoshape <https://docs.opendatakit.org/form-question-types/#location-widgets>`_
*  `image <https://docs.opendatakit.org/form-question-types/#image-widgets>`_
*  `audio <https://docs.opendatakit.org/form-question-types/#audio-widget>`_
*  `video <https://docs.opendatakit.org/form-question-types/#video-widgets>`_
*  `file upload <https://docs.opendatakit.org/form-question-types/#file-upload-widget>`_
*  `barcode <https://docs.opendatakit.org/form-question-types/#barcode-widget>`_
*  `range <https://docs.opendatakit.org/form-question-types/#range-widgets>`_
*  `note <https://docs.opendatakit.org/form-question-types/#note-widget>`_
*  `trigger/acknowledge <https://docs.opendatakit.org/form-question-types/#trigger-acknowledge-widget>`_
*   calculate
*  `"begin group" and "end group" <https://docs.opendatakit.org/form-logic/#groups>`_
*  `"begin repeat" and "end repeat" <https://docs.opendatakit.org/form-logic/#id26>`_
 
Chart
-----

Type:  chart

Shows a chart in the survey. Settings for the graph are specified in the question parameters. More details are available in :ref:`charts`

Not available in Webforms.
 
Child Form / Parent Form
------------------------

Type:  child_form / parent_form

Launches another survey from within the current survey. The difference between these is in how the data from the two surveys
are linked in the results database.  If you don't care about linking the data between the two surveys then either type will do.
Detailed information on using these question types is available in :ref:`launch-survey`.

Not available in Webforms.
