Features
========

.. contents::
 :local:  

Surveys
-------

.. csv-table:: 
  :header: Feature, FieldTask, WebForms, Versions
  :widths: 55,15,15,15

  :ref:`charts`, yes, no
  last-saved value retrieval, yes, no
  :ref:`launch a survey from within a survey<launch-survey>`, yes, yes
  :ref:`Multi-language<languages>`, yes, yes
  works offline, yes, yes,
  audit (timing; location per question; question changes), yes, no
  :ref:`image` questions, yes, yes
  video questions, yes, yes
  audio questions, yes, yes
  :ref:`Read and record barcode and QR codes<barcode-questions>`,yes, no, 
  :ref:`Read and record NFC chip identifiers<nfc-questions>`,yes, no, 
  :ref:`Read and match finger prints<feature-fingerprints>`,yes, no, SmapServer 23.01
  :ref:`background-audio-recording`, yes, no, FieldTask 6.300 - SmapServer 21.03
  :ref:`choices-from-repeat`,yes, yes, SmapServer 21.04
  :ref:`Matrix layout of questions<matrix>`,no, yes, 

Using Reference Data in Surveys
-------------------------------

.. csv-table:: 
  :header: Feature, FieldTask, WebForms, Versions
  :widths: 55,15,15,15

  :ref:`Referring to reference data in a csv file while offline<looking-up-data-csv>`, yes, yes
  :ref:`Referring to reference data in another survey while offline<looking-up-data-survey>`, yes, yes
  :ref:`Include local data not submitted to the server in reference data lookups.<looking-up-data-local>`, yes, no, FieldTask 6.400 - SmapServer 21.05
  :ref:`Lookup repeating data from other surveys or collections of surveys.<looking-up-data-pulldata>`, yes, no, FieldTask 6.200
  :ref:`Lookup data collected by other surveys while online without requiring an offline copy of the data<looking-up-data-survey-online>`, yes, yes
  :ref:`Lookup images online and use them in a survey (dynamic images)<dynamic-images>`, yes, yes

Administration
--------------

.. csv-table:: 
  :header: Feature, Versions
  :widths: 80,20

  :ref:`online-editor`,
  :ref:`Offline apreadsheet editor<xls-editor>`,
  :ref:`A history of all changes made to a survey<change-history>`,
  :ref:`Administration reports including access to forms; usage by user; usage of resources such as reference csv files by surveys; notifications that have been set etc<admin-reports>`,

Geospatial
----------

.. csv-table:: 
  :header: Feature, Versions
  :widths: 80,20

  Data is stored in PostGIS; a PostgreSQL database with geospatial extensions, 
  :ref:`Point; Line and Area type location data can be collected<locations>`,
  :ref:`Specify custom base maps when visualising location data on the server<shared-maps>`,

Analysis
--------

.. csv-table:: 
  :header: Feature, Versions
  :widths: 80,20

  Data is stored in a PostgreSQL relational database,
  :ref:`An internal dashboard is included which easily allows the creation of table; map; chart and image views of data. This is particularly useful for doing quality assurance and gaining quick insights into the data without requiring the effort and expense to setup a full featured BI tool<dashboard>`,
  Integration with external dashboards such as PowerBI and Tableau using the data API. `example live dashboard <https://www.meqadata.com/ul-reading-camps-bangladesh>`_,
  Embedding of AWS Quicksight dashboards within the server.  This allows you to use the Smap Server to authenticate users and control access to the dashbaord
  

Case Management
---------------

.. csv-table::
  :header: Feature, Versions
  :widths: 80,20

  :ref:`Cases <case-management>`,
  :ref:`Tasks<editing-adding-tasks>`,
  Email tasks that can be completed by people who do not have an account on the system and are instead identified by their email address,
  Notification Messages,
  :ref:`Manage work using the console<console>`,
  Audit trail of all changes,
  :ref:`Automatic labelling of images; translation of text and transcription of audio<automation>`, 
  :ref:`Automatically escalate cases if they have not been addressed in a specified time or based on the data<case_escalation>`, v20.06 

Security
--------

.. csv-table::
  :header: Feature, Versions
  :widths: 80,20

  :ref:`Multiple isolated enterprises on a single server<enterprises>`
  :ref:`Multiple isolated organisations on a single server<organisations>`
  :ref:`Manage access to surveys by teams by using projects<projects>`
  :ref:`rbac`
  :ref:`security-groups`
  :ref:`password-strength`, 22.04
  :ref:`html-sanitisation`, 23.02
  :ref:`delete-restore`
  :ref:`logs`
  `Strong privacy committment <https://smap.com.au/privacy.shtml>`_


Connectivity
------------

.. csv-table::
  :header: Feature, Versions
  :widths: 80,20

  :ref:`Server APIs that allow programmatic access to collected data as well as other data such as survey definitions and adminstration information such as users and projects<apis>`,
  :ref:`APIs for the FieldTask Android App that support customisation and extension of the capabilities of the app<fieldtask-api>`,
  :ref:`Call web hooks when an event happens such as a data submission or data is updated.<webhooks>`, Smap Server 21.05

