.. _integration:

Integration
===========

.. contents::
 :local:

Applications built with Smap can be integrated with other applications in multiple ways.  The following diagram shows the primary
interfaces in blue.  Typical external applications are shown in orange and the Smap components in green.

.. figure::  _images/integration1.jpg
   :align:   center
   :alt:     Integration

   Integration
   
Data Lake
---------

Data tables, images, video and other files collected using MDC can be pushed to a data lake where the data can be processed by data analytics tools 
pushed to other systems.

Smap Server API
----------------

Custom apps such as Progressive Web Apps, Native Mobile Apps or corporate systems can call this API to retrieve and update data.
(:ref:`apis`)

Android External App
---------------------

From forms, running inside Field Task, external applications can be called to retrieve data.  (:ref:`external-applications`)

.. _sharepoint:

SharePoint
-----------

Requires SmapServer v26.05.01

Smap can write submission data to SharePoint lists and use SharePoint lists as shared
reference data in forms. 

1. **Notification target** — when a form is submitted, a trigger can insert or update
   a row in a SharePoint list.
2. **Shared resource** — a SharePoint list can be used as a source of reference data,
   accessible from forms using the ``pulldata()`` and ``search()`` functions.

Supported versions
++++++++++++++++++

* **SharePoint Server 2019** (on-premises) — supported using S2S high-trust
  certificate authentication.
* **SharePoint Online** — planned for a future release.

.. _sharepoint-server-config:

Server Configuration
++++++++++++++++++++

SharePoint connection details are configured at the server level by a user with the
**server** security group.  Go to **Admin** → **Users** → **Server** tab and scroll
to the **SharePoint** section.

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Field
     - Description
   * - SharePoint URL
     - Base URL of your SharePoint server, e.g. ``https://sharepoint.example.org``
   * - Client ID
     - The GUID of the app principal registered in SharePoint (see :ref:`sharepoint-register-app`).
   * - Realm
     - The SharePoint farm realm GUID.  Use the **Discover** button to fetch this
       automatically from the server (no credentials required).
   * - Private Key (PEM)
     - The PKCS8 private key used to sign authentication tokens.
       See :ref:`sharepoint-prepare-cert` for preparation steps.

.. _sharepoint-prepare-cert:

Preparing the private key
~~~~~~~~~~~~~~~~~~~~~~~~~

The private key must be in **PKCS8 unencrypted PEM** format, beginning with
``-----BEGIN PRIVATE KEY-----``.

If you have a PKCS1 key (beginning with ``-----BEGIN RSA PRIVATE KEY-----``),
convert it with:

.. code-block:: bash

   openssl pkcs8 -topk8 -inform PEM -outform PEM -nocrypt \
       -in key.pem -out key_pkcs8.pem

Paste the full contents of ``key_pkcs8.pem`` into the **Private Key** field in the
server settings.

.. _sharepoint-register-app:

Registering the app in SharePoint (S2S High Trust)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before Smap can connect to SharePoint you must register it as a trusted app and
associate it with your certificate.

1. Generate a self-signed certificate and extract the public certificate and private
   key:

   .. code-block:: bash

      # Generate private key and self-signed certificate
      openssl req -x509 -nodes -newkey rsa:2048 -days 3650 \
          -keyout key.pem -out cert.pem \
          -subj "/CN=SmapSharePointIntegration"

      # Convert private key to PKCS8 (required by Smap)
      openssl pkcs8 -topk8 -inform PEM -outform PEM -nocrypt \
          -in key.pem -out key_pkcs8.pem

