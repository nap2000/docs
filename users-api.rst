Users API
=========

.. contents::
 :local:


User Locations
--------------

.. http:get:: /api/v1/users/locations

  :synopsis: Returns the locations of users when they last refreshed fieldTask
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/users/locations
  
  .. sourcecode:: http
  
	HTTP/1.1 200 OK
	Vary: Accept
	Content-Type: application/json
	
	{
	  "type": "FeatureCollection",
	  "features": [
	    {
	      "type": "Feature",
	      "geometry": {
	        "type": "Point",
	        "coordinates": [
	          153.0110065,
	          -27.4457921
	        ]
	      },
	      "properties": {
	        "prikey": "1",
	        "User": "neil",
	        "Refresh Time": "2020-01-11 21:47:18.783563"
	      }
	    }
	  ],
	  "message": ""
	}
	
  :query tz: Timezone
  :reqheader Authorization: basic
  :statuscode 200: no error

