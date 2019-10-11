Survey References
=================

.. contents::
 :local:

.. _question-names:

Question Names
--------------

Question and choice names should have

*  no spaces (use "_" to separate words)
*  use letters only from the english alphabet
*  can include numbers
*  can include some punctuation including . - _
*  first character must be a letter, not a number
*  must be shorter than 64 characters

Names that are ok:

*  householder_name
*  Q1.2

Names that are not ok:

*  1_house  (Starts with a number)
*  householder name   (Contains a space)

Question Types
--------------

Smap supports all the ODK question types as well as additional types specific to Smap.

ODK Question types
++++++++++++++++++

*  `text <http://docs.opendatakit.org/form-question-types/#default-text-widget>`_
*  `integer <https://docs.opendatakit.org/form-question-types/#integer-widget>`_
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
+++++

Type:  chart

Shows a chart in the survey. Settings for the graph are specified in the question parameters.

Not available in Webforms.
 
Child Form / Parent Form
+++++++++++++++++++++++++

Type:  child_form / parent_form

Launches another survey from within the current survey. The difference between these is in how the data from the two surveys
are linked in the results database.  If you don't care about this linkage then either will do.

.. _meta_items:

Meta Items
----------

Data for meta items is collected automatically without asking the user.  Hence no label is required and you 
only need to specify the type and a unique name.  

.. note::

  Smap automatically adds the start time, end time and device id 
  to every new survey as this information is important for quality assurance of the data. Hence
  you will not need to specify these meta item	
  
.. csv-table:: Meta Items:
  :width: 50
  :widths: 10,40
  :header-rows: 1
  :file: tables/meta.csv


.. _expression-reference:

Expressions
-----------

Relevance, constraints and calculates all compute a new value using answers from other questions. 

Syntax
+++++++

.. csv-table:: Syntax:
  :width: 70
  :widths: 10,10, 10, 40
  :header-rows: 1
  :file: tables/syntax.csv

Date Functions
++++++++++++++

.. csv-table:: Date Functions:
  :width: 80
  :widths: 20,20,40
  :header-rows: 1
  :file: tables/datefns.csv

Date Formats
^^^^^^^^^^^^

1.	%Y    :   4 digit year
2.	%y    :   2 digit year
3.	%m   :   numeric month padded with 0
4.	%n    :   numeric month
5.	%b    :   short text month (English)
6.	%d    :   day of month
7.	%H   :   hour, 24 hour clock padded with 0
8.	%h    :   hour, 24 hour clock
9.	%M  :   minute padded with 0
10.	%S    :   second padded with 0
11.	%3    :   milliseconds padded with 0
12.	%a    :   short text day (English)   

Text Functions
++++++++++++++


.. csv-table:: Text Functions:
  :width: 80
  :widths: 20,20,40
  :header-rows: 1
  :file: tables/textfns.csv
  
Mathematical
++++++++++++

Referring to data inside repeats, also called sub-forms, can be quite complex as you often need to identify which iteration of the 
sub form you are referring to.  These functions can assist.

.. csv-table:: Math Functions:
  :width: 80
  :widths: 20,20,40
  :header-rows: 1
  :file: tables/mathfns.csv
  
Repeats
+++++++

Referring to data inside repeats, also called sub-forms, can be quite complex as you often need to identify which iteration of the 
sub form you are referring to.  These functions can assist.

.. csv-table:: Repeat Functions:
  :width: 80
  :widths: 20,20,40
  :header-rows: 1
  :file: tables/repeatfns.csv

Other
+++++

.. csv-table:: Other Functions:
  :width: 80
  :widths: 20,20,40
  :header-rows: 1
  :file: tables/otherfns.csv

.. _settings-reference:

Survey Settings
---------------

The following settings can be specified in the settings worksheet of the XLS editor.  When using the online
editor they are specified in either the Setting Dialog or Keys Dialog.  
  
.. csv-table:: Settings:
  :width: 70
  :widths: 10,40, 20
  :header-rows: 1
  :file: tables/settings.csv








