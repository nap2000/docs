.. _application-change-history:

Application Change History
==========================

.. contents::
 :local:

26.12.01
--------

Release Pending.  Not available for download.

#.  Editing a record that has repeating groups no longer adds the existing rows again.  Previously, each time a record was
    edited in WebForms, updated by a task, or updated by a later survey in a case management process, the rows of its
    repeating groups were duplicated.  Now the rows that are submitted replace the existing rows: unchanged rows are kept,
    new rows are added and deleted rows are removed.

    *   A repeating group that is not relevant in the survey doing the update is cleared, as for any other question that is
        not relevant
    *   A repeating group that the updating survey does not contain is not changed
    *   A repeating group with a "key_policy" or "instance_count" parameter works as before.  See :doc:`sub_form_kp`

    **Check before upgrading**.  If you update records through the API by submitting only the new rows of a repeating
    group, or have update tasks that are meant to add rows to the existing ones, then set the parameter
    ``key_policy=append`` on the repeating group so that the rows continue to be added.  Records that already have
    duplicated rows are not changed.

#.  Conflicting updates are merged.  When a record is saved from a version that somebody else has changed since it was
    opened, answers the person saving did not change keep the other person's change, and rows added to a repeating group by
    either person are kept.  Answers both people changed are recorded as a conflict in the record's history, where they
    can be reviewed, and a notification can be sent.  See :ref:`console_conflicts`.

    *   A change to a single record in the console now creates a new version of the record, as a submission does.  Bulk
        changes are unchanged.
    *   Rows of repeating groups now carry a hidden identifier.  ODK Collect will download each form again once after the
        upgrade.  FieldTask picks up the identifier when a survey is next changed; until then rows are matched by their
        answers.

#.  A case can be assigned to more than one person.  Turn on **Allow multiple assignees** in a bundle's case settings
    and everyone assigned has the same access to the case.  The setting is off by default, so existing bundles work as
    before.  See :ref:`multiple_assignees`.

    *   In the console, **Add user** adds somebody to the people who have the case, and choosing **Everyone in** a
        role adds every member of the role who can be given it.  An administrator can take one person off, or everybody with
        **Unassign all**.  **Release** takes only you off.
    *   An escalation adds its people and takes off those an earlier escalation added; people assigned in the console
        stay.  An escalation to a role adds every member of the role who can access the record.
    *   Every person assigned gets the case on their device.  Rejecting it takes only that person off.  Closing a case
        takes everybody off.
    *   Emails to the assigned user go to everyone assigned, and the **Assigned** column lists them all.
    *   In Operations the case viewer shows **Who has this case**: the people assigned and those with the case as a
        reference, how and by whom each was added, and the role if it was through one.  Record lists show how many
        people have each case as a reference.  See :doc:`operations`.

#.  Editing lines and shapes in WebForms is easier.  A whole line or shape can be dragged to a new place, points can be
    added from a handle in the middle of each side, points are removed without a confirmation and can be put back with
    undo, and all points can be removed at once.  Any point of a closed shape, including the first, can now be selected
    and dragged.  On a phone or tablet, geotrace and geoshape questions now always have a map, as in FieldTask, without
    needing the maps or placement-map appearance.  See :ref:`editing-lines-shapes`.

#.  A new operational issues report lists the problems that somebody needs to fix: conflicting updates waiting for
    review, notifications and alerts that failed, submissions that could not be loaded, filters that no longer work,
    notifications whose survey has gone, task problems, and records assigned to people in a survey bundle that is not set
    up for case management.  It can be downloaded as a spreadsheet.  Administrators open
    it from Operations, and analysts from the console.  See :doc:`operational-issues`.

