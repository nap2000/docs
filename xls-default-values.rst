Default Values
==============

.. contents::
 :local:

Static Values
-------------

A static default is set when the the form is first opened.  

.. note::

  To add a static default; place the default value in the default column without using quotation marks.

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

  Available in FieldTask.  Available in WebForms in versions 25.08+

Dynamic Defaults
----------------

A dynamic default value is specified in the **calculation** column for a question.  Hence you can set the initial answer to a question
based on the answer to a preceding question.
  
.. warning::

  Calculations in FieldTask are updated every time their source changes and also just before the survey is saved. This can cause lots of issues when using them
  to set default values.  For example if you had a dynamic default calculation of ${number_girls} to set the default value for a question on how many girls go 
  to school then the answer (to how many girls go to school) will be reset back to the default value when the form is saved.  

To avoid the problem of recalculation of defaults when the form is saved  wrap the calculation in the either the once() function or in fieldTask version 6.209 and above you can use the default() function::  

  once(${number_girls}) 
  default(${number_girls})

Now the default value is set when the question is shown. 

*  If you use the once function then after the answer has been set it will not be changed again using the default calculation.
*  If you use the default() function then if the dependencies of the calculation change the value will be reset however it will not be
   changed either when the form is saved or when the form is initialised. This latter condition is important if you are restoring from a 
   saved survey or starting a task. 

.. note::

  WebForms does not have the above issues with dynamic defaults and you **should not** wrap the default calculation in the once() function. However
  you can use the default() function as this will just be ignored.
  
You can also use :ref:`trigger-calculation` to get the same result as you can set the trigger to be the referenced
question from which you are getting the default.  The calculation will then only be updated when that value changes.

Dynamic Defaults in Repeats
---------------------------

You can use a entered in a previous repeat instance to calculate the default in the next repeat instance.
Requires version 23.11 of the Smap Server.  An "xpath" expression ise specified as the default value for
a question inside a repeat.  You can modify the following example to get what you need.

For example in the following survey the value of observation_id will default to "1" for the first instance and
then increment by 1, for each additional repeat instance.

.. csv-table:: Survey Worksheet
  :header: type, name, label, default

  begin repeat, observations, Observations,
  int, observation_id, ID , "if(position(..)=1,1,(${observations}[position() = position(current()/..) - 1]/observation_id)+1)"
  end repeat

*  "${observations}" refers to the name of the repeat.
*  "position(current()/..) - 1" refers to a value in the previous repeat instance
*  "/observation_id" refers to the value in the observation_id question
*  "+ 1"  adds one to that value


Dynamic Images
--------------

You can dynamically specify an image URL as the default value of a question.  If the Android device or
WebForm is online this image will then be downloaded.  One application of this might be if you had an image question with an appearance of
**annotate**.  The image URL can be selected from a list of drawing schematics, the selected image would then be downloaded and the user would be
able to annotate the selected schematic.

Use a get_image() function to download the required URL. 
Only one parameter is required for get_image() which is the URL of the image.  Then the calculation question is specified in the 
calculation column of the target question::

  image  imageQuestion   default(if(string-length(${q1}) > 0, get_image(${q1}), ''))
  
The dynamic default value should be wrapped in a default() or once() function so that it does not get changed when the form is saved. default()
is usually better as it would allow the url of the image to be re-calculated and a new image applied whereas if once() is used then once the image
is set it cannot be changed without manually clearing the answer.

`Example survey for Dynamic Images <https://docs.google.com/spreadsheets/d/1n1QQ5zzMT18T1UsoNLMFWu1LxZJcD0X8O1gNe_x3DcI/edit?usp=sharing>`_

Security Considerations
+++++++++++++++++++++++

Security controls on the server holding the images may prevent their access within a form.  So unless they are on a 
completely open server you will need to consider access permissions and CORS settings. 

Alternatively if you are accessing images collected by other surveys on the same Smap server then you can use the Smap security controls (projects, RBAC) to control access. 
