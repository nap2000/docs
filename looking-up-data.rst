.. _looking-up-data:

Looking up Data
===============

.. contents::
 :local:

Overview
--------

Lists of choices and reference data can be obtained from sources outside of the survey template.  This allows you to:

*  Update the survey with new choices or reference values without changing the survey template,

*  Share the same data between multiple surveys, for example lists of provinces and districts for a user to select.

*  Use much larger numbers of potential choices and reference values than you could put directly into a survey without making it too slow to load

Sources
-------

Data can be sourced from:

*  CSV Files
*  Surveys

CSV files can be used with data that does not change too often as it is a manual process to upload an updated CSV file onto the server.  Data
sourced from other surveys will be available automatically as soon as the data is submitted to the source survey.

In the remainder of this document the source of the data will be written as *SOURCE*.  Replace this with the name of the CSV file or the 
identifier of the survey that contains your data.

.. _looking-up-data-csv:

Using CSV Files
+++++++++++++++

Creating the file
%%%%%%%%%%%%%%%%%

The first row of the CSV file contains the header. Use the same rules for specifying column headers as are used for question names,
that is english characters and underscores with no spaces.  

Subsequent rows contain the data.  These can contain any characters supported by your phones using Unicode.

.. warning::

  The name of the CSV file should not have any spaces.

Loading a CSV file onto the Server
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

If your CSV file might be used by more than one survey then you should load it on to the server as a shared resource.

*  Select the *Admin* module
*  Select *Shared Resources*
*  Click on the *Add File* button and select all the CSV files that you want to load
*  Click on the *Upload* button

Your CSV file is now available to any survey that refers to it.

If you want your CSV file to be only used by a single survey then:

*  Select the *Admin* module
*  Select *Forms*
*  Click on the form name to edit it
*  Select the menu *File* then *Media*
*  Click on the *Add File* button and select all the CSV files that you want to load
*  Click on the *Upload* button

Referring to the file
%%%%%%%%%%%%%%%%%%%%%

Replace SOURCE with the name of the file without the CSV extension.  In the following examples the full file name is "locations.csv"::

  search('locations')
  search('locations', 'matches', 'region_v', ${region})

.. _looking-up-data-survey:

Using another Survey as the Source
++++++++++++++++++++++++++++++++++

Replace SOURCE with "linked\_"  followed by the ident of the survey.  In the following examples the survey ident is s3_23::


  search('linked_s3_23')
  search('linked_s3_23', 'matches', 'region_v', ${region})

.. note::

  The online editor will guide you through accessing another survey's data.  For example to look up choices in another survey select
  appearance, click on the edit button and then select the **search** tab.  You can then look up available surveys without having to 
  know their "ident".  

.. note::

  If you are editing your survey in a spreadsheet then you can find "ident" of the survey that you are looking up by again using the 
  online editor but this time open the file that you want to reference and then select the menu option **File** and then **Info**.  

.. warning::

  The survey that is referenced will need to be in the same organisation as the survey doing the referencing.

Looking up Choices
------------------

The approach is similar to using choices from the choices sheet but with the difference that the choices list contains the names of the columns 
that have the choices rather than the choices themselves.  You will also need to add a "search()" function to the question's **appearance** 
telling it where to get the data.

Specifying Column Names
+++++++++++++++++++++++

*  In the name column of the choices list specify the column name that contains the **value** of the choice.  
*  In the label column(s) of the choices list specify the column name that contains the **label** for the choice.

.. figure::  _images/lookup1.jpg
   :align:   center
   :alt:     Setting the choice list values

   Setting the choice list values

Notes:

*  In the label you can specify multiple column names separated by commas.  The data from each of these columns will then be combined and shown to the user
*  The value column and the label column can be the same
*  The choice labels can be in multiple languages as you can specify a different column for each language just as you would normally specify different text for each language

Adding fixed choices
%%%%%%%%%%%%%%%%%%%%

You can add fixed choices to the choices that are sourced from the csv file or survey.  For example you may have a select question to look up 
geographic locations from a survey.  These locations may be where your team is working and be maintained in a separate survey.
That survey is presumably not going to have a value for a location of
"none of these".  Hence you can add that directly as a fixed choice.  The value must be numeric to distinguish this choice from the choice that identifies in the CSV file.

.. figure::  _images/lookup2.jpg
   :align:   center
   :alt:     Adding fixed choices

   Adding fixed choices

The Search Function
+++++++++++++++++++

