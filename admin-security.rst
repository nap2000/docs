.. _admin-security:

Security
========

.. contents::
 :local:

Groups
------

Users can be assigned one or more :ref:`security-groups` such as "Administrator" or "Analyst".  These groups determine
they functionality that the user can access.

Role Based Access Control
-------------------------

:ref:`rbac` can be used to provide fine grained control over access.

Password Strength
-----------------

A minimum password strength can be set for user passwords. When a user changes their password
they will be required to set a new password that is at least as strong as the minimum.

The minimum strength can be set for the :ref:`server-settings` and/or the organisation :ref:`organisations-settings`.  
The maximum of the two values set will be used.
