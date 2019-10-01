Server Calculations
===================

.. contents::
 :local:

Introduction
------------

Questions can be added to surveys where the answer is calculated on the server and not on the phone.   When creating reports or
viewing data in the console these calculations appear just like data that was entered in Weborms or on a mobile device.  An important
difference is that the calculation is performed when the data is viewed.  Hence if you change the expression used in the server 
calculation then the answer shown will change for all previously collected data.

.. note::

  You can also create calculation questions that are performed within a survey by specifying a question ot type "calculate".   
  This is useful if you are going to use the results of that calculation during the data collection process, perhaps in a 
  relevance. However it the calculation is only used during analysis you could consider server calculations.  Calculations
  performed in a survey are fixed once the data is submitted.  So if you update the survey to change the calculation the 
  values calculated for already collected data will not change.
  

Excel Editor
------------

In the Survey sheet specify

* type:  server_calculate
* name:  Specify a unique name name
* server_calculation:  Put the calculation here

Syntax
------

Referring to Questions
++++++++++++++++++++++

Use the same approach that is used for referring to questions in a relevance. That is surround
the question name with curly brackets and put a dollar sign in front.

Questions can be in any form. For example you may have a survey that gathers information on
comapanies and the projects that they are involved in.  The following filter will trigger on a
company name of "Widgets" that has at least one project with a value over 100,000

.. code-block::

   {company_name} = 'Widgets' and ${project_value} > 100000

Examples
++++++++

