.. _analysis-external:

External Dashboards
===================

.. contents::
 :local:

External dashboards such as Power BI and Tableau can be configured to access data collected by Smap.  They read
it through the data API, so the dashboard updates as more data is collected without anybody having to export a
spreadsheet.

Use version 2 of the API for this.  It authenticates with an API key sent in a header, which is what these tools
expect, and a key can be revoked on its own if a report is retired or a laptop is lost.  Version 1 uses the
account password over Basic authentication, so anybody who can open the workbook learns the password to the
whole account.

Getting a key
-------------

Create the key from the **API key** item on the user profile menu.  Creating and revoking keys is described in
:ref:`user-profile-api-key`, and the API itself in :ref:`apis`.

Some advice that applies whichever dashboard tool you use:

*  Give each report its own key, named after the report.  When the report is retired, or the person who built it
   leaves, revoke that one key and nothing else stops working.
*  Copy the key while it is displayed.  It is shown once and the server keeps only a hash of it.
*  Think about the expiry before choosing it.  A scheduled refresh whose key has expired simply starts failing,
   some months after anybody last thought about it, and the only symptom is an authentication error.  Either
   choose **Never** for a dashboard, or note the date and replace the key before it arrives.
*  The key is stored inside the workbook or the published dataset in a form that can be read.  Treat a workbook
   holding one as you would treat the password.

Which key belongs to which report cannot be worked out later from the key itself, so the name is worth filling
in properly.

The data URLs
-------------

Data for one survey is available in two formats:

*  ``https://<your server>/api/v2/data/<survey ident>`` returns JSON
*  ``https://<your server>/api/v2/data.csv/<survey ident>`` returns CSV

To find the survey ident, browse ``https://<your server>/api/v1/data?links=true`` in a browser and follow the
link for the survey you want.  Version 1 is used here only because a browser can answer its password prompt - a
browser cannot send the ``x-api-key`` header, so version 2 URLs cannot be browsed in the same way.  Take the
identifier out of the version 1 URL and put it into the version 2 URL above.

Add the key to every request as a header:

.. code-block:: none

  x-api-key: smap_a_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

A request with no key, an unknown key, an expired key or a revoked key is answered with 401 and
``{"code": 401, "message": "Unknown User"}``.  The four cases are deliberately not distinguished.

Records returned, and how often you can ask
-------------------------------------------

Two server settings limit what the API returns.  Both are shared by everybody in your organisation rather than
being per key, and your server administrator sets them (:ref:`admin-server`):

*  **API requests per minute**.  Once the organisation has used them up, further requests are refused until the
   next minute.  A refused request is answered with the text ``Rate exceeded. Access to this service is rate
   limited to n requests per minute.`` in place of the data, so the dashboard reports a parsing error rather
   than an obvious rate limit.  When a refresh fails in a way that makes no sense, this is worth ruling out
   first.
*  **Max records per API request**.  Where this is set, a request asking for more records than the limit is
   given the limit instead.  A dashboard showing fewer rows than the survey holds is usually this.

The ``limit`` and ``start`` query parameters control how much is returned:

*  ``limit`` is the number of records, subject to the server setting above.
*  ``start`` is **a primary key to start from, not a row offset**.  Records are returned from that key onward.

That distinction matters when a tool offers to page through the data for you.  Those pagers assume ``start``
counts rows, and Smap primary keys are not a gapless count of rows - there are gaps wherever a record has been
deleted.  Left to page on its own, such a tool loses records and repeats others.

.. note::

  Rather than paging, ask for the whole survey in one request and let the dashboard refresh on a schedule.  If a
  survey really is too large for that, page by asking for records from the highest primary key you have already
  received, plus one - not by counting rows.

Power BI
--------

Use the **Web** source, not the CSV source, and set its credentials to **Anonymous**.  The key travels in the
header, and choosing any other credential type makes Power BI send something else instead.

Build the query with ``RelativePath`` and ``Query`` rather than joining the URL together as text:

.. code-block:: none

  let
      Key    = "smap_a_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      Source = Json.Document(
          Web.Contents("https://<your server>",
              [ RelativePath = "api/v2/data/<survey ident>",
                Query   = [ limit = "10000" ],
                Headers = [ #"x-api-key" = Key ] ])),
      Table  = Table.FromRecords(Source)
  in
      Table

A URL assembled by joining text together is treated by the Power BI service as a dynamic data source and refused
when the report is refreshed on a schedule, even though it works on the desktop.  Written as above the address
stays fixed and only the path and the parameters vary, which the service accepts.

Hold the key in a Power BI parameter rather than typing it into each query, so that replacing it is one edit.

.. warning::

  Don't select CSV as the source in Power BI and then enter a URL that downloads data in CSV format.  Power BI
  treats the URL as a file and makes a large number of identical calls to it, which will use up the requests per
  minute allowed to your organisation and cause the refresh to fail.  You can use CSV files if you download them
  first and then make them available to Power BI as a file, either from a script that updates the file
  periodically or by putting it on OneDrive.

Tableau
-------

Use the **REST API Connector** from the Tableau Exchange.  It reads JSON and CSV over HTTP and, unlike the built
in web sources, can send a header of your own.  It needs Tableau 2023.3 or later.  Web Data Connectors are not
the way to do this any more: the 2.x framework is being removed, and 3.0 means writing and hosting a connector
yourself.

Tableau will say that a driver is needed.  The one to download is **REST API (JDBC)** - it is not a different
connector, it is the driver this one runs on.  Put the ``.jar`` in the Tableau drivers folder, which is
``/Users/<you>/Library/Tableau/Drivers`` on a Mac and ``C:\Program Files\Tableau\Drivers`` on Windows,
creating the folder if it is not there.  Then quit Tableau completely and start it again: the folder is only
read at startup, so a driver copied in while Tableau is running is still reported as missing.  Java does not
have to be installed separately.

Then, on the **General** tab of the connection dialog:

*  **REST API URL** is the data URL, for example
   ``https://<your server>/api/v2/data/<survey ident>``.
*  **Response Format** is JSON, and **JSON Path** is then ``$[*]``.  The response is a flat list of records,
   one per submission.
*  Leave **Authentication** alone.  The Basic, Bearer and OAuth options offered there do not apply to Smap -
   the key goes in a header instead.

And on the **Advanced** tab:

*  **HTTP Headers** takes ``name=value`` pairs.  Enter the key as one of them:

   .. code-block:: none

     x-api-key=smap_a_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

*  Leave **Pagination Type** turned off, for the reason given above under ``start``.

The connector is extract only, so the dashboard reads an extract rather than the server itself, and that extract
is refreshed on a schedule.

.. note::

  Tableau Cloud cannot refresh these extracts by itself.  It needs Tableau Bridge, and where Smap is installed on
  a private network Bridge has to run somewhere that can reach the Smap server.  Worth settling before the
  dashboard is built.

Static Data
-----------

You can fetch data manually using the same URLs.  You can also import data from exported spreadsheets.