#.  Server expressions are checked when they are saved.  A notification or case alert filter, task rule, PDF template
    rule, role row filter, reference data filter or server calculation that will not work, for example because it names a
    question the survey does not have or compares text with a number, is refused with a message that says why.  A survey
    change that breaks an expression already saved warns about it, and the operational issues report lists it.  Filters
    typed in the console and for exports get the same message.  A question whose name is longer than 52 characters can
    now be used in an expression.  See :ref:`server-expressions-checks`.

    **Check before upgrading**.  An integration that creates notifications, alerts or task rules through the API with
    filters that do not work yet, expecting to fix them later, will now be refused.

#.  Survey expressions are checked when a survey is uploaded and, for the first time, when it is changed in the
    online editor.  A relevant, constraint, calculation or choice filter that cannot be read, uses a function that does
    not exist or gives it the wrong number of arguments, or calculations and relevance that depend on each other in a
    loop, are reported with the question, the column and the character where the problem is.  A select with no
    choices is also reported.  The editor does not save a change that causes one of these problems.  Problems already
    in a survey, and a function used wrongly in a constraint or choice filter, are shown as warnings.  See
    :ref:`expression-reference`.

    **Check before upgrading**.  Surveys are no longer checked by loading them with the JavaRosa library that
    FieldTask uses, so test new surveys in FieldTask before they are used.

#.  Several status values can close a case, and a case reopens when a change of status moves it back to an open value.
    The same rule applies to a submission, a console or bulk update, and an update through the API.  Closing records in
    the history who had the case; reopening gives the case back to them, restarts its alerts from the reopening, and
    sends notifications with the new **Case reopened** trigger.  Closing a case in the console now takes everyone off
    it, as a submission already did.  A later survey in a bundle that does not ask the status question no longer opens a
    closed case.  See :ref:`case_reopen`.

    *   The closed statuses are chosen from the status question's answers when it is a select one question.
    *   A case closed by the submission that creates it, or by importing data, is recorded in its history.
    *   Operations record lists show how many times each case has been reopened.

#.  Operations shows open cases and tasks by person, as well as by role and by survey bundle, and the panel that was
    labelled Units (roles) is now named after the view it shows.  See :doc:`operations`.

#.  Operations only shows the work of the projects you are a member of.  This applies to security managers too, who
    still see every role.

    **Check before upgrading**.  An administrator who used Operations to watch projects they are not a member of should
    be added to those projects.

#.  Other

     *  In a bundle of surveys, when the first survey in the bundle updates a record, rows that other surveys in the bundle
        added to repeating groups are now kept.
     *  A location passed as an initial value to a WebForm, or in the initial data of a mailout, is now set on a new record.
     *  Operations status no longer counts records as open cases after case management has been turned off for a survey.
     *  Setting a survey role to not enabled and then back to enabled no longer loses its row and column filters.
     *  A record's history shows the case alerts it has raised, with a switch to hide them, and an email notification that
        had nobody to send to is shown as "No recipients".
     *  The workflow page shows the subject and recipients of email and SMS steps, and notifications on a bundle can be
        edited from it.
     *  Saving a task step on the workflow page no longer removes a task rule that takes the assignee from the data.
        The step now shows that rule, which is still changed in task management.  A rule removed this way by an earlier
        version has to be set again in task management.
     *  Errors when saving a PDF template rule, or a step on the workflow page, are now shown.
     *  In Operations a long list of open alerts scrolls within its panel.
     *  In the console a record can be locked and edited from a row of one of its sub forms.  Sub form rows can no longer
        be deleted or bulk edited on their own.
     *  In the console map the layer switches show and hide the data and heatmap layers.  The add layer dialog, which made
        unsaved copies of layers, has been removed.
     *  When a change to a record is refused, the message says which question needs a number, date or location.
        Clearing a number answer now empties it.
     *  Dashboard map clusters count a missing answer as 0, and their percentages are weighted by the number of records.
     *  Dashboard question tables no longer have a Record column, and a new panel selects the survey when there is only
        one.
     *  Dashboards need the Analyst, Admin or View Data security group.
     *  Only administrators can change an organisation's CSS.
     *  Replacing a survey with an XLSForm applies the roles in the XLSForm.  Roles not in it are kept and listed in a
        warning.  The pii setting of questions is now saved on upload.
     *  Uploading a survey as an XForm (.xml) file uses the same checks as an XLSForm, and translations of the same
        language are merged.
     *  A task rule that prepopulates its tasks no longer also marks them as blank.
     *  On the settings page the Appearance tab is now Organisation Appearance and the Server tab is first.  The DHIS2
        tab confirms a save, and all tabs show save errors on the page.
     *  The case settings page is laid out more clearly.

