Regular Expressions
===================

.. contents::
 :local:
 
Using
-----

Regular expressions can be added as constraints to text questions.   They allow you to specify that the
answer must fit a specific pattern such as an email address or a phone number. For example::

  regex(. , '^[a-zA-Z]*$')

The first parameter of the above regex function is a 'dot'.  This refers to the current question.  So assuming you have 
added the above as a constraint on a text question then it will ensure that the answer only includes upper and lowecase 
english type alphabetic characters.
  
More Examples
-------------

::

  regex(. , '^[0-9]*$')                                               -- Numbers Only
  regex(. , '^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})*$')    -- An email address

Refer to `this website <https://gist.github.com/nerdsrescueme/1237767>`_ for more examples of regular expressions. 

.. note::

  When using examples from the above link do not include the slashes ('/') at the beging and end or the regular expression.

