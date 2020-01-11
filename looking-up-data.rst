.. _looking-up-data:

Looking up Data
===============

.. contents::
 :local:

Sources
-------

Data can be sourced from:

*  CSV Files
*  Surveys

In the remainder of this document the source of the data will be written as *SOURCE*.  Replace this with the name of the CSV file or the 
identifier of the survey that contains your data.

Using CSV Files
+++++++++++++++

Creating the file
%%%%%%%%%%%%%%%%%

The first row of the CSV file contains the header. Use the same rules for specifying column headers as are used for question names
english characters and underscores with no spaces.  

Subsequent rows contain the data.  These can contain any characters supported by your phones using Unicode.

.. note::

  Microsft Excel does not support Unicode characters in CSV files.  Hence if you want to use non English characters you should use a
  different spreadsheet editor such as Libre Office.

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

Using another Survey as the Source
----------------------------------

.. warning::

  The user creating the reference to the second survey will need to have access to that survey.  It will need to be in a project that they
  can access and if it has a security role the survey editor will also need that security role.  However the enumerator filling in a survey
  need not have access to the referenced survey.  The survey editor is effectively giving access to the referenced data to any user who
  has access to the survey that looks up that reference.

Choices
-------