26.11.04
--------

`Download 26.10.04 <https://smap-code.s3.us-east-1.amazonaws.com/os_smap_26_11_04_7101.tgz>`_

#.  The installation scripts should work on additional linux distros including

    *  Debian 13
    *  RHEL 10
    *  Amazon Linux Server

#.  Group by on map panels and the ability to generate hexagonal grids to group by has been restored

#.  When the connection to the  mail server is encrypted then its certificate is now checked.  Earlier versions encrypted the connection
    when the mail server offered it but accepted any certificate.

    *   On port 465 the connection is encrypted from the start
    *   On other ports the connection is encrypted with STARTTLS when the mail server offers it.  If a mail user name
        and password are set the mail server must offer it, otherwise nothing is sent
    *   The mail server's certificate must come from a public certificate authority and match the host name in your
        email settings
    *   A mail server on the Smap server itself (localhost or 127.0.0.1) is not affected

    **Check before upgrading**.  Sending will stop if your mail server uses a self-signed or internal certificate, if
    the host name in the email settings does not match its certificate (for example an IP address is entered but the
    certificate names mail.example.com), or if it needs a password but does not offer STARTTLS.  The email error then
    says which of these it is and names the mail server.

    **To fix it** set the email host to the name on the mail server's certificate, give the mail server a certificate
    from a public certificate authority, or, on your own server, add your internal certificate authority to the Java
    trust store that Tomcat uses.  There is no setting to turn the check off.

#.  Other

     *  Fix formatting of table list labels
     *  Fix formatting of WebForm print to remove menu bar choices.
     *  Self registration of new organisations is now a server setting, “Allow anyone to register a new organisation”, off by default.
     *  The registration page uses Turnstile when the server has Turnstile keys, limited to 3 an hour from one address, and to 20 an hour per server when Turnstile is not set.
     *  Email attachments that could run in a browser, such as html and svg files, are now downloaded rather than opened.
     *  Emails include one click unsubscribe headers, so Gmail, Outlook and Apple Mail show their own unsubscribe button.
     *  Re-subscribing: the subscriptions page now emails a link for each organisation instead of listing them on the page. Subscribe and opt in links work once and expire after 30 days.
     *  Contacts: An unsubscribed contact can now be deleted while keeping the email address unsubscribed.
     *  New servers have password strength set by default so that a strong password is required by default. The server admin user can then change the default password strength from the server settings page.
     *  When the admin user first logs on to a new server they are forced to change their password.
     *  When a password is changed the existing password cannot be reused.

26.10.02
--------

`Download 26.10.02 <https://smap-code.s3.us-east-1.amazonaws.com/os_smap_26_10_02_5656.tgz>`_

#.  Security fixes.
#.  Data protection requests (DSAR and right to be forgotten) now require the Data Protection Officer security group.  Give this group to whoever handles these requests before upgrading
#.  WhatsApp and SMS conversations.  Direct support for the Meta WhatsApp Cloud API.  Reply to a case's conversation from the console and from WebForms
#.  Organisation settings have moved from the Users page to a new Organisation tab on the Settings page
#.  Messaging settings are split into separate Vonage, WhatsApp and SMS sections
#.  The Submissions column in campaigns counts submissions from each recipient's link in that campaign
#.  Webhooks can no longer call addresses on the server itself, webhook URLs with a port number now work, and webhooks time out instead of holding up notifications
#.  Rate limited API requests now get HTTP status 429 (Too Many Requests)
#.  Bug fixes

