Question Types
==============

.. contents::
 :depth: 2
 :local:  
 
text
----

Use for questions that require a text response.  It can also be used with the numbers appearance to get integer responses that are longer
than the 9 character limit of the **integer** type.

**Type**
  text

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

.. csv-table:: Survey Worksheet
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
  integer

**Appearances:**

*  thousands-sep:  Inserts a separator between thousands 
*  hidden:  Hide the widget in fieldTask

**Availability:**

*  FieldTask: yes
*  Webforms:  yes

**Example**

.. csv-table:: Survey Worksheet
  :width: 30
  :widths: 10,10,10
  :header-rows: 1
  :file: tables/widget-integer.csv 

decimal
-------

Number question with a decimal point.  Decimal questions are limited to 14 digits plus the decimal point.  You can use
a text question with the **numbers** appearance if you need more.

**Type**
  decimal

**Appearances:**

*  thousands-sep:  Inserts a separator between thousands 

**Availability:**

*  FieldTask: yes
*  Webforms:  yes

**Example**

.. csv-table:: Survey Worksheet
  :width: 30
  :widths: 10,10,10
  :header-rows: 1
  :file: tables/widget-decimal.csv 

bearing
-------

A bearing widget captures the compass reading and stores it as a decimal type.

**Type**
  decimal

**Required Appearance:**

*  bearing  

**Availability:**

*  FieldTask: yes
*  Webforms:  no

**Example**

.. csv-table:: Survey Worksheet
  :width: 40
  :widths: 10,10,10,10
  :header-rows: 1
  :file: tables/widget-bearing.csv 

.. figure::  _images/widget-bearing.jpg
   :align: center
   :width: 300px

   Bearing

date, time and datetime
------------------------

Default date type
+++++++++++++++++

**Type**
  date
**Availability:**
  FieldTask: yes
  Webforms:  yes

**Example**

.. csv-table:: Survey Worksheet
  :header: type, name, label

  date,birthdate,When were you born?

.. figure::  _images/widget-date.jpg
   :align: center
   :width: 300px

   Default Date type

Date widget with spinner input
++++++++++++++++++++++++++++++

A more compact date widget that makes it easy to select dates that are far from the current (or default) date.

**Type**
  date

**Appearance:**
  no-calendar

.. csv-table:: Survey Worksheet
  :header: type, name, label, appearance

  date,birthdate,When were you born?,no-calendar

.. figure::  _images/widget-date-spinner.jpg
   :align: center
   :width: 300px

   Default Date type

Month and year only
+++++++++++++++++++

Only records the month and the year.

**Type**
  date

**Appearance:**
  month-year

.. csv-table:: Survey Worksheet
  :header: type, name, label, appearance

  date,birth_month,What month were you born?,month-year

Year only
+++++++++

Only records the year.

**Type**
  date

**Appearance:**
  year

.. csv-table:: Survey Worksheet
  :header: type, name, label, appearance

  date,birth_year,What year were you born?,year


Date widgets with non-Gregorian calendars
+++++++++++++++++++++++++++++++++++++++++

.. contents::
  :local:

.. note::

  The non-Gregorian calendar is used only on input.
  The dates are then converted and stored as standard Gregorian dates


**Availability:**

*  FieldTask: yes
*  Webforms:  no

Bikram Sambat calendar
^^^^^^^^^^^^^^^^^^^^^^

**Type**
  date

**Appearance:**
  bikram-sambat

.. figure::  _images/widget-date-bikram.jpg
   :align: center
   :width: 300px

Coptic calendar
^^^^^^^^^^^^^^^

**Type**
  date

**Appearance:**
  coptic

.. figure::  _images/widget-date-coptic.jpg
   :align: center
   :width: 300px

Ethiopian calendar
^^^^^^^^^^^^^^^^^^

**Type**
  date

**Appearance:**
  ethiopian

.. figure::  _images/widget-date-ethiopian.jpg
   :align: center
   :width: 300px

Islamic calendar
^^^^^^^^^^^^^^^^

**Type**
  date

**Appearance:**
  islamic

.. figure::  _images/widget-date-islamic.jpg
   :align: center
   :width: 300px

Myanmar calendar
^^^^^^^^^^^^^^^^

**Type**
  date

**Appearance:**
  myanmar

.. figure::  _images/widget-date-myanmar.jpg
   :align: center
   :width: 300px

Persian calendar
^^^^^^^^^^^^^^^^

**Type**
  date

**Appearance:**
  persian

.. figure::  _images/widget-date-persian.jpg
   :align: center
   :width: 300px

Time widget
+++++++++++

Records the time of day.

.. note::

  The time is stored along with the time zone.  Hence a point in time is recorded.  If you record a time of
  10:00 am in London then the value is the same as 8pm in Sydney.  If someone in Sydney generates a report 
  using their local timezone then they will see the result as 8pm.

  If you want to record a local time then you can use an **integer** type or **decimal** type or a **select_one** type that has
  a list of valid times. A question like "What time did the parcel arrive?" could be recorded with or without timezone depending
  on how you want to analyse the data.

