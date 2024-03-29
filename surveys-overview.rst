Surveys Overview
================

.. contents::
 :local:
 
Tools
-----

1.  Excel Editor
2.  Online Editor

The excel editor is most suited to larger complex surveys.  It also allows editing without an internet connection.

The online editor is quicker and simpler than the excel editor but harder to use for large complex surveys.  It also can be
unreliable when moving questions within the survey, particularly if this is to and from groups.  If you enclounter any problems
when moving questions export the survey to excel, do the move there and then load the excel survey back onto the server.  
  

Survey Size
-----------
Surveys can be as small as 1 question.  There is no specified maxiumum size,  one customer completed a survey that had over 4,500 questions.
However surveys used for evaluations commonly have around 300 questions.  Surveys used for monitoring would usually be shorter.

Although there is no limit to the size of surveys we can only store the answers for 1,600 questions in a form.  So if you have more
questions you will need to put them into multiple forms.  This can be done so that the data collector and analyst are 
unaware that the survey has been split up.

1. Put around 1,500 questions in the main form (Leaving a bit of room for expansion later)
2. Then specify a subform using the "begin repeat" question type and with a repeat_count of "1"
3. Put the next 1,500 questions in this subform
4. Repeat until all questions have been added

To allow all the data to be exported together each new subform should be create in it's parent subform as shown below:

-- Main Form
   -- Subform 1
      -- Subform 2


XML Surveys
-----------   
However you can also load surveys in an XML XForm format.  These can contain sophisticated functionality that is not supported by
the above two editors.  If you have a survey in XML format then you can load it onto the server in the same way you would load a
Survey created with Excel.  `Creating a survey in XML <https://opendatakit.github.io/xforms-spec>`_

.. note::

  We use the terms "Survey" and "Form" interchangeably.  However more precisely there can be multiple forms in a survey. 
  These consist of a main form where you start answering questions and zero or more repeating sub forms. For example the main
  form may ask questions about a household while a sub-form asks questions to be answered for each member of the household.

