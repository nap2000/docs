Data API
========

.. contents::
 :local:

Introduction
------------

This API is based on the Kobo Version 1 API however it has had some significant extensions.  To use the examples you will need to enter
a user id and password.  If you are already logged on to the server then you should see your own data otherwise you can access demo data using::

  user: api
  password: api

Multiple Records
----------------

.. http:get:: /api/v1/data

  :synposis: Returns available end points.   For each url in the response ``data`` can be replaced with ``data.csv`` 
	to return the data
	in a CSV file.
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/data
  
  .. sourcecode:: http
  
	HTTP/1.1 200 OK
	Vary: Accept
	Content-Type: text/javascript
	
	[
	  {
	  "id": 1778,
	  "id_string": "s193_1778",
		"title": "Basic Form",
		"description": "Basic Form",
		"url": "https://sg.smap.com.au/api/v1/data/s193_1778?links=true"
		},
		{
		"id": 18569,
		"id_string": "s193_18569",
		"title": "Form with audit data",
		"description": "Form with audit data",
		"url": "https://sg.smap.com.au/api/v1/data/s193_18569?links=true"
		},
		{
		"id": 18568,
		"id_string": "s193_18568",
		"title": "Form with repeats",
		"description": "Form with repeats",
		"url": "https://sg.smap.com.au/api/v1/data/s193_18568?links=true",
		"subforms": {
		"q2": "https://sg.smap.com.au/api/v1/data/s193_18568?form=q2"
		}
		},
		{
		"id": 18502,
		"id_string": "s193_18502",
		"title": "القراءة بحسب الباركود",
		"description": "القراءة بحسب الباركود",
		"url": "https://sg.smap.com.au/api/v1/data/s193_18502?links=true"
		}
	]
	
  :reqheader Authorization: basic
  :statuscode 200: no error
	
.. http:get:: /api/v1/data(survey ident)

  :synposis: Returns data for the specified survey. The example shows 
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/data/s193_18568?links=true

  .. sourcecode:: http
  
	HTTP/1.1 200 OK
	Vary: Accept
	Content-Type: text/javascript
	
	[
		{
		"prikey": "1",
		"Key": "",
		"Survey Duration": "27.7929999999999993",
		"User": "api",
		"Upload Time": "2019-09-01 06:26:18+00",
		"Survey Name": "Form with repeats",
		"_scheduled_start": "",
		"Version": "2",
		"Complete": "t",
		"Survey Notes": "",
		"Location Trigger": "",
		"Instance Name": "",
		"start": "2019-09-01 06:25:50+00",
		"end": "2019-09-01 06:26:17+00",
		"deviceid": "deviceid not found",
		"uuid": "uuid:7d2b9a69-0cad-4e0c-8dd5-cb3e3c14eb14",
		"name": "Tom",
		"links": {
		"data": "https://sg.smap.com.au/api/v1/data/s193_18568/uuid:7d2b9a69-0cad-4e0c-8dd5-cb3e3c14eb14",
		"pdf": "https://sg.smap.com.au/surveyKPI/pdf/s193_18568?instance=uuid:7d2b9a69-0cad-4e0c-8dd5-cb3e3c14eb14&tz=UTC",
		"webform": "https://sg.smap.com.au/webForm/s193_18568?datakey=instanceid&datakeyvalue=uuid:7d2b9a69-0cad-4e0c-8dd5-cb3e3c14eb14",
		"audit_log": "https://sg.smap.com.au/api/v1/audit/log/s193_18568/uuid:7d2b9a69-0cad-4e0c-8dd5-cb3e3c14eb14"
		}
		},
		{
		"prikey": "2",
		"Key": "",
		"Survey Duration": "15.5079999999999991",
		"User": "api",
		"Upload Time": "2019-09-01 06:26:33+00",
		"Survey Name": "Form with repeats",
		"_scheduled_start": "",
		"Version": "2",
		"Complete": "t",
		"Survey Notes": "",
		"Location Trigger": "",
		"Instance Name": "",
		"start": "2019-09-01 06:26:17+00",
		"end": "2019-09-01 06:26:33+00",
		"deviceid": "deviceid not found",
		"uuid": "uuid:8bf658ad-33ab-4cfe-97c9-fad91406fb86",
		"name": "Sally",
		"links": {
		"data": "https://sg.smap.com.au/api/v1/data/s193_18568/uuid:8bf658ad-33ab-4cfe-97c9-fad91406fb86",
		"pdf": "https://sg.smap.com.au/surveyKPI/pdf/s193_18568?instance=uuid:8bf658ad-33ab-4cfe-97c9-fad91406fb86&tz=UTC",
		"webform": "https://sg.smap.com.au/webForm/s193_18568?datakey=instanceid&datakeyvalue=uuid:8bf658ad-33ab-4cfe-97c9-fad91406fb86",
		"audit_log": "https://sg.smap.com.au/api/v1/audit/log/s193_18568/uuid:8bf658ad-33ab-4cfe-97c9-fad91406fb86"
		}
		}
	]
	
  :query start: Retrieve data starting from the specified key
  :query limit: The number of records to retrieve
  :query form: Retrieve data for a sub-form.  The available subforms are shown in the returned data from the /api/v1/data call.
		This call will return the key for the parent form in the "parkey" attribute so that its data can be combined with that of
		the main form.
  :query start_parkey: Parent key to start from.  Only useful when working with subform data.
  :query bad: One of ``yes`` return deleted records, ``only`` Only return deleted records, ``none`` do not return deleted (default)
  :query audit: set to ``yes`` to return audit data. This data is the time in milliseconds that the user took to answer each question. 
		You can also specify in the settings for the form that the GPS coordinates where each question was answered should be included. 
		There is a thid level of audit where every change made to a question during the course of an interview is recorded. 
		This information is available through the separate audit API.
  :query merge_select_multiple: Set to ``yes`` to combine all the selected choices for a select multiple into a single column / Json 
		text property.
  :query geojson: 	Set to ``yes`` for the data to be returned in geoJson format rather than the kobo api format.
  :reqheader Authorization: basic
  :statuscode 200: no error
  :statuscode 404: not authorised

