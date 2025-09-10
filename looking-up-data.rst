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

.. _looking-up-data-file:

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
  search('linked_self')
  search('linked_s3_23', 'matches', 'region_v', ${region})

.. note::

  Use linked_self to lookup data previously submitted in the same survey

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

Filter the data (4 parameters)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

::

 search('SOURCE', 'A FILTER FUNCTION', 'COLUMN IN SOURCE TO FILTER ON', FILTER VALUE)

The filter function can be one of:

#.  contains    (For use in webForms requires Smap server 21.08)
#.  startswith  (For use in webForms requires Smap server 21.08)
#.  endswith    (For use in webForms requires Smap server 21.08)
#.  matches
#.  in
#.  not in
#.  eval        (requires FT6.505 and Smap server 21.09, not available in webForms)

The filter values for "in" and "not in" should be lists separated by spaces. Use it with filter values that come from select multiple questions.

.. warning

  Using column names in the CSV file of "name" or "label" to filter on will cause problems in webForms if these are not also the columns
  that are used for the value and label of the choice.  In other words if you are going to call a CSV column "label" then make sure it does
  contain the label! 

Double filter the data (6 parameters)
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

.. _looking-up-data-pulldata:

Getting Reference Data with the Pulldata Function
--------------------------------------------------

The second type of data that you can get from a CSV file, or another survey, is reference data.  This is data that
is "pulled" from it's source and added as the answer to a calculate question.  
It can then be treated like any other answer, and be sent to the server, used in a relevance etc.

There are 4 different versions of the pulldata function with 3,4,5 or 6 parameters.

*  **3 params:** Get a single value identified using an expression
*  **4 params:** Get a single value identified by a specific value in a single filter column 
*  **5 params:** Get a result for multiple values identified using an expression
*  **6 params:** Get a result for multiple values identified by specific value in a single filter column 

The Syntax::

  pulldata('source', 'column to retrieve', 'filter expression')
  pulldata('source', 'column to retrieve', 'filter column', 'filter value')
  pulldata('source', 'column to retrieve', 'filter expression', 'index', 'eval')
  pulldata('source', 'column to retrieve', 'filter column', 'filter value', 'index', 'filter type')

The most commonly used version is the one with 4 parameters.  This is also the standard pulldata version 
that is used by other data collection tools.

Get a value using a key (4 parameters)
++++++++++++++++++++++++++++++++++++++

Add a calculate question to your survey and give it a name. For the calculation specify the pulldata function::

  pulldata('source', 'column to retrieve', 'filter column', 'filter value')

#.  The source can be the :ref:`name of a CSV file <looking-up-data-file>`, without its extension or :ref:`the identifier for another survey. <looking-up-data-survey>`
#.  The column to retrieve is the name of the column in the CSV file whose data you want, or the name of the question in the survey that you are looking up.
#.  The filter column is the name of the column / question that identifies the value to retrieve.  So if you are looking up the product name using the product code, then this parameter contains the name of the product code column.
#.  The filter value is the value of the filter name that you want.  So for the product example if the filter value was set to 'a10' then you would expect to get back the product name for the product with code 'a10'.

.. _filter-expressions:

Get a value using an expression (3 parameters)
++++++++++++++++++++++++++++++++++++++++++++++

In this approach the 'filter column' and 'filter value' are replaced by an expression.  This allows much more
flexibility in how the 'column to retrieve' is selected::

  pulldata('source', 'column to retrieve', 'filter expression')

When using an expression to filter data you can use the ${question name} syntax to refer to questions in the 
current survey as usual. However to refer to columns in the csv file or referenced survey use #{column name}.

You can also enclose the whole expression in double quotes.  This allows you to use single quotes around text values.  
For example  "#{city} = 'london'"

Data values may need to be "cast" to integer or decimal types.
This is because all CSV data is stored as text. For example if you have a filter expression like "#{age} < ${max_age}". 
Here #{age} is the age value in the csv table and you will need to change your expression 
to "cast( #{age} as integer ) < ${max_age}".  Refer to :ref:`server-expressions-cast` for more details.

.. warning::

  In fieldTask, a pulldata function using an "expression" is not automatically triggered if any of the 
  referenced questions changes their value. This means that the pulldata value 
  will not be updated when you were expecting it to be
  However you can force this behaviour by enclosing the pulldata function within an if() function 
  that references the same questions.  The examples
  below show this approach.