The search function is placed in the **appearance** of the select question and tells the system where the source of data can be found.  This function
has between 1 and 5 parameters depending on how complex your filtering requirements are:

Simple (1 parameter)
%%%%%%%%%%%%%%%%%%%%

::

  search('SOURCE')

Looks in SOURCE for the data.

Only this simple form of the search function can be used with WebForms.

.. note::

  Duplicates will be removed.

.. _look-up-filters:

Filter the data (3 parameters)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

::

 search('SOURCE', 'A FILTER FUNCTION', 'COLUMN IN SOURCE TO FILTER ON', FILTER VALUE)

The filter function can be one of:

#.  contains    (For use in webforms requires smap server 21.08)
#.  startswith  (For use in webforms requires smap server 21.08)
#.  endswith    (For use in webforms requires smap server 21.08)
#.  matches
#.  in
#.  not in
#.  eval        (requires FT6.505 and smap server 21.09)

The filter values for "in" and "not in" should be lists separated by spaces. Use it with filter values that come from select multiple questions.

.. warning

  Using column names in the CSV file of "name" or "label" to filter on will cause problems in webforms if these are not also the columns
  that are used for the value and label of the choice.  In other words if you are going to call a CSV column "label" then make sure it does
  contain the label! 

Double filter the data (5 parameters)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Like the normal filter but with an extra "matches".

::

  search('SOURCE', 'A FILTER FUNCTION', 'COLUMN IN SOURCE TO FILTER ON', FILTER VALUE, 'COLUMN TO MATCH ON', VALUE TO MATCH)

Example::

  search('children', 'matches', 'class_v', 'class1', 'enrolled_v', 'yes')

Returns all records in the children csv file where the "class_v" column has the value "class1" and the "enrolled_v" column has the value "yes".

Examples
%%%%%%%%

.. csv-table::  Search examples
  :widths: 1,20,10
  :header-rows: 1
  :file: tables/choices-example-list.csv

for more information on using the **eval** function refer to :ref:`filter-expressions`.

Getting Reference Data with the Pulldata Function
--------------------------------------------------

The second type of data that you can get from a CSV file or another survey is reference data.  There are 4 different versions with 3,4,5 or 6 arguments.

#.  **3 params:** Get a single value identified using an expression
#.  **4 params:** Get a single value identified by a specific value in a single filter column 
#.  **5 params:** Get a result for multiple values identified using an expression
#.  **6 params:** Get a result for multiple values identified by specific value in a single filter column 

Syntax::

  1. pulldata('source', 'column to retrieve', 'filter expression')
  2. pulldata('source', 'column to retrieve', 'filter column', 'filter value')
  3. pulldata('source', 'column to retrieve', 'filter expression', 'index', 'eval')
  4. pulldata('source', 'column to retrieve', 'filter column', 'filter value', 'index', 'filter type')

.. warning::

  In fieldTask, a pulldata function using an "expresion" is not automatically triggered if any of the 
  referenced questions changes their value. This means that the pulldata value 
  will not be updated when you were expecting it to be
  However you can force this behaviour by enclosing the pulldata function within an if() function 
  that references the same questions.  The examples
  below show this approach.

Example showing how to force a 3 parameter pulldata to be called::

  if(string-length(${id_no}) > 0, pulldata('source', 'column to retrieve', '#{key} = ${id_no}'), '')

.. note::

  Looking up data for static references may cause problems as the lookup function needs to be triggered
  by a change in one of its parameters.  For exmaple:   lookup('ref_data', 'name', 'code',  'AAAA1').   So
  in this example the code is fixed and the lookup will not automatically be triggered.

Support
+++++++

.. csv-table:: Support for looking up data in CSV files and other surveys
  :header: pulldata version, fieldTask offline, fieldTask online, webForms offline, webForms online

  3 params, v6.503, v6.503, v20.09, v20.09
  4 params, v6.503, yes, yes, yes
  5 params, v6.503, 6.503, v20.09, v20.09
  6 params, v6.503, 6.503, v20.09, v20.09

Examples
++++++++
  
You may want to look up the maximum age for a program in a particular region. This example uses the 4 parameter version.
In this example we ask what training sector the interviewee is interested in. Then we ask their age.  We then do a lookup in
the csv file "ref_data.csv" for the maximum allowed age for that sector.  Then if the person qualifies we ask them if they want to enroll.


