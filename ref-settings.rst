.. _settings-reference:

Survey Settings
===============

The following settings can be specified in the settings worksheet of the XLS editor.  When using the online
editor they are specified in either the Settings Dialog or Case Management Dialog as shown below.

.. csv-table:: Settings:
  :width: 80
  :widths: 10,40,30
  :header-rows: 1
  :file: tables/settings.csv

  Roles
  -----

  Two columns are used for each role to store the row filter (:ref:`filtering-rows`) and the group that the role belongs to
  (:ref:`filter-groups`).  These headings are made up of::

      role::{role name}
      filter_group::{role name}

  In the role column you can put a row filter and in the filter_group column you can put the group the filter belongs to, this can be A or B.

.. csv-table:: Roles in Settings Worksheet
  :header: role::WASH, filter_group::WASH

  ${project} = 'wash', A
 


