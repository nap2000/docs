Create a Data PDF using a Template
==================================

Create and style the PDF template in a PDF editor then use **Prepare Form** to add the form fields that will be populate
by data from the submitted record.

*  Use a text field for text, integer, barcode, select questions.
*  Use an image field for location questions such as geopoint, geotrace, geoshape and start-geopoint
*  Use an image field for image questions
*  Set the name of the field to the name of the question

Where questions are inside a repeating group you need to identify which iteration of the repeat you want to show.  The field name
should be set to  repeat_name[i].question_name where i is repeat record you want to show.  For example::

  members[0].name  
  Will be filled with the name from the first entry in the members sub form.



