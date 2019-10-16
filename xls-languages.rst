Languages
=========

Surveys can contain translations into multiple languages.  You will need to create a separate “label” and “hint” 
column in the survey worksheet for each language.  

You will also need a separate “label” column for each language in the choices worksheet.

Single Languages
----------------

.. figure::  _images/languages0.jpg
   :align:   center
   :width:   500px
   :alt:     Single Language
   
   Single Language

You can write the labels for a survey in any language that is supported by your devices and your laptop. It is not necessary
to identify the language if there is only one.  In the diagram above the survey has been typed in Esperanto.  The principle 
columns where you will enter language specific text are the:

*  label column in the survey sheet
*  hint column in the survey sheet
*  label column in the choices sheet

Identifying the Language
------------------------

You can label the language by adding its name to the column heading (label / hint) with a \:\: separator. In the following
diagram the language has been labelled as being esperanto.  

.. figure::  _images/languages1.jpg
   :align:   center
   :width:   500px
   :alt:     Labelled
   
   Labelled Language
   
This is not really useful.  The only point of labelling a language is so that the data collector can choose the language
that they want to use.  This is only necessary if there is more than one.  In the xls template the default language is specified 
as "language".  There is no need to change this name unless you are going to have more than one language.

Multiple Languages
------------------

.. figure::  _images/languages2.jpg
   :align:   center
   :width:   500px
   :alt:     Multiple Languages
   
   Multiple Language

Now there are two languages each with their own label.

You can give the language any name you like. For example oldlatin. 
As long as there are no spaces and you are consistent for all three columns.

Right to Left Languages
-----------------------

If you include **(rtl)** in the language name then it will be set right to left automatically::

  label::language(rtl)
  
Also if you include the following language codes the direction will be set Right to Left::

  label::arabic
  label::lanugage(ar)
  label::language(he)
  label::language(ur)
  
To force the direction as Left to Right even when the language is arabic then include (ltr) in the language name::

  label::language(ltr)
  



