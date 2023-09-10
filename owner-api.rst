Whole Server
============

.. contents::
 :local:

This API provides access to the overall state of the server.  It requires SmapServer version 23.09 or later.

Queue State
-----------

.. http:get:: /api/v1/queues/(text: queue name)

  :synposis: The queue state API allows you to view the real time status of the specified queue name.  This is one of 's3upload' or 'submissions'
  **Example request**:

  .. sourcecode:: http

    GET /api/v1/queues/s3upload HTTP/1.1
    Host: sg.smap.com.au
    Content-Type: application/json


