.. _admin-server:

Server
======

.. contents::
 :local:

.. warning::

  The **server** security group is required in order to access the server management page.
  
To get to the server management screen select the **Admin** module then **Users** then select the **Server** tab.
  
.. figure::  _images/adminServer1.jpg
   :align:   center
   :alt:     Server Settings

   Server Settings

The settings in the server page are defaults that apply to all organisations be default but can ususally be overridden by the
organisation settings for a single organisation.

Mapbox Key
----------

The key for the mapbox account which provides many of the maps used by the server.  Each mapbox key is permitted a number of
free map accesses per month after which there will be a charge. (Note the Mapbox and Google keys in the above image are not 
real keys).

Google Map Key
--------------

Where google maps are used a google map key is requried.  As for Mapbox Google have a free usage threshold after which there
will be a charge.

Email Settings
--------------

Smtp Host, Email Domain, Email user name, Email password, Email Server port are all used when setting up the email server.

SMS Url
-------

This can be set to a URL that will be used to send SMS notifications.   The URL should have a placeholder for the phone 
number and the message.  

* ${phone}
* ${msg}

For example::

  https://sms.provider.com/send?user=auser&password=apassword&number=${phone}&msg=${msg}

If AWS is to be used to send the SMS messages then enter the word **aws** into this field.

SMS messages can be initiated using a notification.  Once you have specified the URL of your SMS provider here, an option of `SMS` for the target
of a notification will be selectable.  In the notification you can specify the number to be called or a question in the submitted data that
contains the number.  The message to be sent can be specified in the "content" section of the notification.  You can include items from the 
submitted data in the content by using the ${question_name} syntax.


.. warning::

  SMS messaging may result in a cost.  Hence it cannot be set up at the organisational level and can only be 
  enabled in the server settings.

API requests per minute
-----------------------

If set to 0 then there is no limit.  Otherwise this value sets the maximum number of API requests per
organisation per module per minute.  Currently the API services managed by this limit are:

*  /api/v1/data
*  /api/v1/data.csv
*  /surveyKPI/items

Minimum Password Strength
-------------------------

If set then this will specify the minimum password strength allowed on the server.  The actual strength used
will be the higher of this value and the minimum password strength of an organisation.