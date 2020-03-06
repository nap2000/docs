People
======

.. contents::
 :local:


.. http:get:: /api/v1/subscriptions

  :synopsis: get subscribed users
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/subscriptions
  
  .. sourcecode:: http
  
        HTTP/1.1 200 OK
        Vary: Accept
        Content-Type: application/json
	
        [
          {
            "id": 511,
            "email": "tom@x.com",
            "name": "Tom Smith",
            "status": "subscribed",
          },
          {
            "id": 510,
            "email": "sally@x.com",
            "name": "Sally",
            "status": "pending",
          }
        ]
	
  :reqheader Authorization: basic
  :statuscode 200: no error

