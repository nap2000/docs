.. _apis:

Server APIs
===========

The APIs consist of REST web services, although they are not a strict REST implementation.   Most return JSON or GeoJson.  Many also accept
a query parameter of links=true.  This allows the API calls to be browsed from web browser, especially if you have a JSON formatter installed. A good place
to start would be  `https://sg.smap.com.au/api/v1/admin/projects?links=true <https://sg.smap.com.au/api/v1/admin/projects?links=true>`_
This will return the projects that you have access to and links to get more data  related to each project.

Using POST
----------

When sending data to the server using a POST request:

*  Set the "Content-Type" in the header to "application/x-www-form-urlencoded"
*  Set the body of the request to be "x-www-form-urlencoded"

.. toctree::
  :maxdepth: 1
  
  data-api.rst
  admin-api.rst
  audit-api.rst
  tasks-api.rst
  users-api.rst
  log-api.rst
  contacts-api.rst
  campaign-api.rst
