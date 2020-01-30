.. _survey-ident:

Survey Identifier
=================

Every survey has a unique identifier that starts with the letter s and then some numbers an underscore and some more numbers.  For example::

  s44_867

This identifier can be used to look up data in that survey such as by using the **search** function to get a list of choices for a survey using 
data from another survey.  The survey identifier does not change if a survey is edited using the online editor or replaced by another XLSForm survey.

To get the identifier for a survey open the survey in the online editor and select the menu **File** and then **Info**.  The survey identifier will
be one of the values shown in a dialog.

.. figure::  _images/survey_ident1.jpg
   :align:   center
   :width:   300px
   :alt:     Survey Information

   Survey Information

.. note::

  The special identifier **self** can also be used wherever the survey identifier is used.  **self** refers to the current survey.  This is useful for looking up
  data that has previously been collected by the survey that you are using.
