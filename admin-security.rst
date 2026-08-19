.. _admin-security:

Security
========

.. contents::
 :local:

Survey Isolation
----------------

Surveys are placed inside an :ref:`organisational-hierarchy`. Firstly inside projects, 
projects inside organisations and organisations inside enterprises. Access to
each of these can be managed by assigning users access.

Groups
------

Users can be assigned one or more :ref:`security-groups` such as "Administrator" or "Analyst".  These groups determine
the functionality that the user can access.

Role Based Access Control
-------------------------

:ref:`rbac` can be used to provide fine grained control over access.

.. _password-strength:

Password Strength
-----------------

This feature is available with version 22.04 of the server.

A minimum password strength can be set for user passwords. When a user changes their password
they will be required to set a new password that is at least as strong as the minimum.

The minimum strength can be set for the :ref:`server-settings` and/or the organisation :ref:`organisations-settings`.  
The maximum of the two values set will be used.

The strength of a password reflects its randomness and avoidance of common words used by password breakers. The
following table shows sample password values and their strength;

.. csv-table:: Password Strengths
  :header: password, strength, comment

  password, 1, very weak
  Passw0rd, 10, very weak
  b0Gota987, 23, reasonable
  q2@dFgVPx, 51, strong
  q2@dFgVPxFvv%67d, 77, very strong

.. note::

  All of the above example passwords have been blocked from use if password strength is set above 0

.. _admin-security-two-factor:

Two Factor Authentication
-------------------------

Users can choose to protect their account with a code from an authenticator app in addition
to their password.  It is set up by each user from their own profile menu, and
:ref:`two-factor-authentication` describes how.

There is no organisation wide setting to require it.

Seeing who has it
+++++++++++++++++

The user management page has a column showing which users have two factor authentication
turned on, and a filter above the list so you can show only those who have it or only those
who do not.  The exported user spreadsheet includes the same column.  Importing a
spreadsheet never changes it, so two factor authentication cannot be turned on or off in
bulk.

Turning it off for a user
+++++++++++++++++++++++++

There are no recovery codes, so a user who has lost the phone their authenticator was on
needs an administrator to turn it off for them.  A button against the user in user
management does this.  Only administrators and organisational administrators can use it, and
only for users in their own organisation.

The user then signs in with their password alone and may set it up again against a new phone
whenever they choose.  They are not prompted to.

Enrolment, removal, failed codes and administrator resets are all recorded in the
:ref:`logs`.

.. warning::

  Two factor authentication applies to the web client only.  FieldTask and the API
  authenticate with a password or a token and are unaffected.  A password that may have been
  exposed still needs to be changed.

.. _html-sanitisation:

Sanitisation of WebForm HTML
----------------------------

User provided content, such as labels for questions, are sanitised using the OWASP java HTML sanitiser.  This removes all executable
code from the content and also any HTML elements that are not white listed as permitted for use.  This approach protects webForms from being used for cross site
scripting attacks while still permitting formatting with headers, bold text etc.

Validation of Names
-------------------

Names, such as user name or project name, are validated on entry to prevent use of HTML or other unsafe values.  They are also escaped before being shown in a web page.

Logging of changes to data
--------------------------

All changes to collect data are logged.  The data cleansing tool, which allows for mass changes to text answers, also allows for those changes
to be reversed automatically.
