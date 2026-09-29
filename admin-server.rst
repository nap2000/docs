.. _admin-server:

Server
======

.. contents::
  :local:

.. warning::

  The **server owner** security group is required in order to change server settings.

Server wide settings are on the **Server** tab of the settings page.  To open it select **Admin**, then **Settings**, and then
the **Server** tab.  Each setting is described in :ref:`server-settings`.

The settings on the server tab are defaults that apply to all organisations, but many of them can be overridden in an individual
organisation's settings.

This page adds some details that are not covered on the settings page.

The server owner security group
-------------------------------

This security group indicates that the user owns the server and can therefore change server-wide settings or monitor
server-level events. You cannot set this security group through the user interface. Instead, run SQL directly:

#. Connect to the ``survey_definitions`` database.
#. Get the user ID for the user who should have server administration rights:

   .. code-block:: sql

      select id from users where ident = '{user_ident}';

   Replace ``{user_ident}`` with the user's ident.

#. Update the ``user_group`` table. The numeric identifier of the owner security group is ``9``:

   .. code-block:: sql

      insert into user_group (u_id, g_id) values (123, 9);

   Replace ``123`` with the user ID from the previous step.

SMS Url
-------

The URL used to send SMS notifications should include placeholders for the phone number and message.

* ${phone}
* ${msg}

For example::

  https://sms.provider.com/send?user=auser&password=apassword&number=${phone}&msg=${msg}

If AWS is used to send SMS messages, enter **aws** in this field.

Once the SMS URL is set, ``SMS`` becomes available as a notification target. In the notification, you can specify the
destination number directly or provide a question in submitted data that contains the number. Define the message text in the
notification ``content`` section. You can insert submitted data values using ``${question_name}``.

.. warning::

  SMS messaging may result in a cost. Therefore it cannot be set up at the organisational level and can only be
  enabled in the server settings.

API requests per minute
-----------------------

If set to 0, there is no limit. Otherwise, this value sets the maximum number of API requests per organisation,
per module, per minute. The API services currently managed by this limit are:

*  /api/v1/data
*  /api/v1/data.csv
*  /api/v2/data
*  /api/v2/data.csv
*  /surveyKPI/items

Minimum Password Strength
-------------------------

The enforced strength is the higher of the server value and the organisation-level minimum password strength.  See
:ref:`password-strength`.
