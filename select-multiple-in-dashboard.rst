.. _sm_dashboard:

Select Multiple Questions in a Dashboard
========================================

.. contents::
 :local:
 
In the database, answers to select multiple questions are stored as space separated values.  For example
here is data from a question asking for the titles applicable to a criminal complaint::

                                  title
  ---------------------------------------------------------------------
   In_possession_of_Dangerous_Drug
   Unlawful_Assault Provoking_Breach_Of_Peace
   Domestic_Violence
   Rape
   Unlawful_Wounding
   In_possession_of_Dangerous_Drug Conveying_of_D/Drugs Stealing_Minor

Exporting for Analysis
----------------------

By default when you export select multiples they are converted into one column per choice, so a question with
10 choices would be exported in 10 columns.  The value put
into each choice column is 0 or 1.  This is the preferred format for analysis by tools such as SPSS.  In
a spreadsheet you could simply sum the values in a column to find out how many times a choice was selected.

You can also choose "Compress select multiples" when exporting.  In this case there is only one column per
per question and the selected choices are shown space separated as above. 

Creating a bar chart in a dashboard
-----------------------------------

Dashboards don't handle either of the above formats.  At least I could not find out how to do this in Quicksight.
Fortunately we can use the Postgres function regexp_split_to_table() to transform the data into a table row per 
choice that the dashboard can process. This function takes two parameters, the text to transform and a regular
expression telling it how to split the text into rows. So for the above example of "title"::

  select regexp_split_to_table(title, '\s+') as title from ob;

                 title
  -----------------------------------
   In_possession_of_Dangerous_Drug
   Unlawful_Assault
   Provoking_Breach_Of_Peace
   Domestic_Violence
   Rape
   Unlawful_Wounding
   In_possession_of_Dangerous_Drug
   Conveying_of_D/Drugs
   Stealing_Minor
   In_possession_of_Dangerous_Drug

Now the data is in a format that can be used by the dashboard.

Connecting your dashboard to the modified data
----------------------------------------------

You can create a database view for each select multiple::

  create view regexp_split_to_table(title, '\s+') as title, station from ob;

In the above example I have added police station as a column so the dashboad can present the data broken
down by station.

You can then give permission for your dashboard to access this view in the database. To do this you would need to be 
running your own server instance.  If you are using the SG server and need this feature then contact the Smap support
team.
