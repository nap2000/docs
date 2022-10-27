Log
===

.. contents::
 :local:


.. http:get:: /api/v1/log

  :synopsis: get application log entries
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/log
  
  .. sourcecode:: http
  
        HTTP/1.1 200 OK
        Vary: Accept
        Content-Type: application/json
	
        [
          {
            "id": 511,
            "log_time": "2020-02-09 22:43:39",
            "sId": 0,
            "sName": "",
            "userIdent": "",
            "event": "optin",
            "note": "x@a.com has un-subscribed from email notifications"
          },
          {
            "id": 510,
            "log_time": "2020-02-09 22:40:14",
            "sId": 0,
            "sName": "",
            "userIdent": "",
            "event": "optin",
            "note": "Opt in email sent to \"y@zarkman.com\""
          }
        ]
	
  :query start: The id of the first record to retrieve
  :query limit: The number of log items to retrieve
  :query sort:  The column name to sort on. One of `id`, `log_time`, `sId`, `sName`, `userIdent`, `event`, `note`
  :query dirn: The direction of sort.  One of `asc` or `desc`
  :reqheader Authorization: basic
  :statuscode 200: no error

.. http:get:: /api/v1/log/organisation/{year}/{month}

  :synopsis: get the number of events per organisation for a month
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/log/organisation/2020/07
  
  .. sourcecode:: http
  
        HTTP/1.1 200 OK
        Vary: Accept
        Content-Type: application/json
	
        [
            {
                "organisation": "Smap",
                "events": {
                    "API view": 224,
                    "erase": 38,
                    "create": 42,
                    "Update": 81,
                    "delete": 56,
                    "email": 34
                }
            }
        ]

  :query tz:    The timezone for example ``Australia/Brisbane``.  All date time and date answers will be returned in this time zone.
  :reqheader Authorization: basic
  :statuscode 200: no error

.. http:get:: /api/v1/log/organisation/{year}/{month}/{day}

  :synopsis: get the number of events per organisation for a day
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/log/organisation/2020/07/04
  
  .. sourcecode:: http
  
        HTTP/1.1 200 OK
        Vary: Accept
        Content-Type: application/json
	
        [
            {
                "organisation": "Smap",
                "events": {
                    "API view": 104,
                    "erase": 3,
                    "create": 2,
                    "Update": 1,
                    "delete": 2,
                    "email": 1
                }
            }
        ]

  :query tz:    The timezone for example ``Australia/Brisbane``.  All date time and date answers will be returned in this time zone.
  :reqheader Authorization: basic
  :statuscode 200: no error

.. http:get:: /api/v1/log/hourly/{year}/{month}/{day}

  :synopsis: get a count of log events over each hour of a specific day
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/log/hourly/2020/07/04
  
  .. sourcecode:: http
  
        HTTP/1.1 200 OK
        Vary: Accept
        Content-Type: application/json
	
        [
            {
                "hour": 10,
                "events": {
                    "erase": 2
                }
            },
            {
                "hour": 15,
                "events": {
                    "API view": 1,
                    "erase": 1,
                    "delete": 2
                }
            }
        ]	

  :query tz:    The timezone for example ``Australia/Brisbane``.  All date time and date answers will be returned in this time zone.
  :reqheader Authorization: basic
  :statuscode 200: no error

