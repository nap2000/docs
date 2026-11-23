.. _operational-issues:

Operational Issues
==================

Available with Smap Server version 26.12.01+.

.. contents::
 :local:

The operational issues report lists the problems in your projects that somebody needs to fix, such as a
conflicting update that has not been reviewed or a notification whose filter no longer works.  Each issue has
a **Fix** button that opens the page where it can be fixed.

To open it administrators select **Issues** on the :ref:`operations` page.  Analysts,
who do not have the Operations page, select **Issues** in the console.

Scope
-----

The report covers the surveys in the projects you are a member of, in the organisation you are currently in.
Conflicting updates are only listed for bundles whose records you can see in full; if a role restricts you to
some of a bundle's records, its conflicts are not shown.

Errors are those recorded in the last 30 days.  An error that happens repeatedly, for example a notification
that fails on every submission, is listed once with the number of times it happened and when it first and last
happened.  Once the cause is fixed the error stops recurring and drops off the report after 30 days.

Issues
------

.. csv-table::
   :header: "Issue", "What it means", "Fix opens"
   :widths: 20, 50, 30

   "Conflicting update", "Two people changed the same answers of a record and the conflict has not been reviewed.  See :ref:`console_conflicts`.", "The record in the console, review it in the History tab"
   "Notification error", "A notification failed, for example its filter could not be evaluated or the email could not be sent", "The notification"
   "Case alert error", "A case management alert could not be evaluated", "The alert on the case management page"
   "Submission not loaded", "Submissions that could not be loaded into the database", "The monitor page, showing that survey"
   "Notification filter does not work", "An enabled notification whose filter no longer works with its survey, for example because a question it uses was deleted or renamed.  This is checked when the report is opened, so it is found before a submission fails.", "The notification"
   "Case alert filter does not work", "A case management alert whose filter no longer works with its survey", "The alert on the case management page"
   "Notification for a deleted survey", "An enabled notification whose survey, or every survey in whose bundle, has been deleted.  It will never be sent.", "The notification"
   "Tasks assigned to a deleted user", "Open tasks assigned to a user who has since been deleted", "The task group"
   "Task email not sent", "Emailed tasks that could not be sent", "The task group"
   "Assigned records that are not cases", "Records in a survey bundle that are assigned to people, although the bundle is not set up for case management.  They reach the people they are assigned to but are not counted or shown as cases, so nobody is monitoring them.  Either set up case management for the bundle, with a status question, or take the people off the records.  The count is the number of records.  See :ref:`case-management-config`.", "The case management page for the bundle"

Errors recorded before version 26.12.01 do not say which notification or alert they came from.  For these the
Fix button opens the list of notifications, or the case management page, for the survey.

Filtering and downloading
-------------------------

The buttons at the top show how many issues there are of each type; select one to show only that type.  The
issues can also be filtered by survey and by searching for text.

Select **Download XLSX** to save all of the issues as a spreadsheet.
