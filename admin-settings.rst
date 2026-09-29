Settings
========

.. contents::
 :local:

The settings page can be accessed from the **Admin** module.  It has multiple tabs that allow you to configure
various parts of the system.  Apart from the **Server** tab, the settings apply to the organisation that you are
currently in.  Some tabs are only shown to users with a particular security group:

*  **Server**. Server owner.
*  **Organisation**. Organisational administrator.
*  **Operations**. Administrator.
*  **Sensitive Data**. Security manager.

.. figure::  _images/settings.jpg
   :align:   center
   :alt:     The tabs available on the settings page
   
   Settings Tabs
   
.. note::

  Each survey also has **Settings** which can be specified in the online editor or the settings tab of an XLSForm. 
  Documentation on these can be found here, :ref:`settings-reference`.

Appearance
----------

From here you can set the appearance of server pages for the current organisation.  Each organisation can have
its own appearance.

You can:

*  Set an image to appear on the home page
*  Set the background colour of the menu bar
*  Set the text colour of the menu bar (New in version 21.01)
*  Set a custom style sheet to customise buttons, fonts etc

Custom Style Sheet
++++++++++++++++++

The Smap server from version 21.01 uses Bootstrap version 4.5.  The buttons and other elements of the pages
are styled using the default Bootstrap style sheet.  However you can upload your own CSS file that will override
these styles.

To add a customised stylesheet:

*  In the appearance tab click on "Upload a CSS style sheet"
*  Click on "Select a style sheet" and select the file you just uploaded
*  Click "Save"

.. _server-settings:

Server
------

The server tab is only shown to users who have the server owner group. It can be used to set parameters for the entire server.

Map services
++++++++++++

*  Mapbox key. This key can be obtained from https://mapbox.com and allows you to use maps from Mapbox as backgrounds.
*  Google maps key. A key can be obtained from https://developers.google.com and entered here. It allows you to use maps and satellite images from Google.
*  MapTiler key. A key can be obtained from https://www.maptiler.com and entered here.

Messaging
+++++++++

Messaging settings are grouped by channel.  Leave a group blank if you do not use that channel.  Secrets are masked once
they have been saved.

**Vonage - SMS and WhatsApp**.  Send and receive SMS and WhatsApp messages through Vonage.  See :ref:`sms-server-admin`.

*  Vonage application ID.
*  Vonage webhook secret.

**WhatsApp - Meta Cloud API**.  Connect WhatsApp directly to Meta without Vonage.  When the access token is set, WhatsApp
messages are sent this way instead of through Vonage.  Requires Smap Server version 26.10+.  See :ref:`whatsapp-meta`.

*  WhatsApp Access Token.
*  WhatsApp App Secret.  Used to check that inbound messages came from Meta.
*  WhatsApp Webhook Verify Token.  Any value you choose.  Enter the same value in Meta when you set up the webhook.
*  API Version.  The Meta Graph API version.  Defaults to v21.0 if left blank.

**SMS URL**.  URL of a service to send SMS notifications, or just "aws" if the AWS SMS service is to be used.

Email Server
++++++++++++

*  Email type. Select SMTP or AWS SES.
*  AWS region (AWS SES).
*  SMTP host.
*  Email domain.
*  Email user name.
*  Email password.
*  Email server port.

Load management
+++++++++++++++

*  Maximum number of API requests per minute.
*  Maximum API records per request.

.. note::

    Changes to these values can take up to a minute to take effect

Security
++++++++

*  Minimum password strength.
*  Require security manager privilege to delete data.  When set, only users with the security manager group can
   delete all the data for a survey or restore it, see :ref:`delete-restore`.  Deleting individual records is not affected.
*  Turnstile Site Key
*  Turnstile Secret Key

If you specify the Turnstile keys and add your server domain to the domains protected by your Cloudflare account then Turnstile protection can be added
to a public form.  You will still need to specify the use of Turnstile in the form settings. This feature is available in version 26.03.09+.
Turnstile provides protection against automated bots completing your public surveys
and works in a similar way to CAPTCHA.

SharePoint
++++++++++

Requires SmapServer v26.05.01.  The connection used to write submissions to SharePoint lists and to read SharePoint
lists as shared reference data.

*  SharePoint URL.
*  Authentication Type.  S2S High-Trust (on-premises) or Windows (NTLM).
*  Client ID, Realm and Private Key (PEM).  For S2S High-Trust.  The **Discover** button finds the realm.
*  Windows Domain, Username and Password.  For Windows (NTLM).

See :ref:`sharepoint-server-config` for how to set these up.

Server custom style sheet
+++++++++++++++++++++++++

This section sets a server wide custom style sheet. The approach is identical to that for the per organisation style sheet described in the appearance tab.

.. _organisation-admin-settings:

Organisation
------------

Requires SmapServer v26.10+.  In earlier versions these settings are in the organisation dialog on the
**Organisations** tab of the users page.

