.. _notification-api:

Notification API
================

.. contents::
 :local:

Available with Smap Server 26.04.01+.

This API manages notifications that fire when a form submission is received. The current
implementation covers **SharePoint list notifications**, which write submission data to a
designated SharePoint list each time a record is submitted.

The API is intended for server-to-server use (for example, a SharePoint Add-In that
automatically wires up a notification when a new Smap form is created). No
``X-Requested-With`` header is required.

Authentication
--------------

Standard Basic Authentication is used (``/api/v1``). The calling user must have
**analyst** or **admin** privilege.

SharePoint List Notifications
-----------------------------

A SharePoint list notification connects a Smap survey to a SharePoint list. Each time
a submission is received the specified fields are written to the list. Column mapping
controls which Smap question answers are written to which SharePoint columns.

.. http:get:: /api/v1/sharepoint/notifications

  :synopsis: Returns all SharePoint list notifications accessible to the authenticated user, across all their projects.

  **Example response**:

  .. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    [
      {
        "id": 42,
        "name": "Staff form to HR list",
        "survey_ident": "s12_345",
        "survey_name": "Staff Onboarding Form",
        "enabled": true,
        "sp_list_title": "HRStaffList",
        "sp_operation": "insert",
        "sp_match_column": null,
        "sp_match_field": null,
        "column_map": [
          { "sp_column": "Title",      "smap_field": "full_name" },
          { "sp_column": "Department", "smap_field": "dept" },
          { "sp_column": "StartDate",  "smap_field": "start_date" }
        ]
      }
    ]

  :query text tz: Timezone for date/time values (default ``UTC``).
  :reqheader Authorization: Basic authentication.
  :statuscode 200: Success. Returns an array (may be empty).

.. http:post:: /api/v1/sharepoint/notifications

  :synopsis: Create a new SharePoint list notification. Returns the created notification including its generated ``id``.

  **Request body** (JSON):

  .. sourcecode:: json

    {
      "name": "Staff form to HR list",
      "survey_ident": "s12_345",
      "enabled": true,
      "sp_list_title": "HRStaffList",
      "sp_operation": "insert",
      "column_map": [
        { "sp_column": "Title",      "smap_field": "full_name" },
        { "sp_column": "Department", "smap_field": "dept" }
      ]
    }

  **Required fields:**

  * ``survey_ident`` — the Smap survey identifier (e.g. ``s12_345``).
  * ``sp_list_title`` — the display title of the target SharePoint list.

  **Optional fields:**

  * ``name`` — a human-readable label for the notification.
  * ``enabled`` — whether the notification fires on submission (default ``true``).
  * ``sp_operation`` — ``"insert"`` (default) or ``"update"``.
  * ``sp_match_column`` — SharePoint column used to locate the existing row (required when ``sp_operation`` is ``"update"``).
  * ``sp_match_field`` — Smap question name whose submitted value is matched against ``sp_match_column`` (required when ``sp_operation`` is ``"update"``).
  * ``column_map`` — array of ``{ "sp_column": "...", "smap_field": "..." }`` objects mapping SharePoint column names to Smap question names. If omitted, no fields are written.

  **Example response**:

  .. sourcecode:: http

    HTTP/1.1 201 Created
    Content-Type: application/json

    {
      "id": 42,
      "name": "Staff form to HR list",
      "survey_ident": "s12_345",
      "survey_name": null,
      "enabled": true,
      "sp_list_title": "HRStaffList",
      "sp_operation": "insert",
      "sp_match_column": null,
      "sp_match_field": null,
      "column_map": [
        { "sp_column": "Title",      "smap_field": "full_name" },
        { "sp_column": "Department", "smap_field": "dept" }
      ]
    }

  :reqheader Authorization: Basic authentication.
  :reqheader Content-Type: ``application/json``
  :statuscode 201: Notification created. Body contains the new notification with its ``id``.
  :statuscode 400: Missing required fields.
  :statuscode 403: Not authorised to access the specified survey.

.. http:put:: /api/v1/sharepoint/notifications/(int: id)

  :synopsis: Update an existing SharePoint list notification. The full notification object must be supplied; all fields are replaced.

  **Path parameter:**

  * ``id`` — the notification id returned by the POST or GET call.

  **Request body** — same structure as POST.

  **Example request**:

  .. sourcecode:: http

    PUT /api/v1/sharepoint/notifications/42 HTTP/1.1
    Content-Type: application/json

    {
      "name": "Staff form to HR list",
      "survey_ident": "s12_345",
      "enabled": true,
      "sp_list_title": "HRStaffList",
      "sp_operation": "update",
      "sp_match_column": "EmployeeId",
      "sp_match_field": "employee_id",
      "column_map": [
        { "sp_column": "Title",      "smap_field": "full_name" },
        { "sp_column": "Department", "smap_field": "dept" },
        { "sp_column": "EmployeeId", "smap_field": "employee_id" }
      ]
    }

  :reqheader Authorization: Basic authentication.
  :reqheader Content-Type: ``application/json``
  :statuscode 200: Notification updated.
  :statuscode 400: Missing required fields.
  :statuscode 403: Not authorised to access the specified survey.

.. http:delete:: /api/v1/sharepoint/notifications/(int: id)

  :synopsis: Delete a SharePoint list notification.

  **Path parameter:**

  * ``id`` — the notification id.

  **Example request**:

  .. sourcecode:: http

    DELETE /api/v1/sharepoint/notifications/42 HTTP/1.1

  :reqheader Authorization: Basic authentication.
  :statuscode 200: Notification deleted.
  :statuscode 404: No SharePoint notification found with that id.

Column Map
----------

The ``column_map`` array controls which Smap question answers are written to which
SharePoint list columns on each submission.

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Field
     - Description
   * - ``sp_column``
     - The internal name of the SharePoint column (not the display name). Use the
       SharePoint list settings to find the internal name if it differs from the label.
   * - ``smap_field``
     - The Smap question name as defined in the survey (the ``name`` column in XLSForm).

Update Mode
-----------

When ``sp_operation`` is ``"update"``, Smap will look for an existing list item whose
``sp_match_column`` value equals the submitted value of ``sp_match_field``, and update
that item rather than inserting a new one. If no matching item is found the submission
is silently skipped; no new row is inserted.

Finding Which Form Corresponds to a SharePoint List
----------------------------------------------------

To determine which Smap survey is already linked to a given SharePoint list, call
``GET /api/v1/sharepoint/notifications`` and search the returned array for an entry
whose ``sp_list_title`` matches the list you are interested in. The ``survey_ident``
field on that entry identifies the linked survey.
