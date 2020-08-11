Question Types
==============

.. contents::
 :local:  
 
Smap supports all the ODK question types as well as additional types specific to Smap.

text
----

Use for questions that require a text response.  It can also be used with the numbers appearance to get integer responses that are longer
than the 9 character limit of the **integer** type.

**Type**

*  text

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
  :width: 30
  :widths: 10,10,10
  :header-rows: 1
  :file: tables/widget-text.csv 

.. figure::  _images/widget-text.jpg
   :align: center
   :width: 300px

   Text widget with 5 rows

integer
-------

Number questions that don't allow a decimal point and are not longer than 9 digits.

**Type**

*  integer

**Appearances:**

*  thousands-sep:  Inserts a separator between thousands 
*  hidden:  Hide the widget in fieldTask

**Availability:**

*  FieldTask: yes
*  Webforms:  yes

**Example**

.. csv-table:: 
  :width: 30
  :widths: 10,10,10
  :header-rows: 1
  :file: tables/widget-integer.csv 

decimal
-------

Number question with a decimal point.  Decimal questions are limited to 14 digits plus the decimal point.  You can use
a text question with the **numbers** appearance if you need more.

**Type**

*  decimal

**Appearances:**

*  thousands-sep:  Inserts a separator between thousands 

**Availability:**

*  FieldTask: yes
*  Webforms:  yes

**Example**

.. csv-table:: 
  :width: 30
  :widths: 10,10,10
  :header-rows: 1
  :file: tables/widget-decimal.csv 

bearing
-------

A bearing widget captures the compass reading and stores it as a decimal type.

**Type**

*  decimal

**Required Appearance:**

*  bearing  

**Availability:**

*  FieldTask: yes
*  Webforms:  no

**Example**

.. csv-table:: 
  :width: 30
  :widths: 10,10,10,10
  :header-rows: 1
  :file: tables/widget-bearing.csv 

.. figure::  _images/widget-bearing.jpg
   :align: center
   :width: 300px

   Bearing

Other ODK Question types
------------------------

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
 
**Type**

*  chart

Shows a chart in the survey. Settings for the graph are specified in the question parameters. More details are available in :ref:`charts`

**Availability:**

*  FieldTask: yes
*  Webforms:  no
 
Child Form / Parent Form
------------------------

**Type**

*  child_form
*  parent_form

Launches another survey from within the current survey. The difference between these is in how the data from the two surveys
are linked in the results database.  If you don't care about linking the data between the two surveys then either type will do.
Detailed information on using these question types is available in :ref:`launch-survey`.

**Availability:**

*  FieldTask: yes
*  Webforms:  no

Matrix
------

The **begin matrix** type is a convenient way to show questions in a matrix structure using webforms.

.. figure::  _images/widget-matrix.jpg
   :align: center
   :width: 500px

   Matrix Widget


To create the matrix, group the questions that will appear horizontally, however instead of using **begin group/end group** use **begin matrix/end matrix**. 
Because these questions are appearing horizontally there will be a limit to how many you can fit on the screen comfortably.

Then specify the rows of the matrix in a choice list in the choices worksheet.  Put the name of the choice list used by the matrix in the
"list name" column of the survey worsheet.  As these choices create the rows of the matrix you can add as many as you like and the matrix will 
simply extend down the page.

Finally in the settings sheet, under "style" add "theme-grid".

When you load the survey onto the server additional questions will be created in groups.  One group for each of the choices and a group for
the header.  Hence the matrix type is not a real type as it is converted into multiple other questions on upload.

**Type**

*  begin matrix
*  end matrix

**Example**

.. csv-table:: Survey Sheet: 
  :width: 40
  :widths: 10,10,10,10
  :header-rows: 1
  :file: tables/widget-matrix-s.csv 

.. csv-table:: Choices Sheet: 
  :width: 30
  :widths: 10,10,10
  :header-rows: 1
  :file: tables/widget-matrix-c.csv 

`Example Form <https://docs.google.com/spreadsheets/d/15chqbL61l-ywdd0nOhjNspxi6j0laaIqT7pHzCRodoE/edit?usp=sharing>`_

**Availability:**

*  FieldTask: yes
*  Webforms:  no
*  XLSForm: yes
*  Online Editor: no

