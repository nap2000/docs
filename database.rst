Database Design
===============

Smap uses a PostgresSQL databases with PostGIS extensions.  Because of the dependence on these geospatial extensions we gave
up on making the design database independent so there many PostgresSQL specifics in the design.

There are two databases:

*  survey_definitions.  Contains the meta information for surveys.
*  results. Contains all the collected data

Most of the tables in both databases are in the public schema, however some csv reference information is stored in
a csv schema in the survey_definitions database.

.. toctree::
  :maxdepth: 1

  database-tasks.rst

