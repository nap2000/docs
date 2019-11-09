Audit API
=========

.. contents::
 :local:


Audit Data End Points
---------------------

.. http:get:: /api/v1/audit

  :synposis: get a list of services to retrieve audit data
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/audit
  
  .. sourcecode:: http
  
	HTTP/1.1 200 OK
	Vary: Accept
	Content-Type: application/json
	
	[
		{
			"id": 20361,
			"id_string": "s1554_20361",
			"title": "street light",
			"description": "street light",
			"url": "https://sg.smap.com.au/api/v1/audit/s1554_20361"
		}
	]
	
  :reqheader Authorization: basic
  :statuscode 200: no error

Per Question Audit Data
-----------------------

.. http:get:: /api/v1/audit/(survey ident)

  :synposis:  Get per question audit data from a survey. (survey ident) is the survey identifier which can be found in the list of services retrieved above. A GeoJson object is returned for each question and includes the time it took for the data collector to answer the question and the gps coordinates of where the question was answered. This data is only returned if "Timing Data" and "Record Location" were enabled for the survey.`
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/audit/s1554_20361

  Data is returned as GeoJSON
  
  .. sourcecode:: http
  
	HTTP/1.1 200 OK
	Vary: Accept
	Content-Type: application/json

	{
	  "type": "FeatureCollection",
	  "features": [
		{
		  "type": "Feature",
		  "properties": {
			"question": "occupation",
			"value": "Builder",
			"time_spent": 8404,
			"prikey": 1,
			"user": "neil",
			"start": "2019-11-09 09:24:07.837+00",
			"end": "2019-11-09 09:24:37.296+00",
			"device": "863914040631978"
		  },
		  "geometry": {
			"type": "Point",
			"coordinates": [
			  153.0120208,
			  -27.4465832
			]
		  }
		},
		{
		  "type": "Feature",
		  "properties": {
			"question": "name",
			"value": "Bob",
			"time_spent": 11493,
			"prikey": 1,
			"user": "neil",
			"start": "2019-11-09 09:24:07.837+00",
			"end": "2019-11-09 09:24:37.296+00",
			"device": "863914040631978"
		  },
		  "geometry": {
			"type": "Point",
			"coordinates": [
			  153.0120208,
			  -27.4465832
			]
		  }
		},
		{
		  "type": "Feature",
		  "properties": {
			"question": "age",
			"value": "25",
			"time_spent": 6310,
			"prikey": 1,
			"user": "neil",
			"start": "2019-11-09 09:24:07.837+00",
			"end": "2019-11-09 09:24:37.296+00",
			"device": "863914040631978"
		  },
		  "geometry": {
			"type": "Point",
			"coordinates": [
			  153.0120208,
			  -27.4465832
			]
		  }
		}
	  ]
	}

  :reqheader Authorization: basic
  :statuscode 200: no error