.. code-block::

  * ${person_name} = 'Tom'
  * ${age} > 5


                <h2>Supported Question Types</h2>
                <ul>
                    <li>text</li>
                    <li>integer</li>
                    <li>decimal</li>
                    <li>select_one</li>
                    <li>barcode</li>
                    <li>calculation</li>
                    <li>date</li>
                    <li>datetime</li>
                    <li>acknowldege</li>
                </ul>
                <h2>Minimal-Support</h2>
                These question types can be used only to check to see if they were answered. For example
                "${video_question} empty"
                <ul>
                    <li>image</li>
                    <li>audio</li>
                    <li>video</li>
                    <li>geopoint</li>
                    <li>polygon</li>
                    <li>line</li>
                </ul>
                <h2>Un-Supported</h2>
                The following question types currently cannot be used to filter data
                <ul>
                    <li>select_multiple</li>

                </ul>
            </div>


            <h1 id="operators" class="page-header">
                <a class="anchorjs-link " href="#operators" aria-label="Anchor link for: operators"
                   data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal;
	   				font-variant: normal; font-weight: normal; position: absolute; margin-left: -1em; 
	   				padding-right: 0.5em; margin-bottom: 2em;">Operators</a>
            </h1>
            <h2>Operators</h2>
            <p>These are used for comparisons and to build up more complex expressions.  There must be a space each
                both sides of these operators.</p>

            <ul>
                <li>= (equals)</li>
                <li>> (greater than)</li>
                <li>< (less than)</li>
                <li>>= (Greater than or equals)</li>
                <li><= (Less than or equals)</li>
                <li>!= (Not equals)</li>
                <li>not</li>
                <li>- (minus)</li>
                <li>+ (plus)</li>
                <li>* (times)</li>
                <li>/ (divide)</li>
                <li>and</li>
                <li>or</li>
                <li>like (Similar to.  Use the % symbol to match a range of characters.
                    Use the _ underscore character to match a single character)</li>
                <li>not like (returns the rows that do not match)</li>
            </ul>
            <b>Examples</b>
            <ul>
                <li>${age} > 25</li>
                <li>${age} > 25 or ${name} = 'tom'</li>
                <li>${name} like 'sam%'   (Matches "sam", "samuel", "sammy" etc)</li>
                <li>${city} like '_erlin'   (Matches "Berlin", "berlin")</li>
                <li>${city} not like '%ich%'   (Matches anything that does not have "ich" in it )</li>
            </ul>

            <h1 id="brackets" class="page-header">
                <a class="anchorjs-link " href="#brackets" aria-label="Anchor link for: brackets"
                   data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal;
	   				font-variant: normal; font-weight: normal; position: absolute; margin-left: -1em;
	   				padding-right: 0.5em; margin-bottom: 2em;">Brackets</a>
            </h1>
            <h2>Brackets</h2>
            <p>Use smooth brackets for "association".  Like for operators these brackets must have spaces
                around them.</p>

            <ul>
                <li>(</li>
                <li>)</li>
            </ul>
            <b>Examples</b>
            <ul>
                <li>${age} > 25 or ( ${name} = 'tom' and ${age} > 5 )</li>
            </ul>

            <h1 id="constants" class="page-header">
                <a class="anchorjs-link " href="#constants" aria-label="Anchor link for: constants"
                   data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal;
	   				font-variant: normal; font-weight: normal; position: absolute; margin-left: -1em;
	   				padding-right: 0.5em; margin-bottom: 2em;">Constants</a>
            </h1>
            <h2>Constants</h2>

            <ul>
                <li>integers written as is</li>
                <li>decimals written as is</li>
                <li>text values enclosed in single quotes</li>
                <li>date values enclosed in single quotes and in the following format yyyy-mm-dd.  Note
                that you need to enter two characters for months and days.</li>
            </ul>
            <b>Examples</b>
            <ul>
                <li>${name} > 25</li>
                <li>${weight} < 0.5</li>
                <li>${name} = 'tom'</li>
                <li>${date_question} = '2016-04-23'</li>
            </ul>

            <h1 id="dates" class="page-header">
                <a class="anchorjs-link " href="#brackets" aria-label="Anchor link for: dates"
                   data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal;
	   				font-variant: normal; font-weight: normal; position: absolute; margin-left: -1em;
	   				padding-right: 0.5em; margin-bottom: 2em;">Date Calculations</a>
            </h1>
            <h2>Date Formats</h2>
            <ul>
                <li>'yyyy-mm-dd'</li>
            </ul>
            Hence the thirty first of January, 2018 would be:  '2018-01-31'

            <h2>Date Intervals</h2>

            <ul>
                <li>{1_day}</li>
                <li>{n_days}</li>
                <li>{1_hour}</li>
                <li>{n_hours}</li>
                <li>{1_minute}</li>
                <li>{n_minutes}</li>
                <li>{1_second}</li>
                <li>{n_seconds}</li>
                <li>{hh:mm:ss}</li>
            </ul>

            <h2>Other</h2>

            <ul>
                <li>now()  (The current date and time)</li>
            </ul>
            <b>Examples</b>
            <ul>
                <li>${_upload_time} > ( {allocated_time} + {2_days} )</li>
                <li>${_start} + {7_days}</li>
                <li>${_start} + {7_days} + {20_minutes} </li>
                <li>${_start} + {23:23:23}</li>
                <li>now() - ${_upload_time} < {2_days}</li>
            </ul>

            <h1 id="special" class="page-header">
                <a class="anchorjs-link " href="#special" aria-label="Anchor link for: special terms"
                   data-anchorjs-icon="" style="font-family: anchorjs-icons; font-style: normal;
	   				font-variant: normal; font-weight: normal; position: absolute; margin-left: -1em;
	   				padding-right: 0.5em; margin-bottom: 2em;">Special Terms</a>
            </h1>
            <h2>Special Terms</h2>

            <ul>
                <li>is null (Test to see if an answer was <b>not</b> given to a media or geopoint question)</li>
                <li>is not null (Test to see if an answer was given to a media or geopoint question)</li>
                <li>_upload_time (The date that the survey was uploaded to the server)</li>
                <li>_start (The time the survey was started)</li>
                <li>_end (The time the survey ended)</li>
                <li>${_hrk} (The generated unique key for the record)</li>
                <li>${_device} (The device identifier that submitted the results)</li>
                <li>${_user} (The logon identifier of the user that submitted the results)</li>
            </ul>
            <b>Examples</b>
            <ul>
                <li>${image} empty</li>
                <li>_upload_time > '2017-01-23'</li>
            </ul>

        </div>


If Function
+++++++++++

One of the most important functions is if().  The excel editor adds additional support to make it easier to specify these.  Currently
the if() function for server calculates is not supported by the online editor.

In the server_calculate column of the survey sheet enter only:  if().  In the following example there are two server 
calculations the second of which is an if().

.. figure::  _images/sc_if_survey.jpg
   :align:   center

   if() Server Calculations
   
Then set the conditions and their values in the "conditions" sheet of the excel file.

.. figure::  _images/sc_if_cond.jpg
   :align:   center

   if() Conditions
   
In the above example the value of q3 will be set to 'A Selected' if the answer to q1 was 'A'; 'B Selected' if the answer to q1 was 'b'; and 
to 'Something else selected' in all other cases.  




