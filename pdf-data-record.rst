PDF Data Record
===============

.. contents::
 :local:
 
A PDF can be generated containing the data in a submission.  The style of the PDF can be controlled by using appearance settings in the 
survey or a PDF template can be used where the data from the survey is inserted into fields in the template.

Create a Data PDF using a Template
----------------------------------

Create and style the PDF template in a PDF editor then use **Prepare Form** to add the form fields that will be populate
by data from the submitted record.

Specify PDF form fields as placeholders to be replaced by data from the survey.  Each form field should be given 
the name of the question that contains the data to be inserted at that location.

*  Use a text field for text, integer, barcode, select questions.
*  Use a **pushbutton** field for location questions such as geopoint, geotrace, geoshape and start-geopoint
*  Use a **pushbutton** field for image questions
*  Use a **pushbutton** field for compound location questions
*  Set the name of the field to the name of the question

Attaching a PDF template to a survey
++++++++++++++++++++++++++++++++++++

This is done in the online editor.  Select the menu tools and then **PDF Templates**.  You can then add one or
more templates for use with the survey.

For each survey you can specify:

*  A rule which will determine if the pdf is selected automatically when sent after a notification.  These rules follow the format for :ref:`server-expressions`.
*  A default checkbox.  To make that PDF template the default.
*  A "Not Available" checkbox which will remove the template from the list of selectable templates.

The PDF template that will be used for a notification or set as the default selected template is found using the following process:

#.  The template whose rule matches data in the submitted record
#.  The template set as the default template on the templates page for the survey
#.  A legacy template previously loaded in the setting dialog of the online editor for the survey

If no template is found then a PDF will be generated withut a template.

Repeating Data
+++++++++++++++

Where questions are inside a repeating group you need to identify which iteration of the repeat you want to show.  The field name
should be set to  repeat_name[i].question_name where i is repeat record you want to show (starting from 0).  For example::

  members[0].name  
  Will be filled with the name from the first entry in the members sub form.
  
Special Question Names
++++++++++++++++++++++

*  _hrk:  The generated unique key for the record
*  prikey:  The primary key of the record
*  user: The user who submitted the record
*  _start:  The start time of the survey
*  _end:  The end time of the survey
*  _device:  The device identifier that submitted the record
*  instancename: The generated instance name

Generate PDF Data Record
------------------------

Style the PDF using appearance options set in the survey.  The online editor offers good support for this.  In the appearance
editing dialog there is a tab for PDF settings.  Alterntively you can set appearance values by referring to :ref:`pdf-appearances-reference`

Logo
++++

A logo will be shown at the top of the first page.  The default logo can be set in the survey settings.  If not set then the banner logo for
webforms will be used.  The image selected as the default logo will be scaled to fit 200 pixels long by 50 pixels high.

Showing start-geopoint
----------------------

start-geopoint is a meta item that will automatically record the location of the first question asked in a survey.  In a PDF this is
shown on a map as a **green** pin containing the image of an anchor.  

If there is another geometry in the same form then the start-geopoint will be shown on the same map as the other geometry.  The following
image shows this with the location of a geopoint shown using the (default) red pin near to the location recorded by start-geopoint in green.  

.. figure::  _images/pdf1.jpg
   :align:   center
   :alt: Location of start-geopoint in PDF
   
   Location of start-geopoint in PDF

Special Compound Question Views
-------------------------------

Multiple geopoint questions can be combined onto a map or an abstract image in a pdf.  These compound views are quite specialised and used for
cable or pipe maintenance.  The two views are:

*  :ref:`compound-map-widget`
*  :ref:`compound-image-widget`

Styling a PDF using appearance settings
---------------------------------------


Use :ref:`pdf-appearances-reference` to style the generated PDF.  These appearance settings are mainly used to add styling to a PDF that is generated without
a template however some also apply to pdf templates.
