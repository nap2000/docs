Default Values
==============

.. contents::
 :local:

Dynamic Values
--------------

A dynamic default value is specified in the **calculation** column for a question.  Hence you can set the initial answer to a question
based on the answer to a preceeding question.
  
.. warning::

  For fieldTask dynamic default values have to be wrapped in the once() function as otherwise they will be recalculated when the
  user saves the form and any changes the user has made will be lost.

  For example:  once(${q2})
  
Dynamic Images
--------------

Images are a special case because you can dynamically specify an image URL as the default value of a question.  If the Android device or
WebForm is online this image will then be downloaded.  One application of this might be if you had a image question with an appearance of
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