.. csv-table:: Pulldata: 
  :width: 160
  :widths: 20,20,40, 40, 40
  :header-rows: 1
  :file: tables/pulldata-example.csv

Other examples:

.. csv-table:: Pull data examples
  :widths: 1,20,10
  :header-rows: 1
  :file: tables/pulldata-example-list.csv

Online Lookup
+++++++++++++

If you have a network connection when filling in the form then you can replace "pulldata" with "lookup".  All other parameters remain the same.
For example::

  lookup('source', 'column to retrieve', 'filter expression')
  lookup('source', 'column to retrieve', 'filter column', 'filter value')

When you have very large amounts of reference data lookup can be more practical. Refer to 
`this article <https://blog.smap.com.au/performance-issues-when-looking-up-reference-data//>`_ 
for a discussion on why this is the case.

Selecting Multiple Values
+++++++++++++++++++++++++

.. warning::

  This feature is available in fieldTask 6.200 and above.  It is not available in Webforms.

To select multiple values you can use two additional parameters:

1.  An index into the record you want.  the index of a record starts from 1, however there are two special values:

In FieldTask version 6.500 and above you can also use the following aggregation functions instead of the index:

  *  **sum** - The sum of all the records
  *  **mean** - The mean or average of the values
  *  **min** - The minimum value
  *  **max** - The maximum value
  *  **count** - The count of the number of matching records
  *  **list** - All the matching values separated by a space
 
2.  A filter type to select the data you want to include

  *  contains
  *  startswith
  *  endswith
  *  matches
  *  in
  *  not in 

General Syntax::

  pulldata('SOURCE', 'COLUMN IN SOURCE TO RETRIEVE', 'COLUMN IN SOURCE TO FILTER ON', 'FILTER VALUE', index, 'FILTER FUNCTION')

.. note::

  Where the index is a number it does not have quotation marks.

By using these parameters you no longer need to specify a unique key as the 'COLUMN IN SOURCE TO FILTER ON'.  Instead you can get data from multiple
rows that match the filter function.

The following examples are for the scenario where a child can be enrolled in multiple classes using a select multiple.  So the class codes
are space separated.  ${class} is the answer from a question that identifies the class; the pulldata functions then get the children
enrolled in that class::

  pulldata('linked_s30_268', 'first_name', 'enrolled_in', ${class}, "count", 'contains')
  pulldata('linked_s30_268', 'first_name', 'enrolled_in', ${class}, "list", 'contains')
  pulldata('linked_s30_268', 'first_name', 'enrolled_in', ${class}, 4, 'contains')

The first example gets the number of children in the class.  This could be used as the repeat_count for a "begin repeat" that shows data on
each enrolled child.  The second example gets all of the children's first names as a space separated list. The third example gets the fourth child
in the list.  You can use this last example inside a "begin repeat" where you replace "4" with "position(..).

.. _filter-expressions:

Notes on Filter Expressions and Evaluations
-------------------------------------------

When using an expression to filter data you can use the ${question name} syntax to refer to questions in the current survey as usual. However to 
refer to columns in the csv file or referenced survey use #{column name}.

You can also enclose the expression in double quotes.  This allows you to use single quotes around text values.  For example  "${city} = 'london'"

When using an expression to get data may need to "cast" values to integer or decimal.  
This is because all CSV data is stored as text. For example if you have a filter expression like "#{age} < ${max_age}". 
Here #{age} is the age value in the csv table and you will need to change your expression to "cast( #{age} as integer ) < ${max_age}". 
Refer to :ref:`server-expressions-cast` for more details.

.. _looking-up-data-local:

Local Data
----------

Available with FieldTask Version 6.400 and SmapServer version 21.05

Normally when you reference data in other surveys you are looking up data that is stored on the server and has then been copied onto your device.  
However you may need to complete multiple surveys in a location without an internet connection and while at that remote location 
you may want to reference data that was entered in another survey but has not been submitted yet.  

Surveys have local data searching turned off by default as it could potentially result in significantly longer load times for a survey in cases where
the device has been used offline for a significant period of time and their are hundreds of unsent results.  

To turn local data searching on with the online editor select the menu ``file`` and then ``settings``.  In the settings dialog select the checkbox
labelled "Lookup local, unsent data on device".

To enable local data searching using the xlsForm editor set a value of "yes" in the column "search_local_data" in the settings worksheet (:ref:`settings-reference`).

Values from the local unsubmitted data will then be included in data returned from a search() or a pulldata() function. This happens transparently and
no further action on your part is required.  


