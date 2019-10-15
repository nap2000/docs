Constraint
==========

.. contents::
 :local:  

About Constraints:

*  Constraints are used to prevent the enumerator continuing if an invalid answer has been entered
*  Constraints are checked after the enumerator has finished answering a question and as they are moving onto the next question
*  A constraint always needs in some way to refer to the answer of the current question as its checking if that answer is valid
*  You refer to the answer of the current question using a "." (a dot)
*  This behaviour differs from **relevance** where rules are checked before a question is asked. Hence a relevance should never refer 
   to the value of its own question


.. figure::  _images/constraint1.jpg
   :align:   center
   :alt: Constraint on age which must be less than 15

   The age must be less than 15

.. note::

  In the constraint you specify what the answer must be. Hence in the preceeding example an error message wiil be shown if the age is greater
  than or equal to 15.

Constraint Message
------------------

If a constraint is violated the default error message is not vey helpful::

  Sorry, this response is invalid
  
The message will also be in the language of the phone and not necessarily the language of the survey.  You can provide an
alternative message in the **constraint_message** column.

.. figure::  _images/constraint2.jpg
   :align:   center
   :alt: Constraint Message

   Constraint Message
   
Making the Question Required
----------------------------

Probably the most important constraint that you can add is to specify that they question must be answered

*  It is quite easy when swiping between questions to go past a question without answering it, unless the question is **required**
*  If you don't answer questions then whole blocks of other questions might not show up due to the relevance not being satisfied

To make a question required::

  Add "yes" to the re"quired" column
  Optionally add your own message in the "required_message" column
  
.. figure::  _images/constraint3.jpg
   :align:   center
   :alt: Required

   Required
   
Complex constraints on multiple Questions
-----------------------------------------

Its good to validate a question when the user answers it but sometimes you may want to take into account later questions.

You can add a constraint that forces the user to go back and fix up earlier questions, to do this create a

*  read only question of type “note”
*  make it mandatory!!!  The user will not be able to get past it.
*  make the question **relevant** only if there is a problem with answers to previous questions
*  in the label specify instructions to the data collector on how to resolve the issue

Refer to the example survey “constraint trick question.xls”




  