26.09.04
--------

`Download 26.09.04 <https://smap-code.s3.us-east-1.amazonaws.com/os_smap_26_09_04_4518.tgz>`_

#.  FieldTask updated to version 5.4.02
#.  DHIS2 integration
#.  Bug fixes

26.08.15
--------

`Download 26.08.15 <https://smap-code.s3.us-east-1.amazonaws.com/os_smap_26_08_15_8452.tgz>`_

#.  Manage offline maps from shared resources
#.  Two factor authentication
#.  A new report listing users with enterprise or organisational administration privilege
#.  Performance improvements
#.  Deploy shared libraries to the tomcat shared class loader to reduce size
#.  Bug fixes

26.07.02
--------

`Download 26.07.02 <https://smap-code.s3.us-east-1.amazonaws.com/os_smap_26_07_02_2671.tgz>`_

#.  Remove the legacy sdDataAccess module and move its remaining functionality into sdDAL
#.  Fix user structure report so that it reports on enterprise and organisational administrators
#.  Reduce the number of database access calls per webservice requests that are used for authorisation and to get user details
#.  Fix an unresponsive button on some opt in emails
#.  Move common code to shared libraries in Tomcat
#.  Add logging of changes to notifications
#.  Read report media using the S3 SDK and not over HTTP, improving performance and eliminating authorisation errors when embedding media in a report
#.  Fix issues with automatic camera and location opening on mobile devices when using WebForms
#.  Make the user assign select in notifications a combo button
#.  Open tasks in WebForm by instanceid instead of primary key


26.06.12
--------

`Download 26.06.12 <https://smap-code.s3.us-east-1.amazonaws.com/os_smap_26_06_12_926.tgz>`_

#.  A new operations monitor page to go with the console
#.  A new pulldata / lookup point and click builder in the survey editor
#.  Reference records.  A readonly case that can be assigned to multiple people
#.  Periodic emails can attach an operations summary and not just reports
#.  Dashboards have a relative data range that can be applied to all panels
#.  Administrators can now manage other peoples dashboards
#.  Multiple bug fixes

26.03.32
--------

`Download 26.03.32 <https://smap-code.s3.us-east-1.amazonaws.com/os_smap_26_03_32_9538.tgz>`_

#.  Allow for dates to be represented as empty strings in JSON when creating new tasks via the API
#.  Fix errors on online editor page for preloads


26.03.28
--------

`Download 26.03.28 <https://smap-code.s3.us-east-1.amazonaws.com/os_smap_26_03_28_1759.tgz>`_

#.  Improve Aria support in WebForms, Survey Management
#.  Add text wrapping in table panels in the dashboard.  Previously text answers would be cut off and could not be made visible.
#.  Add a menu option to expand a table record in the dashboard to show one page per record with the question answers displayed down the page.
#.  Fix issues related to the migration to ESM

26.03.09
--------

`Download 26.03.09 <https://smap-code.s3.us-east-1.amazonaws.com/os_smap_26_03_09_360.tgz>`_

#.  Add a tab for servers on the monitoring page.  This shows queue activity include whether queues are running or stopped
#.  Removed the logging of "heartbeats" for queues in the subscriber logs.  The number of logs written by default reduced. `The log level for the subscriber can now be specified. <https://www.smap.com.au/docs/server-admin-logs.html#setting-a-log-level>`_
#.  Improve appearance of analysis page
#.  Add Pie Charts as a charting option on the analysis page


25.10.44
--------

`Download 25.10.44 <https://smap-code.s3.us-east-1.amazonaws.com/os_smap_25_10_44_2056.tgz>`_

