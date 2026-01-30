Whole Server
============

.. contents::
 :local:

This API provides access to the overall state of the server.  It requires SmapServer version 23.09 or later.

To access these requests you will need server owner privilege.

Lookup Survey Details (Survey Ident)
------------------------------------

.. http:get:: /api/v1/lookup/survey_ident/(text: the ident of the survey)

  :synopsis: Allows you to find out the organisation, survey name, project name, number of records and first and last date of submitted records for a survey ident.

  **Example request**:

  .. sourcecode:: http

    GET /api/v1/lookup/survey_ident/s2540_52248 HTTP/1.1
    Host: sg.smap.com.au
    Content-Type: application/json

  **Example response**:

  .. sourcecode:: http

    HTTP/1.1 200 OK
    Vary: Accept
    Content-Type: application/json

    {
      "ident": "s2540_52248",
      "displayName": "submit test",
      "projectName": "A project",
      "organisation": "Smap",
      "enterprise": "Default",
      "records": 38,
      "firstDate": "2025-06-21",
      "lastDate": "2025-10-09"
    }

Lookup Survey Details (Survey Id)
---------------------------------

.. http:get:: /api/v1/lookup/survey_id/(integer: the id of the survey)

  :synopsis: Allows you to find out the organisation, survey name and project name for a survey id. This URL returns the same data as the previous one however it accepts the integer ID rather than the survey ident as the identifier for the survey.

  **Example request**:

  .. sourcecode:: http

    GET /api/v1/lookup/survey_id/2540 HTTP/1.1
    Host: sg.smap.com.au
    Content-Type: application/json

  **Example response**:

  .. sourcecode:: http

    HTTP/1.1 200 OK
    Vary: Accept
    Content-Type: application/json

    {
      "ident": "s2540_52248",
      "displayName": "submit test",
      "projectName": "A project",
      "organisation": "Smap",
      "enterprise": "Default",
      "records": 38,
      "firstDate": "2025-06-21",
      "lastDate": "2025-10-09"
    }

Queue State
-----------

.. http:get:: /api/v1/queues/(text: queue name)

  :synopsis: The queue state API allows you to view the real-time status of the specified queue name.  This is one of:

    * s3upload
    * submissions
    * restore  (Smap Server 24.06+)

  Restore is the re-application of previous submissions initiated from the analysis module.

  **Example request**:

  .. sourcecode:: http

    GET /api/v1/queues/s3upload HTTP/1.1
    Host: sg.smap.com.au
    Content-Type: application/json