The organisation tab is only shown to users who have the organisational administrator group.  These settings apply
to the organisation that you are currently in and cannot be changed by an administrator who does not also have
the organisational administrator group.  To change them for a different organisation, first move to that
organisation.

Access
++++++

These settings control what the organisation is allowed to do.  If any of the "allow" settings are changed then an
email is sent to the help email address set in the :ref:`email-settings` tab.

*  Allow submissions. Allow data to be submitted to this organisation.
*  Allow API access.
*  Allow notifications.
*  Allow sending of task emails.
*  Allow SMS. Allow SMS messages to be sent in notifications.  Only shown if the server uses AWS to send SMS messages.
*  Analysis auto refresh interval.  The interval in minutes at which charts and maps on the analysis dashboard are
   refreshed.  Setting a value of zero disables automatic refresh.

Monthly usage limits
++++++++++++++++++++

Limits on the use of chargeable services each month.  The current usage for the month is shown next to each limit.

*  AWS Translate. Letters translated.
*  AWS Transcribe. Seconds of audio transcribed.
*  AWS Transcribe Medical. Seconds of audio transcribed.
*  AWS Rekognition. Images analysed.
*  AWS Comprehend. Sentiment analysis requests.
*  Submissions. A limit of zero means submissions are unlimited.

.. _mobile-device-settings:

Mobile App Options
------------------

This tab allows setting of options for FieldTask. When the user presses refresh on FieldTask these settings will be applied on their device. Many
of these settings include the option "set on phone" as they can also be set by the phone user. However if another setting is selected then the
on-phone setting will be overridden. These settings apply to all FieldTask instances logged on as a user in the current organisation.

Security
++++++++

*  Force the use of tokens for logon. Requires FieldTask to use the server-issued token rather than a stored password.
*  Password policy. How often the user needs to re-logon. By default the enumerator never has to logon to FieldTask. In this case as long as valid
   credentials have already been entered they can continue to use the device without knowing what those credentials are. Using this setting you can
   override that default behaviour and require the user to logon every time they use FieldTask. You can also require periodic logons, in which case
   set the **Number of days before password expiry**.
*  Disable exit menu. Hides the menu used to exit FieldTask and the tracking controls.
*  Prevent background audio from being disabled. Stops users turning off background audio recording on the device.

Offline Maps
++++++++++++

*  Manage offline map layers on the server. When set, FieldTask downloads the offline map layers belonging to the projects a
   user has access to (:ref:`offline-maps`). The user chooses which of those layers is displayed, and cannot delete one that
   came from the server, but they can still add their own layers on the phone. This setting applies to every user in the
   organisation, so leaving the manual option available means someone who needs a layer larger than the 500 MB upload limit
   is not blocked.

Menus
+++++

The device must be restarted to see changes to these options.

*  Enable ODK style menus to delete, submit, edit and get new forms. Usually a FieldTask user will just use the menu option "refresh". However you can
   also enable the ODK style menus where downloading forms, uploading results etc are separate menu options.
*  Enable ODK Admin menu. The FieldTask admin menu is generally not used. Instead set admin values on the server as described here. However you can
   enable the on device admin menu if you wish.
*  Enable server settings menu. The menu to change the server can be disabled with this setting.
*  Enable user and identity menu. The menu to set user identity can be disabled with this setting.

Form Completion
+++++++++++++++

*  Allow finalised forms to be opened for review. If set the user will be able to view completed surveys in read only mode and add comments. They will not
   be able to change the answers to any questions.
*  Allow user to mark forms as not finalized. If enabled then a checkbox labelled **Mark form as finalized**, will be shown when the enumerator finishes a
   survey and gets to the `save` screen. By default this will always be checked. If the enumerator unchecks this option then the survey will be saved as an
   incomplete instance and the enumerator can open it to continue editing from the tasks tab. Note incomplete instances are not sent to the server.
   (Requires version 21.02+ of the server and 6.302+ of FieldTask)
*  Allow user to set instance name. Instance names can be set automatically using collected data. If you are combining multiple names use concat() or join(). For example **concat(${name}, ' ', ${last_name})**
*  Screen Navigation. Use horizontal swipes, forward/backward buttons, or both.
*  Guidance. Whether survey guidance is shown: no, always shown, or collapsed.
*  Backward navigation. The ability of the user to go back to a previous question can be blocked using this option.

Sync & Connectivity
+++++++++++++++++++

*  Automatically Synchronise. If set the phone will refresh when a form changes on the server. The refresh can be specified to occur if connected to wifi only or
   when also connected via a cellular network. If the option **set on phone** is selected then the enumerator can enable or disable automatic synchronisation
   using the menus on the phone.
*  Delete submitted results from the phone. After a completed survey has been successfully submitted it can be automatically deleted from the device. This is
   recommended to improve security. If you do not select this option then you should manually delete completed forms when you are confident that you have the
   data.