**Type**
  time

.. csv-table:: Survey Worksheet
  :header: type, name, label

  time, arrived, What time did the parcel arrive?

Datetime widget
+++++++++++++++

Records the date and time

**Type**
  dateTime

**Appearance:**
  no-calendar

.. csv-table:: Survey Worksheet
  :header: type, name, label

  dateTime, started, When did you start the project?

Image 
-----

.. contents::
 :local:

Default image widget
++++++++++++++++++++

**Type**
  image

Captures an image either using the camera or by selecting from the device gallery.

.. csv-table:: Survey Worksheet
  :header: type, name, label

  image,picture_of_tree,Take a picture of the tree

Image with annotation
+++++++++++++++++++++

Draw on an image after it has been captured. An additional button labelled "Markup Image" is shown that is
enabled after the image is captured.

**Type**
  image

**Appearance:**
  annotate

.. csv-table:: Survey Worksheet
  :header: type, name, label

  image,damage,Take a photo and circle the damage

.. figure::  _images/widget-image-annotate.jpg
   :align: center
   :width: 300px
   :alt: An image after the user has annotated it by circling an item of interest

   Annotate Type

Image as a drawing 
++++++++++++++++++

**Type**
  image

**Appearance:**
  draw

This is similar to annotate except the user draws on a blank canvas.

.. csv-table:: Survey Worksheet
  :header: type, name, label, appearance

  image,draw_farm_layout,Draw a plan of the farm

Image as a signature
++++++++++++++++++++

**Type**
  image

**Appearance:**
  signature

Allows the user to draw a signature of their name.

.. csv-table:: table
  :header: type, name, label, appearance

  image,hh_signature,Ask houeholder to sign the screen,signature

Other Image appearances and parameters
++++++++++++++++++++++++++++++++++++++

Require a new image
^^^^^^^^^^^^^^^^^^^

The default behavour is to include a button that allows the user to select an existing image rather than taking a new one.
However by adding the appearance "new" the user is requried to capture a new image.

Self portrait (*selfie*) image 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The back camera on the phone is used by default (although the user can change this).  However by setting the appearance "new-front"
the front camera is used by default to capture a selfie.

.. note::

  **selfie** can also be used as the appearance.

Reducing the size of images
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The size can be reduced by specifying the maximum length of the longest side of the image using **max-pixels**. For example if the 
default picture size is 1,000 by 500 and you specify the max-pixels to be 200, then the image will be resized to 200 by 100 pixels.  

In the parameters column add ``max-pixels=`` followed by the maximum length of the long edge in pixels.

..  note::

  The proportions of the image are maintained and if the length of the longest side was less than max-pixels the image will not be changed.

Acknowledge / Trigger
---------------------

type
  trigger or acknowledge

You can use a type of either **trigger** or **acknowlwdge**, they work the same way.  A single checkbox
is shwown which the user can "acknowledge" by checking it.  If they do this then the answer stored for
the question is "OK".

You can use the above answer in relevance for following questions. For example::

  ${ack} = 'OK'

Commonly select_one questions with yes/no choices are used instead of Acknowledge

.. csv-table:: survey
  :header: type, name, label, relevance

  acknowledge,ack,Select to confirm participation
  text, name, What is your name?, ${ack} = 'OK'

.. figure::  _images/widget-ack.jpg
   :align: center
   :width: 300px
   :alt: The trigger widget shown in fieldTask after the checkbox has been selected

   Acknowledge widget in fieldTask

In WebForms a radio button is used instead of a checkbox.

.. figure::  _images/widget-ack-webform.jpg
   :align: center
   :alt: The trigger widget shown in WebForms after the checkbox has been selected

   Acknowledge widget in WebForms

 
Chart
-----
 
**Type**
  chart

Shows a chart in the survey. Settings for the graph are specified in the question parameters. More details are available in :ref:`charts`

**Availability:**

*  FieldTask: yes
*  Webforms:  no
 
Child Form / Parent Form
------------------------

**Type**
  child_form,
  parent_form

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
  begin matrix,
  end matrix

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

*  FieldTask: no
*  Webforms:  yes
*  XLSForm: yes
*  Online Editor: no

Other ODK Question types
------------------------

*  `select and select_one <https://docs.opendatakit.org/form-question-types/#select-widgets>`_
*  `rank <https://docs.opendatakit.org/form-question-types/#rank-widget>`_
*  `geopoint, geotrace and geoshape <https://docs.opendatakit.org/form-question-types/#location-widgets>`_
*  `audio <https://docs.opendatakit.org/form-question-types/#audio-widget>`_
*  `video <https://docs.opendatakit.org/form-question-types/#video-widgets>`_
*  `file upload <https://docs.opendatakit.org/form-question-types/#file-upload-widget>`_
*  `barcode <https://docs.opendatakit.org/form-question-types/#barcode-widget>`_
*  `range <https://docs.opendatakit.org/form-question-types/#range-widgets>`_
*  `note <https://docs.opendatakit.org/form-question-types/#note-widget>`_
 
