Whole Server
============

.. contents::
 :local:

This API provides access to the overall state of the server.  It requires SmapServer version 23.09 or later.

To access these requests you will need server owner privilege.

Lookup Survey Details
---------------------

.. http:get:: /api/v1/lookup/survey_ident/(text: the ident of the survey)

  :synposis: Allows you to find out the organisation, survey name and project name for a survey ident that might me shown in a log.

  **Example request**:

  .. sourcecode:: http

    GET /api/v1/lookup/survey_ident/s2540_52248 HTTP/1.1
    Host: sg.smap.com.au
    Content-Type: application/json

Queue State
-----------

.. http:get:: /api/v1/lookup/(text: queue name)

  :synposis: The queue state API allows you to view the real time status of the specified queue name.  This is one of:

    * s3upload
    * submissions

  **Example request**:

  .. sourcecode:: http

    GET /api/v1/queues/s3upload HTTP/1.1
    Host: sg.smap.com.au
    Content-Type: application/json