.. csv-table:: Examples of pulldata using expressions
  :header: pulldata, Comment

  "if(string-length(${product_code}) > 0, pulldata('products', 'product_name', '#{product_code} = ${product_code} '), '')", This is the same as the simple product name lookup that was described for the 4 parameter version of pulldata! Note that we use #{product_code} to refer to the value from the product_code column in the CSV file. We also refer to the answer to the product code question in the survey using the normal ${} syntax. The pulldata() is enclosed inside an if() function so that fieldTask knows to trigger it when the product_code changes.
  "if(string-length(${product_code}) > 0, pulldata('products', 'product_name', '#{product_code} = ${product_code} and #{region} = ${region}'), '')", Now an example that can't be implemented using the simple 4 parameter version.  This example assumes that product codes can be reused in different regions so to get the right product name you also want to filter by region.
  "if(string-length(${product_code}) > 0, pulldata('products', 'product_name', ""#{product_code} = ${product_code} and #{region} = ${region} and #{year} = '2022' ""), '')", An additional filter by year has been added. Note that because the year is fixed and enclosed in single quotes we have enclosed the whole expression in double quotes.

Get multiple values (5 and 6 parameters)
++++++++++++++++++++++++++++++++++++++++

The previous examples just returned a single value.  If more than one record matches a key just the first
will be returned.  However you can use :ref:`repeating groups <xls-repeats>` to show repeating reference 
data.

The pulldata functions look like this::

  pulldata('source', 'column to retrieve', 'filter expression', 'index', 'eval')
  pulldata('source', 'column to retrieve', 'filter column', 'filter value', 'index', 'filter type')

The first version, 5 parameters, adds an 'index' parameter.  The final parameter 'eval' doesn't do anything,
it is just that there to differentiate this from from the standard 4 parameter pulldata function.

The second version, 6 parameters, add the 'index' parameter and a 'filter type' to the standard 4 parameter version.

Index
%%%%%

The index starts at 1 and allows you to specify which of the multiple matching values you want. So if the index is 3 you
will get the answer in the 3rd matching record.

Instead of a number you can use one of the following aggregation functions as the index:

  *  **sum** - The sum of all the records
  *  **mean** - The mean or average of the values
  *  **min** - The minimum value
  *  **max** - The maximum value
  *  **count** - The count of the number of matching records
  *  **list** - All the matching values separated by a space
 
.. note::

  Where the index is a number it does not have quotation marks.

Filter Type
%%%%%%%%%%%

This is used only with the 6 parameter version and specifies how to filter records.  It works in the same way as the filter function
in :ref:`search <look-up-filters>`.  In the standard pulldata version this is not needed because the filter type has to be matches
since only one record should be found.

  *  contains
  *  startswith
  *  endswith
  *  matches
  *  in
  *  not in 

Example usage
%%%%%%%%%%%%%

.. csv-table:: Reviewing Multiple Complaints - 6 parameter version
  :width: 150
  :widths: 10,10,10,60,60
  :header: type, name, repeat_count, calculation, comment

  calculate, number_recs, ,"pulldata('linked_s11_2134', 'complaint_type', 'office', ${office}, 'count', 'matches')", returns the number of records for the selected office. The second parameter is ignored when using an aggregate function for the index.
  begin_repeat, rpt, int( ${number_recs} ), , Creates a repeat group for each matching complaint.  Note that the repeat count has to be cast to an integer as calculates have text value by default
  note, type, , "pulldata('linked_s11_2134', 'complaint_type', 'office', ${office}, position(..), 'matches')", The pulldata function is almost the same as before except this time we are getting the value for the record number that corresponds to the position in the repeat.
  note, complaint, , "pulldata('linked_s11_2134', 'complaint', 'office', ${office}, position(..), 'matches')", This time we get the details of the complaint as the value of the note
  end_repeat, rpt, , , 

.. _looking-up-data-local:

Support in FieldTask and SmapServer
+++++++++++++++++++++++++++++++++++

.. csv-table:: Support for looking up data in CSV files and other surveys
  :header: pulldata version, fieldTask offline, fieldTask online, webForms offline, webForms online

  3 params, v6.503, v6.503, v20.09, v20.09
  4 params, v6.503, yes, yes, yes
  5 params, v6.503, 6.503, v20.09, v20.09
  6 params, v6.503, 6.503, v20.09, v20.09

More Pulldata Examples
++++++++++++++++++++++
  
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


