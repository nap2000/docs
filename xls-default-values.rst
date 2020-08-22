Default Values
==============

.. contents::
 :local:

Static Values
-------------

A static default is set when the the form is first opened.  

.. note::

  To add a staric default; place the default value in the default column without using quotation marks.

.. csv-table:: Static Default:
  :width: 240
  :widths: 80,40,80,40
  :header-rows: 1
  :file: tables/static_default.csv
  
In the above example the default value for the select one question is set to legumes.  

Special Static Defaults
+++++++++++++++++++++++

You can use one of these special values in the default column.

.. csv-table:: Special Static Default Values:
  :width: 100
  :widths: 50,50
  :header-rows: 1
  :file: tables/special_static_default.csv

Referring to Preloads
+++++++++++++++++++++

Because a static default value is set when the form is first opened there is no point referring to the answers to other question in order
to set the default value.  For that you will need to use a dynamic default.  However you can refer to a preload.  So for example you
may specify a preload to get the users name and you can then use that preload value in a static default.

.. csv-table:: Using Preloads in Static Defaults:
  :width: 240
  :widths: 80,40, 80, 40
  :header-rows: 1
  :file: tables/preload_static_default.csv


Referring to the last saved value
+++++++++++++++++++++++++++++++++

If you are conducting multiple interviews where you have to enter the same answers each time then you can
default the answer to the one given in the previous interview.  The obvious use for this is for addresses. For example if you are interviewing
20 people in a town then the town name will be the same for each person. 

Specify the following in the default column::

  ${last-saved#question_name}

Replace "question_name" with the name of the previously answered question that you want to get the default value from.

.. csv-table:: Example of Last Saved
  :width: 240
  :widths: 80,40, 40, 80
  :header-rows: 1
  :file: tables/last_saved_default.csv

.. warning::

  Requires fieldTask 6.100 or above and Smap Server 20.04 or above

Dynamic Defaults
----------------

A dynamic default value is specified in the **calculation** column for a question.  Hence you can set the initial answer to a question
based on the answer to a preceeding question.
  
.. warning::

  Calculations in FieldTask are updated every time their source changes and also just before the survey is saved. This can cause lots of issues when using them
  to set default values.  For example if you had a dynamic default calculation of ${number_girls} to set the default value for a question on how many girls go 
  to school then the answer (to how many girls go to school) will be reset back to the default value when the form is saved.  

To avoid the problem of recalculation of defaults when the form is saved  wrap the calculation in the either the once() function or in
fieldTask version 6.209 and above you can use the default() function::  

  once(${number_girls}) 
  default(${number_girls})

Now the default value is set when the question is shown. 

*  If you use the once function then after the answer has been set it will not be changed again using the default calculation.
*  If you use the default() function then if the conditions of the calculation change the value will be reset however it will not be
   changed when the form is saved.  

.. note::

  Webforms does not have the above issues with dynamic defaults and you **should not** wrap the default calculation in the once() function.
  
Dynamic Images
--------------

Images are a special case because you can dynamically specify an image URL as the default value of a question.  If the Android device or
WebForm is online this image will then be downloaded.  One application of this might be if you had an image question with an appearance of
**annotate**.  The image URL can be selected from a list of drawing schematics, the selected image would then be downloaded and the user would be
able to annotate the selected schematic.

Use a get_media() function to download the required URL. There are some differences between the way WebForms and FieldTask work.  

WebForms
++++++++

For webforms the get_media() function takes 2 parameters.  The first is the URL to retrieve and the second one is the path to the
question that should receive the URL.  This is different from the every other use of dynamic defaults in that the calculation
places in the result in the specified question.  Hence you don't need to have anything in the calculation column of the target
question::

  get_media(${q1}, '/main/q3')
 
.. note::

  For the second parameter you cannot use the ${} notation. Paths to questions always start with '/main' and then
  continue with the names of groups and questions each separated by a '/'

`Example survey for Dynamic Images (WebForm version) <https://docs.google.com/spreadsheets/d/1MCi1DcIC0kh4H4Hyq33RJWt3mlWAdPOnG2YQRYgtzWg/edit?usp=sharing>`_

FieldTask
+++++++++

Only one parameter is required for get_media() which is the URL of the image.  Then the calculation question is specified in the 
calculation column of the target question::

  calculate  q2   if(string-length(${q1}) > 0, get_media(${q1}, '/main/q3'), '')
  image      q3   once(${q2})
  
Remember the dynamic default value is wrapped in a once() function so that it only gets set once.

`Example survey for Dynamic Images (FieldTask Version) <https://docs.google.com/spreadsheets/d/1WEoARXBgcmbRzgvrDK7lyCsjiU7AhCWq4dondDkY5Pw/edit?usp=sharing>`_

Security Considerations
+++++++++++++++++++++++

Security controls on the server holding the images may prevent their access within a form.  So unless they are on a 
completely open server you will need to consider access permissions and CORS settings. 

Alternatively if you are accessing images collected by other surveys on the same Smap server then you can use the Smap security 
controls (projects, RBAC) to control access. 
