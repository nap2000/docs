Log API
=======

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

