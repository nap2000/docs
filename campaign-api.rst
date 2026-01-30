Campaigns
=========

.. contents::
 :local:

.. _get-mailouts:

Get Campaigns
-------------

.. http:get:: /api/v1/mailout/(survey ident) 

  :synopsis: Returns the mailouts that use the specified survey. A list of surveys can be found using :ref:`surveys-api`.
  
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
            "content": "Dear ${name},\n\nThe form can be accessed from the following link: ${url}. Thank you for taking part.\n\nRegards\n\nSally",
            "multiple_submit": false
          }
        ]
	
  :query boolean links: Return links to other mailout related data.
  :reqheader Authorization: basic
  :statuscode 200: no error

.. _get-campaign-emails:

Get Campaign Emails
-------------------

.. http:get:: /api/v1/mailout/(mailout id)/emails 

  :synopsis: Returns the emails that are included in the specified mailout id. Mailout IDs can be found with the api call :ref:`get-mailouts`
  
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

Create/Edit a Campaign
----------------------

.. http:post:: /api/v1/mailout

  :synopsis: To edit an existing mailout the payload is a JSON object with the same attributes as returned by :ref:`get-mailouts`.  To create a new mailout remove the mailout id. The payload is sent as x-www-form-urlencoded content with a key of "mailout".

  **Example request**:

  .. sourcecode:: http

    POST /api/v1/mailout HTTP/1.1
    Content-Type: application/x-www-form-urlencoded

    mailout = {
       "survey_ident": "s17_119",
       "name": "Here is a new mailout",
       "subject": "Mailout on Program Approach",
       "content": "Dear ${name},\n\nPlease complete\n\nRegards Karen",
       "multiple_submit": true
    }
  

  **Example response:**

     Details on the mailout created are returned.  This will be the same as the passed in details except the `id` of the mailout will be added

     .. sourcecode:: http

       HTTP/1.1 200 OK
       Vary: Accept
       Content-Type: application/json

       {
         "id": 12,
         "survey_ident": "s17_119",
         "name": "Here is a new mailout",
         "subject": "Mailout on Program Approach",
         "content": "Dear ${name},\n\nPlease complete\n\nRegards Karen"
       }


Create a Campaign Email
-----------------------

.. http:post:: /api/v1/mailout/(campaign id)/email

  :synopsis: The payload is a JSON object with the same attributes as returned by :ref:`get-campaign-emails`.  The payload is sent as x-www-form-urlencoded content with a key of "email". Optionally a second payload item with a key of **action** and values of either "email", "manual" or "none" can be included.  If the action is set to email then an email is sent immediately. Alternatively if the action is set to "manual" the URL to complete the form will be returned.  If the **action** is not set, or is set to "none", then the email is added to the campaign to be sent by a user using the user interface.

  **Example request**:

   .. sourcecode:: http

     POST /api/v1/mailout/1/email HTTP/1.1
     Content-Type: application/x-www-form-urlencoded

     email = {
       "email": "neilpenman@gmail.com",
       "name": "Neil",
       "initialData": {
         "values": {
           "street": "Collins Street"
          }
       }
     }

     action=manual
  

  **Example response:**

     Where the action is "manual" details on the campaign email will be returned. Otherwise an empty JSON object will be returned

     .. sourcecode:: http

       HTTP/1.1 200 OK
       Vary: Accept
       Content-Type: application/json

       {
         "id": 22,
         "email": "neilpenmanx@gmail.com",
         "name": "Neil",
         "url": "https://ubuntu1804.smap.com.au/webForm/action/u5c7d9fae-4e12-47a0-bf09-c1fb273faa20",
         "initialData": {
           "values": {
             "street": "Collins Street"
             }
          }
       }

Initial data for surveys with repeating groups can be posted using the format::

    class Instance {
	public HashMap<String, String> values = new HashMap<>();	 	
        public HashMap<String, ArrayList<Instance>> repeats;	
    }
    
    In the following example the survey has a top level form with question q1. Then a subform called "q2"
    with question "q2.1".

     .. sourcecode:: http

       HTTP/1.1 200 OK
       Vary: Accept
       Content-Type: application/json

    {
        "email": "neilpenman@gmail.com",
        "name": "Tom",
        "initialData": { 
            "values": { 
              "q1": "panda" 
            }, 
            repeats: { 
              "q2": [
                { 
                   "values": { 
                      "q2.1": "bear" 
                   } 
                }
              ] 
            } 
        }
    }
