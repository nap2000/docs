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

.. _html-sanitisation:

Sanitisation of Webform HTML
----------------------------

User provided content, such as labels for questions, are sanitised using the OWASP java HTML sanitiser.  This removes all executable
code from the content and also any HTML elements that are not white listed as permitted for use.  This approach protects webforms from being used for cross site
scripting attacks while still permitting formatting with headers, bold text etc.
