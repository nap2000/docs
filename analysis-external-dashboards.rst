.. _analysis-external:

External Dashboards
===================

.. contents::
 :local:
 
External dashboards such as Tableau and PowerBI can be configured to access data collected by Smap.

Live Data
---------

To show live data in a dashboard that automatically updates as more data is collected use the web service data API's that return
data in JSON format.  For PowerBIO the approach is as follows:

#1.  Find the URL that returns data by using /api/v1/data in your browser and then selecting the data link for the survey you are interested in.
#2.  In PowerBI select get data from another source
#3.  Select web as the source
#4.  Enter the URL that that you found in step 1
#5.  Remove "?links=true" from the URL as it is only useful for browsing for data

.. warning::

  Don't select CSV data source in PowerBI and then enter a URL that downloads data in CSV format.  PowerBI will treat the URL as a file
  and make a large number of identical calls to it, these will be rate limited by the server and your data access
  may fail.  You can however use CSV files if you download them first, then make them available to PowerBI.  You could do this either in a
  script that updates the file periodiclly or you could select the option in PowerBI to upload the CSV file to One Drive.

Static Data
-----------

You can get access to data manually using the approach for live data.  You can also import data from exported spreadsheets.



