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


.. _data-api-json:

Data End Points in JSON
-----------------------

.. http:get:: /api/v1/data

  :synposis: Returns available end points.   
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/data
  
  .. sourcecode:: http
  
	HTTP/1.1 200 OK
	Vary: Accept
	Content-Type: application/json
	
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

Data End Points in CSV
----------------------

.. http:get:: /api/v1/data.csv

  :synposis: Returns available end points in a CSV file.
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/data.csv

  :query filename: The name of the file. Default is ``forms.csv``.

.. _survey-data-json:

Survey Data in JSON
-------------------

.. http:get:: /api/v1/data/(survey ident)

  :synposis: Returns data for the specified survey. The example shows 
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/data/s193_18568?links=true

  .. sourcecode:: http
  
	HTTP/1.1 200 OK
	Vary: Accept
	Content-Type: application/json
	
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


  :query links: Return URL links to other API calls on the data
  :query start: Retrieve data starting from the specified key
  :query limit: The number of records to retrieve
  :query form: Retrieve data for a sub-form.  The available subforms are shown in the returned data from the /api/v1/data call.
		This call will return the key for the parent form in the "parkey" attribute so that its data can be combined with that of
		the main form.
  :query start_parkey: Parent key to start from.  Only useful when working with subform data.
  :query parkey: Parent key.  return records in the subform that belong to the specified parent.
  :query bad: One of ``yes`` return deleted records, ``only`` Only return deleted records, ``none`` do not return deleted (default)
  :query audit: set to ``yes`` to return audit data. This data is the time in milliseconds that the user took to answer each question. 
		You can also specify in the settings for the form that the GPS coordinates where each question was answered should be included. 
		There is a thid level of audit where every change made to a question during the course of an interview is recorded. 
		This information is available through the separate audit API.
  :query meta: set to ``yes`` to return meta data and preloads including prikey, instanceid, user, upload time.  Set to ``no`` to
        not return this data. The default is ``yes``
  :query merge_select_multiple: Set to ``yes`` to combine all the selected choices for a select multiple into a single column / Json 
		text property.
  :query sort: 	question name to sort on
  :query dirn: 	Sort direction, either ``asc`` or ``desc``
  :query key: 	The key to filter by.  A key will need to have been specified for this survey.
  :query tz:    The timezone for example ``Australia/Brisbane``.  All date time and date answers will be returned in this time zone.
  :query geom_question: When using geojson=yes, and if you have more than one geometry in the main form, then you can specify the 
                name of the geometry question to use as the GeoJson geometry here.
  :query filter: Advanced filter.  For example  &filter=${q1} > 10
  :reqheader Authorization: basic
  :statuscode 200: no error
  :statuscode 401: not authorised

Survey Data in CSV
------------------

.. http:get:: /api/v1/data.csv/(survey ident)

  :synposis: Returns data for the specified survey. The example shows 
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/data.csv/s193_18568?links=true

  All parameters in :ref:`survey-data-json` can be used.
  
  :query filename: The name of the file. Default is ``data.csv``.

Single Record
-------------

.. http:get:: /api/v1/data/(survey ident)/(instance key)

  :synposis: Get data for the specified instance. The instance key can be found in the :ref:`survey-data-json` API call.
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/data/s1313_16851/uuid:dce538eb-ea90-44f1-b022-7481fad8fe47

  .. sourcecode:: http
  
	HTTP/1.1 200 OK
	Vary: Accept
	Content-Type: application/json
	
	{
	"values": {
	"q1": "Joe",
	"q2": "23",
	"q3": "https://sg.smap.com.au/attachments/s193_1778/82c362f4-8ce5-4fe2-a915-5e3cd2f8ff1c.jpg",
	"instanceid": "uuid:832ed325-4ad3-46b0-9f99-7d1ebda1cdad"
	}
	}

  :query meta: set to ``yes`` to return meta data and preloads including prikey, instanceid, user, upload time.  The default is ``no``
  :query tz:    The timezone for example ``Australia/Brisbane``.  All date time and date answers will be returned in this time zone.
  :reqheader Authorization: basic
  :statuscode 200: no error
  :statuscode 401: not authorised
  :statuscode 404: not found

