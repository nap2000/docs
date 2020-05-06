.. _server-expressions:

Server Expressions
==================

.. contents::
 :local:

Introduction
------------

It is often useful to write expressions that manipulate data on the server.  These can be used to filter data for reports
or in server calculations that create new, derived values, from the data already in a submission.

Referring to Questions
----------------------

Use the same approach that is used for referring to questions in a relevance. That is surround
the question name with curly brackets and put a dollar sign in front.

Questions can be in any form. For example you may have a survey that gathers information on
companies and the projects that they are involved in. Hence the data on projects could be in a sub-form.
The following filter will trigger on a
company name of "Widgets" that has at least one project with a value over 100,000::

   ${company_name} = 'Widgets' and ${project_value} > 100000

It is currently not possible to aggregate data from sub-forms.

Supported Question Types
------------------------

* text
* integer
* decimal
* select_one
* barcode
* calculation
* date
* datetime
* acknowldege

Question types with minimal support
-----------------------------------

These question types can be used only to check to see if they were answered. 

* image
* audio
* video
* geopoint
* polygon
* line

For example::

  ${video_question} empty
  This will find any records where the video question was not answered.

Un-Supported Question Types
---------------------------

The following question types currently cannot be used to filter data

* select_multiple

Operators
---------

These are used for comparisons and to build up more complex expressions.  There must be a space each
both sides of these operators.

* = (equals)
* > (greater than)
* < (less than)
* >= (Greater than or equals)
* <= (Less than or equals)
* != (Not equals)
* not
* \- (minus)
* \+ (plus)
* \* (times)
* / (divide)
* and
* or
* like (Similar to.  Use the % symbol to match a range of characters.
  Use the _ underscore character to match a single character)
* not like (returns the rows that do not match)

Brackets
--------

Use smooth brackets for "association".  Like for operators these brackets must have spaces
around them.

* (
* )

Constants
---------

* integers written as is
* decimals written as is
* text values enclosed in single quotes
* date values enclosed in single quotes and in the following format yyyy-mm-dd.  Note
  that you need to enter two characters for months and days.

Example::

  2020-04-01

Single Quotes in Text
---------------------

You might want to search for the name of a person that contains a single quote in their name such as 'Akeola. In cases like this add an 
extra quote.  The system will then realise that '' means its a quote inside the text and not the end of the text. For example you may
specify an advanced filter as::

  ${first_name} like '%''Akeola%'


This feature is available with Smap Version 20.04

Date Formats
-------------

* 'yyyy-mm-dd'

Hence the thirty first of January, 2018 would be::  

  '2018-01-31'

Date Intervals
--------------

* {1_day}
* {n_days}
* {1_hour}
* {n_hours}
* {1_minute}
* {n_minutes}
* {1_second}
* {n_seconds}
* {hh:mm:ss}

Converting to a different type
------------------------------

Calculations are always stored on the server as 'text' type answers.  However the data inside them can be in many types
integer, decimal, text, date.  It depends on the calculation that was performed.  So you might have a calculate questions that
creates an integer value, for example a calcualtion of age.   If you then try to do a server calculation such as ${age} + 10 
this will fail because age is treated as text.  You can use the following **cast** functions to tell the system which type
you actually want to use

*  cast(${question} as integer)
*  cast(${question} as decimal) 

Examples::

  cast(${age} as integer) < 10
  cast(${age} as decimal) / 2

Other
-----

* now()  (The current date and time)

Special Terms
-------------

* is null (Test to see if an answer was <b>not</b> given to a media or geopoint question)
* is not null (Test to see if an answer was given to a media or geopoint question)
* ${_upload_time} (The date that the survey was uploaded to the server)
* ${_start} (The time the survey was started)
* ${_end} (The time the survey ended)
* ${_hrk} (The generated unique key for the record)
* ${_device} (The device identifier that submitted the results)
* ${_user} (The logon identifier of the user that submitted the results)
* ${prikey} (The unique record number of submitted data)
* ${_version} (The version number of the survey that was used to submit a record)

Note the ${_version} value is of type text, hence if you want to use this in a filter you may need to cast it.  For example::

  cast(${_version} as integer) > 3



Examples
--------

::

  ${person_name} = 'Tom'
  ${age} > 5
  ${age} > 25 or ${name} = 'tom'
  ${name} like 'sam%' 
    Matches "sam", "samuel", "sammy" etc

  ${city} like '_erlin'
    Matches "Berlin", "berlin"

  ${city} not like '%ich%'
    Matches anything that does not have "ich" in it 

Examples with brackets::

  ${age} > 25 or ( ${name} = 'tom' and ${age} > 5 )
  
Examples using constants::

  ${name} > 25
  ${weight} < 0.5
  ${name} = 'tom'
  ${date_question} = '2016-04-23'
 
Period Examples::

  ${_upload_time} > ( {allocated_time} + {2_days} )
  ${_start} + {7_days}
  ${_start} + {7_days} + {20_minutes} 
  ${_start} + {23:23:23}
  now() - ${_upload_time} < {2_days}
 
Special Terms Examples::

  ${image} empty
  _upload_time > '2017-01-23'