#.  Make processing of key queue more robust
#.  Add _assigned as a column that can be filled when importing data
#.  Add support for accepting and rejecting self assigned tasks on the WebForms page
#.  Fix issue in counting tasks so that self assigned ones are counted
#.  Improve consistency of URLs in email campaign mail outs
#.  Fix an issue preventing the resending of email campaign mail outs
#.  Update the version of the Tomcat application server
#.  Add counts for sub forms in survey lookup

Note this release was patched on 2026-03-13 from version 43 to 44 to fix a bug.

25.10.37
--------

`Download 25.10.37 <https://smap-code.s3.us-east-1.amazonaws.com/os_smap_25_10_37_2155.tgz>`_

#.  Add support for fully multi-threaded subscribers so you should be able to start multiple subscribers on multiple servers to process uploads
#.  Performance improvements to the subscriber, if you have tens of millions of uploads the query duration to find new uploads to apply will drop from 3 seconds or so to a few milliseconds
#.  Additional information included in the server information API query "/api/v1/lookup/survey_ident/{survey_ident}". This includes the number of records submitted to the survey and the date of the first and last submission.
#.  Conserve memory in subscriber.  Previously this was causing out-of-memory errors when large numbers of large PDFs were being generated
#.  Fix a bug in writing CSV labels for resource files when there were spaces in some of the survey languages
#.  Add the ability to set a limit on the number of records returned in an API call
#.  Reorganise some of the settings tabs to put settings in categories for easier navigation and readability
#.  Add support for WebP images


25.10.03
--------

`Download 25.10.03 <https://smap-code.s3.us-east-1.amazonaws.com/os_smap_25_10_03_5919.tgz>`_

#.  Use text-type questions in graphs on the analysis page
#.  Add a bundle access report
#.  Add support in the online editor for the no-collapse appearance

25.09.11
--------

`Download 25.09.11 <https://smap-code.s3.us-east-1.amazonaws.com/os_smap_25_09_11_708.tgz>`_

#.  Fix errors in setup scripts used on a new install
#.  Fix issue with addition of parameters to console queries that may occur if the columns are re-ordered
#.  Automatically release a record after it is closed
#.  Remove the record history entry showing a record has been deleted when this is part of an update transaction

25.09.03
--------

`Download 25.09.03 <https://smap-code.s3.us-east-1.amazonaws.com/os_smap_25_09_03_7295.tgz>`_

#.  Set the user name of the user who assigned a case in the history page
#.  Include additional security groups in the form access report
#.  Add row filters to the form access report
#.  Unescape HTML codes when downloading data to XLS from the console
#.  Require specific security groups before allowing bulk update
#.  Store multiple column orders in the console for different combinations of survey and oversight form
#.  Add support for last saved in select questions in webforms
#.  Only send a notification once per record
#.  Fix paging in the console at 100
#.  Close webform tab automatically when opened as a task

25.04.39
--------

`Download 25.04.39 <https://smap-code.s3.us-east-1.amazonaws.com/os_smap_25_04_39_3887.tgz>`_

#.  Include support for last-saved in WebForms
#.  Reduce size of WebForm code that needs to be downloaded to browser
#.  Default the user name to the user ident if it is not set when adding a user
#.  Include read-only surveys as surveys that can be selected for the application of security roles
#.  Fix a bug that prevented the showing of images in PDFs when those images were stored in AWS S3.
#.  Add support for barcodes in WebForms.  These can now be used in browsers on iOS devices.
#.  Fix a bug in reports which caused multiple issues when the data included server calculations.

25.04.33
--------

`Download 25.04.33 <https://smap-code.s3.amazonaws.com/os_smap_25_04_33_6357.tgz>`_.

*  Set a limit on uploaded media of 30MB for each file
*  Fix a problem generating PDFs when embedded images do not contain metadata allowing rotation
*  Remove renaming of subscriber logs when deploy script is run.  It is assumed that logrotate will be used instead.
*  Update Spanish translations