*  Maximum number of tasks to download. The tasks are ordered by due date in ascending order.

Media
+++++

*  High Resolution Video. Allow or prevent the recording of high resolution videos.
*  Maximum pixels of the long edge of an image. This is a very useful setting to reduce the size of images that have to be sent over the network and stored
   on the server. Select the original size from the camera or one of: Very small (640px), Small (1024px), Medium (2048px) or Large (3072px).  The image is
   scaled so that its long edge is no larger than this, so if the image on the phone is 2,048 by 1,024 pixels and you select **Very small (640px)** then the
   submitted image will be 640 by 320 pixels.

Tracking & Geolocation
++++++++++++++++++++++

*  Prevent the disabling of location tracking. Locks tracking so it cannot be turned off on the device.
*  Enable Geo-fence. Enables the geo fence feature that can download or show tasks when the user is within a specified perimeter.
*  Send location data on path of user. Controls whether FieldTask records and sends the path of the user.
*  GeoShape and GeoTrace Input Method. How FieldTask records the points of a GeoShape or GeoTrace: placement by tapping, manual location recording or
   automatic location recording.  If this is set on the server then a dialog is no longer shown to FieldTask users before they start recording points.
   This reduces the time required to start recording and allows a consistent approach to recording geo poly types.
*  Recording Interval. When the input method is automatic, the time in seconds between points.
*  Accuracy. When the input method is automatic, the accuracy threshold in meters.

.. _webform-settings:

Webform Options
---------------

This tab allows customisation of WebForm appearance:

*  Page background colour.
*  Paper background colour.
*  Footer position.  The position of the "powered by" icon in the footer of the page.
*  Button colour.
*  Button text colour.
*  Heading text colour.
*  The WebForm banner logo.
*  Hiding the "save as draft" checkbox.

.. _email-settings:

Email Options
-------------

Sets up the email server that this organisation will use.  If these are not set then the email server specified
in the :ref:`server-settings` tab is used.

*  Email to get help.  The administrator email.  This address is also sent an email when the access settings in the
   :ref:`organisation-admin-settings` tab are changed.
*  SMTP host.  The host name of the SMTP relay that will forward email messages from the Smap server.
*  Email domain.
*  Email user name.
*  Email password.
*  Email server port.
*  Content.  Default content for emails.
*  Server identification.

DHIS2
-----

Requires SmapServer v26.09

This tab holds the connection to a DHIS2 instance.  One connection is held per organisation, so
a test instance should be set up in its own organisation.

From here you can set the DHIS2 URL and personal access token, optionally pin the API version,
and test the connection.  The test reports the DHIS2 version, the user the token belongs to and
how many organisation units that user can capture data for, so a connection that authenticates
but cannot do anything useful is apparent before it is relied on.

For the full description, including how to prepare the token in DHIS2, see :ref:`dhis2-connection`.

Operations
----------

Requires SmapServer v26.06.  Thresholds used by the :ref:`operations` page for the organisation that you are currently in.

*  Stale interval (days).  Any open task or case older than this counts as stale.
*  Trend window (days).  The period covered by the sparklines and backlog chart.
*  RAG amber threshold (overdue %).  The overdue percentage at which a unit turns amber.
*  RAG red threshold (overdue %).  The overdue percentage at which a unit turns red.

Sensitive Data
--------------

This tab is only shown to users with the security manager group.  It sets restrictions on access to sensitive data for the
organisation that you are currently in.

*  Signature Questions.  **No restrictions** or **Admin Only**.  If set to Admin Only then signature questions, that is image
   questions with the signature appearance, are hidden from users who do not have the administrator group.  They are left out of
   the console, exports, analysis and the API.  To restrict other questions, or to restrict signatures by role, use
   :ref:`rbac`.

.. _other-settings:

Other Options
-------------

This tab allows you to set other organisation level settings for the organisation that you are currently in.
Before SmapServer v26.10 only the minimum password strength was set here, and the other settings were in the
organisation dialog on the **Organisations** tab of the users page.

*  Time zone.  The default time zone for the organisation.  Usually the time zone is obtained from a user's browser
   settings.  However where reports are generated automatically this information may not be available and the time
   zone set here will be used.
*  Language.  The default language for the organisation.  As for time zone, normally the user's language is used.
*  Map source.  The default source of background maps: Mapbox, Google or MapTiler.  The keys for these services are set
   in the :ref:`server-settings` tab.
*  Allow editing of results.  Allow results to be edited on the server.
*  Allow notifications to be sent from WebForms.
*  Enable opt in.  Require the recipient of an email to opt in before they are sent emails.
*  Enable redactions.  Allow personal data to be redacted, see :ref:`rtbf`.
*  Minimum password strength.  See :ref:`password-strength`.  Only a user with the security manager group can change
   this setting.  Other administrators can see the value but not change it.