2. On the SharePoint server, open a **SharePoint Management Shell** and register the
   app principal:

   .. code-block:: powershell

      # Read the certificate
      $cert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2
      $cert.Import("C:\path\to\cert.pem")

      # Register the app principal — choose any display name
      $app = Register-SPAppPrincipal `
          -NameIdentifier "<client-id>@<realm>" `
          -Site (Get-SPSite "https://<sharepoint-url>") `
          -DisplayName "SmapIntegration"

      # Register the certificate as a trusted token issuer
      New-SPTrustedSecurityTokenIssuer `
          -Name "SmapIntegration" `
          -Certificate $cert `
          -RegisteredIssuerName "<client-id>@<realm>" `
          -IsTrustBroker

   Replace ``<client-id>`` with a new GUID you generate (e.g. via ``[guid]::NewGuid()``
   in PowerShell) and ``<realm>`` with the farm realm GUID (use the **Discover** button
   in Smap server settings to find it).

3. Grant the app the permissions it requires on the relevant site collections using
   ``Set-SPAppSiteSubscriptionName`` or the SharePoint app permission request XML,
   depending on your SharePoint version and governance requirements.

4. Enter the ``<client-id>`` GUID in the **Client ID** field in Smap server settings,
   and paste the contents of ``key_pkcs8.pem`` into the **Private Key** field.

.. warning::

   Keep the private key confidential.  It grants app-level access to your SharePoint
   server.  Rotate the certificate if it is ever compromised.

.. _sharepoint-notifications:

Notification Target: SharePoint List
++++++++++++++++++++++++++++++++++++

A submission notification can insert or update a row in a SharePoint list whenever a
form is submitted.  See :ref:`notifications` for general notification setup.

When adding a notification, select **SharePoint List** as the target.  The following
additional fields appear:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Field
     - Description
   * - List Name
     - The display name of the target SharePoint list, e.g. ``Incidents``.
       Once entered, the column selector is populated from the live list.
   * - Operation
     - **Insert** — adds a new row for every qualifying submission.

       **Update** — finds an existing row and updates it.  Requires a match
       column and match field (see below).
   * - Match Column *(update only)*
     - The SharePoint column used to find the existing row.
   * - Match Field *(update only)*
     - The survey field whose submitted value is compared against the match column.
   * - Column Map
     - A table mapping SharePoint column names (fetched from the live list) to
       survey field names.  Add a row for each column you want to write.

.. note::

   Column names are fetched directly from SharePoint when you enter the list name,
   so the server connection must be working before you configure notifications.

.. note::

   For update operations, if no matching row is found the notification will fail and
   an error will be recorded in the notification audit log.

.. figure::  _images/sp-update.jpeg
   :align:   center
   :alt:     Shows a form with mappings between SharePoint column and survey field ready for update

   Specifying a notification to update a SharePoint list

.. _sharepoint-shared-resources:

SharePoint Lists as Shared Resources
++++++++++++++++++++++++++++++++++++

A SharePoint list can be made available as a shared reference data source, accessible
from any survey in the organisation using the ``pulldata()`` and ``search()`` functions.

Setting up a SharePoint list mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to **Admin** → **Shared Resources** → **SharePoint Lists** tab.

.. figure::  _images/sharepoint1.png
   :align:   center
   :alt:     A table of SharePoint resources showing one added resource

   SharePoint List Tab on the Shared Resources page

You can add, edit or delete SharePoint resources.  Addition and edit open a dialog that allows you to set:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Field
     - Description
   * - Smap Name
     - The internal name used to reference the list in forms.  Forms refer to
       this resource as ``sharepointlist_<smap-name>``.
   * - SharePoint List Name
     - The display name of the list on the SharePoint server.
   * - Refresh Interval (minutes)
     - How often the local cache is updated from SharePoint.  Default: 60 minutes.
   * - Enabled
     - Toggle to suspend syncing without deleting the mapping.

Click **Sync Now** to force an immediate refresh.
Click **Show fields** to see the data available in the SharePoint list.

.. note::

   Data is cached locally.  If SharePoint is temporarily unavailable, forms continue
   to function using the last cached copy.

.. note::

   The cache holds up to 5,000 rows per list.  Support for larger lists will be added
   in a future release.

Using a SharePoint list in a form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reference the list in forms the same way you reference any shared resource, using
``sharepointlist_<smap-name>`` as the file name.

**pulldata() example** — look up a value from a matching row:

.. code-block:: none

   pulldata('sharepointlist_incidents', 'Reporter', 'IncidentId', ${incident_id})

**search() example** — populate a select question from the list:

.. code-block:: none

   search('sharepointlist_products', 'matches', 'Category', ${selected_category})

See :ref:`looking-up-data` for full details of the ``pulldata()`` and ``search()``
functions.


.. _dhis2:

DHIS2
------

Requires SmapServer v26.09

DHIS2 is the national health information system in many of the countries where Smap is used.
It is built for aggregation, indicators and reporting.  Smap is built for case management:
assigning work to field staff, following it up and closing it, offline.  The two solve
different halves of the same problem and work better connected.

Smap can use reference data held in DHIS2, so that a form collects against the client's own
organisation unit hierarchy rather than a separately maintained copy that drifts out of step.

.. note::

   Writing submission data back to DHIS2 as aggregate data values is planned for a later
   release.  This release covers reference data coming from DHIS2 into Smap.

.. _dhis2-prepare:

Preparing DHIS2
+++++++++++++++

Smap authenticates to DHIS2 with a **personal access token** (PAT).  Before setting up the
connection, create the token in DHIS2.

Use a dedicated service account, not a personal login
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a DHIS2 user for the integration rather than generating a token from an
administrator's own account.  There are three reasons.

*  **Two factor authentication blocks personal access tokens.**  DHIS2 refuses a token that
   belongs to an account with 2FA enabled, because a token bypasses the second factor.  If a
   token from an administrator account is used the connection test fails with
   *The API token is disabled, locked or 2FA is enabled*.  A service account without 2FA
   avoids weakening a person's login to make the integration work.
*  **Attribution.**  Anything Smap writes to DHIS2 is recorded against the account that owns
   the token.  A service account makes the DHIS2 audit trail describe the integration rather
   than name a person.
*  **Revocation.**  The integration's access can be withdrawn without disturbing anyone's
   ability to log in.

Creating the token
~~~~~~~~~~~~~~~~~~

In DHIS2, go to **Edit profile** then **Personal access tokens** and create a token.  Note
the following, all of which cause the connection to be refused with a 401 if set wrongly:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Setting
     - Guidance
   * - Allowed HTTP methods
     - **GET** must be permitted.  Smap reads metadata from DHIS2.
   * - Allowed IP addresses
     - Leave empty unless you have a reason not to.  DHIS2 validates the address from the
       ``X-Forwarded-For`` header, which a direct connection from the Smap server does not
       set, so an allow list can reject an address that looks correct.
   * - Expiry
     - Tokens expire.  Note the date, because the sync will begin to fail on it.

Copy the token when it is shown.  DHIS2 displays it once.

Organisation units and authorities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The service account needs the organisation units it will work with assigned to it.  A token
can be perfectly valid and every request still be refused because the DHIS2 user has no
organisation units.  The connection test reports how many the account has.

.. _dhis2-connection:

Setting up the connection
+++++++++++++++++++++++++

One DHIS2 connection is held per organisation.  If you need to work against a test instance
as well as a live one, set the test instance up in its own Smap organisation.

Go to **Admin** then **Settings** and select the **DHIS2** tab.

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Field
     - Description
   * - Name
     - A label for the connection, shown when a connection is referred to elsewhere.
   * - DHIS2 URL
     - The root of the DHIS2 instance, for example ``https://dhis2.example.org``.  A trailing
       slash or an included ``/api`` is accepted and removed.
   * - Personal Access Token
     - The token created above.  It is stored write only: once saved it is never sent back to
       the browser, so the field is blank when you return to the page.  Leave it blank to keep
       the token already stored, or type a new one to replace it.
   * - API Version
     - Optional.  Pin requests to a DHIS2 API version, for example ``42``.  Leave blank to use
       the instance default.
   * - Enabled
     - Suspends the connection without deleting it.

Click **Test Connection** to save and then check the connection.

Reading the connection test
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The test reports more than whether the server answered.  A connection can authenticate
successfully and still be unable to do anything useful, so the test also reports:

*  the DHIS2 version and database name
*  the DHIS2 user the token belongs to
*  how many organisation units that user can capture data for

Warnings are shown when the account has no data capture organisation units, or does not
report the authority to add data values.  These are warnings rather than failures, because
authority names differ between DHIS2 versions and an unfamiliar name should not block a
working connection.  They are worth resolving before relying on the connection.

.. _dhis2-org-units:

DHIS2 organisation units as a shared resource
+++++++++++++++++++++++++++++++++++++++++++++

The organisation unit hierarchy can be cached in Smap and used as reference data in any survey
in the organisation, in the same way as any other shared resource.  Set this up on
**Admin** then **Shared Resources**, on the **DHIS2** tab.  The cache is downloaded to Field
Task, so the hierarchy is available offline.

The hierarchy is flattened as it is read, because a cascading select cannot walk a tree on the
device.  Each row describes one organisation unit and carries its ancestors as ordinary
columns, so a cascading select is a normal choice filter.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Column
     - Description
   * - ``uid``
     - The DHIS2 identifier of the organisation unit.
   * - ``code``
     - The DHIS2 code.  This is the value to store in a form, because it is stable across a
       rebuild of the DHIS2 instance and is what DHIS2 expects when data is sent back.
   * - ``name``
     - The name of the organisation unit.
   * - ``level``
     - The level number within the hierarchy.
   * - ``<level>_code``, ``<level>_name``
     - A pair of columns for each level of the hierarchy, named from the level names set in
       DHIS2, for example ``district_code`` and ``district_name``.  Where levels have not been
       named in DHIS2 the columns are ``level1_code``, ``level2_code`` and so on.  A facility
       row carries every level above it, so filtering on an ancestor needs no lookup.
   * - ``gs_<group set>``
     - One column for each organisation unit group set, holding the group this unit belongs to
       within that set.  Group sets are the non hierarchical classifications in DHIS2, such as
       facility type or ownership, so these columns filter alongside the hierarchy rather than
       instead of it.

Setting up the synchronisation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to **Admin** then **Shared Resources** and select the **DHIS2** tab.  Set up the DHIS2
connection on the settings page first, see :ref:`dhis2-connection`.

You can add, edit or delete resources.  Adding and editing open a dialog that allows you to
set:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - Type
     - **Organisation units** for the hierarchy, or **Option set** for a single DHIS2 option
       set.
   * - Resource Name
     - The internal name used to reference the data in forms.  Forms refer to this resource
       as ``dhis2_<resource-name>``.  It must not contain spaces.  The dialog shows the full
       name a form will use as you type.
   * - Option set
     - For an option set resource only.  Chosen from the option sets on your DHIS2 instance,
       so you do not need to know an identifier.
   * - Filter
     - For an organisation unit resource only.  Optional.  The identifier of an organisation
       unit, to copy only that part of the hierarchy rather than all of it.
   * - Refresh (mins)
     - How often the cache is refreshed.  Default 1440, a day, which suits metadata that
       changes slowly.
   * - Enabled
     - Suspends synchronisation without deleting the resource.

Click **Sync Now** to copy the data immediately rather than waiting for the next refresh.

The table shows how many rows each resource holds and when it was last synchronised.  Where a
synchronisation failed, the reason is shown beneath the time, because the usual causes are
ones you can act on: no DHIS2 connection set up, a token that has expired, or a filter that
matches no organisation units.

.. note::

   Organisation units and option sets can be copied.  Programs are planned for a later release.

.. _dhis2-option-sets:

DHIS2 option sets as choice lists
+++++++++++++++++++++++++++++++++

A DHIS2 option set can be copied and used as the choice list for a question, so that a form
offers the client's own coded values rather than a separately maintained list.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Column
     - Description
   * - ``code``
     - The DHIS2 option code.  This is the value to store in the form, because it is what
       DHIS2 expects and it does not change when an option is relabelled.
   * - ``name``
     - The label to show to the user.
   * - ``uid``
     - The DHIS2 identifier of the option.
   * - ``sortby``
     - The order the options are held in within DHIS2.  Smap orders choices by a column of
       this name automatically, so the list appears in the same order as it does in DHIS2.

Use it in a form the same way as any other shared resource::

   search('dhis2_referral_reasons')

See :ref:`looking-up-data` for the ``search()`` function and :ref:`online-choices` for
building a choice list from a shared resource.

Limiting the hierarchy
~~~~~~~~~~~~~~~~~~~~~~

A national hierarchy can run to tens of thousands of organisation units.  Where an
organisation works in one region, set an organisation unit filter to the identifier of that
subtree and only that part of the hierarchy is synchronised.  Reducing the data at source is
more effective than any transport optimisation, and it keeps the download to Field Task small.

.. note::

   If DHIS2 returns no organisation units, the synchronisation fails and the previously cached
   list is left in place.  An empty result is far more likely to mean a filter that matches
   nothing, or a change in permissions, than a hierarchy that has genuinely emptied, and the
   cost of accepting it would be every form losing its choice list.

Using the hierarchy in a form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reference the resource in a form as ``dhis2_<smap-name>``, the same way a SharePoint list is
referenced as ``sharepointlist_<smap-name>``.

**Cascading select** — choose a district, then a facility within it:

.. code-block:: none

   search('dhis2_orgunits', 'matches', 'district_code', ${district})

**Filtering by group set as well as hierarchy** — clinics within the chosen district:

.. code-block:: none

   search('dhis2_orgunits', 'matches', 'district_code', ${district}, 'gs_facility_type', 'CLINIC')

**pulldata() example** — look up the name of a facility from its code:

.. code-block:: none

   pulldata('dhis2_orgunits', 'name', 'code', ${facility_code})

See :ref:`looking-up-data` for full details of the ``pulldata()`` and ``search()`` functions,
and :ref:`xls-cascading-selects` for cascading selects.

.. note::

   Store the DHIS2 ``code`` rather than the name.  It is what DHIS2 expects when data is sent
   back to it, and it does not change when a facility is renamed.
