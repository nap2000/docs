Mailout
=======

.. contents::
 :local:

.. _get-mailouts:

Get Mailouts
------------

.. http:get:: /api/v1/mailout/(survey ident) 

  :synopsis: Returns the mailouts that use the specified survey
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/mailout/s17_119
  
  .. sourcecode:: http
  
	HTTP/1.1 200 OK
	Vary: Accept
	Content-Type: application/json
	
        [
          {
            "id": 7,
            "survey_ident": "s17_119",
            "name": "A Mailout",
            "subject": "Survey on Attitudes",
            "content": "Dear ${name},\n\nThe form can be accessed from the following link: ${url}.  Thankyou for taking part.\n\nRegards\n\nSally"
          }
        ]
	
  :query boolean links: Return links to other mailout related data.
  :reqheader Authorization: basic
  :statuscode 200: no error

Get Mailout Emails
------------------

.. http:get:: /api/v1/mailout/(mailout id)/emails 

  :synopsis: Returns the emails that are included in the specified mailout id. Mailout Ids can be found with the api call :ref:`get-mailouts`
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/mailout/1/emails
  
  .. sourcecode:: http
  
	HTTP/1.1 200 OK
	Vary: Accept
	Content-Type: application/json
	
        [
          {
            "id": 13,
            "email": "neilpenman@gmail.com",
            "name": "Neil",
            "status": "new",
            "status_loc": "New",
            "status_details": "",
            "initialData": {
              "values": {
                "q2": "Initial text",
                "q3": "More initial text"
              }
            }
          },
          {
            "id": 14,
            "email": "neilpenman@smap.com.au",
            "name": "Neil The Smap One",
            "status": "new",
            "status_loc": "New",
            "status_details": "",
            "initialData": {
              "values": {
                "q2": "Apples",
                "q3": "Oranges"
              }
            }
          }
        ]
	
  :reqheader Authorization: basic
  :statuscode 200: no error

Get Email Totals
----------------

.. http:get:: /api/v1/mailout/(mailout id)/emails/totals 

  :synopsis: Returns the counts of how many emails are in each valid state
  
  **Example response**:
  
  https://sg.smap.com.au/api/v1/mailout/1/emails/totals
  
  .. sourcecode:: http
  
	HTTP/1.1 200 OK
	Vary: Accept
	Content-Type: application/json
	
        {
          "total": 0,
          "complete": 0,
          "unsent": 2,
          "error": 0,
          "unsubscribed": 0,
          "pending": 0,
          "sent": 0,
          "expired": 0
        }

  :reqheader Authorization: basic
  :statuscode 200: no error

Create/Edit a Mailout
---------------------
	
.. http:post:: /api/v1/mailout

  :synposis: To edit an existing mailout the payload is a JSON object with the same attributes as returned by :ref:`get-mailouts`.  To create a new mailout remove the mailout id. The payload is sent as x-www-form-urlencoded content with a key of "mailout".  

  **Example request**:

  .. sourcecode:: http

    HTTP/1.1 200 OK
    Vary: Accept
    Content-Type: application/x-www-form-urlencoded

    mailout = {
       "survey_ident": s17_119,
       "name": "Here is a new mailout",
       "subject": "Mailout on Program Approach",
       "content": "Dear ${name},\n\nPlease complete\n\nRegards Karen"
    }		   
  

  **Example Response:**

     Details on the mailout created are returned.  This will be the same as the passed in details except the `id` of the mailout will be added

     .. sourcecode:: http

       HTTP/1.1 200 OK
       Vary: Accept
       Content-Type: application/json

       {
         "id": 12,
         "survey_ident": s17_119,
         "name": "Here is a new mailout",
         "subject": "Mailout on Program Approach",
         "content": "Dear ${name},\n\nPlease complete\n\nRegards Karen"
       }		   

