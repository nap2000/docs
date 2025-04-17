Whole Server
============

.. contents::
 :local:

This API provides access to the overall state of the server.  It requires SmapServer version 23.09 or later.

To access these requests you will need server owner privilege.

Lookup Survey Details (Survey Ident)
------------------------------------

.. http:get:: /api/v1/lookup/survey_ident/(text: the ident of the survey)

  :synopsis: Allows you to find out the organisation, survey name and project name for a survey ident that might be shown in a log.

  **Example request**:

  .. sourcecode:: http

    GET /api/v1/lookup/survey_ident/s2540_52248 HTTP/1.1
    Host: sg.smap.com.au
    Content-Type: application/json

Lookup Survey Details (Survey Id)
------------------------------------

.. http:get:: /api/v1/lookup/survey_id/(integer: the id of the survey)

  :synopsis: Allows you to find out the organisation, survey name and project name for a survey id that might be shown in a log. This URL returns the same data as the previous one however it accepts the integer ID rather than the text Ident as the identifier for the survey.

  **Example request**:

  .. sourcecode:: http

    GET /api/v1/lookup/survey_ident/s2540_52248 HTTP/1.1
    Host: sg.smap.com.au
    Content-Type: application/json

Queue State
-----------

.. http:get:: /api/v1/queues/(text: queue name)

  :synopsis: The queue state API allows you to view the real time status of the specified queue name.  This is one of:

    * s3upload
    * submissions
    * restore  (Smap Server 24.06+)

restore is the re-application of previous submissions initiated from the analysis module.

  **Example request**:

  .. sourcecode:: http

    GET /api/v1/queues/s3upload HTTP/1.1
    Host: sg.smap.com.au
    Content-Type: application/json


