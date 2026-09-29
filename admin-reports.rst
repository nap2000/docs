.. _admin-reports:

Administration Reports
======================

.. contents::
 :local:  
 
There are several useful reports that can help you understand what is
happening on your server.

Where a report takes longer to run, it is generated in the background and can
be downloaded later from the Reports module.

Form Access Report
------------------

This shows who has access to a survey and what level of access they have.  If they can't access a survey it shows the reason::

  Access from the Form Management Page
  Select "Form Access Report"
  Select the form that you want

Bundle Access Report
--------------------

This shows, for every survey in a bundle, its project and whether it is a data survey, an oversight survey, read only or
hidden on devices, together with which users can access each survey.  Access takes account of the users' projects,
security groups and roles::

  Access from the Form Management Page
  Select "Bundle Access Report"
  Select a survey in the bundle


Usage Report
------------

This report shows the number of surveys completed by each user for a month and
for all time. Optionally, this can be broken down by project, survey, or
device::

  Access from the Form Management Page
  Select "Usage Report"
  Select the month
  Optionally select a detailed breakdown
  Optionally include temporary users such as for anonymous logons and email tasks

Attendance Report
-----------------

This report shows the first time during the day that an enumerator refreshed
the phone and the last time, as well as the duration between these events and
the number of completed surveys. This can be used as an indicator of
attendance if enumerators are expected to press refresh at the start of work
and then refresh again to submit data at the end of the day's work.

Notification Report
-------------------

This report shows all notifications currently set up to respond to submitted
data::

  Access from the Form Management Page
  Select the "Notification Report"

Resource Utilisation Report
---------------------------

This report shows resources in Shared Resources, including CSV files, images,
video, and audio. It also shows which surveys use these resources::

  Access from the Form Management Page
  Select the "Resource Utilisation Report"

Summary of events by hour
-------------------------

This report shows a count of events recorded in the log for each hour of the
selected day.

  Access from the Log Management Page
  Select the "Hourly Summary" report

Organisational Structure
------------------------

A list of the enterprises, organisations and projects on the server.  Requires the administrator security group::

  Access from the Form Management Page
  Select "Organisational Structure"

Enterprise and Organisation Administrators
------------------------------------------

Available from SmapServer 26.08.  A list of the users who have the enterprise administrator or organisational
administrator security group, with their ident, name, email, enterprise and organisation.  These users can reach data
across organisations, so this report is a useful check of who holds that access.  Requires the organisational administrator or
enterprise administrator security group::

  Access from the Form Management Page
  Select "Enterprise and Organisation Administrators"
