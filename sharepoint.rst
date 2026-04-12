.. _sharepoint:

SharePoint Integration
======================

.. contents::
  :local:

Requires SmapServer 
Smap can integrate with Microsoft SharePoint to support two workflows:

1. **Notification target** — when a form is submitted, a trigger can insert or update
   a row in a SharePoint list.
2. **Shared resource** — a SharePoint list can be used as a source of reference data,
   accessible from forms using the ``pulldata()`` and ``search()`` functions.

Supported versions
------------------

* **SharePoint Server 2019** (on-premises) — supported using S2S high-trust
  certificate authentication.
* **SharePoint Online** — planned for a future release.

.. _sharepoint-server-config:

Server Configuration
--------------------

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
-------------------------------------

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

.. _sharepoint-shared-resources:

SharePoint Lists as Shared Resources
--------------------------------------

A SharePoint list can be made available as a shared reference data source, accessible
from any survey in the organisation using the ``pulldata()`` and ``search()`` functions.

Setting up a SharePoint list mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to **Admin** → **Shared Resources** → **SharePoint Lists** tab.

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
