.. _repeat_from_select_multiple:

Repeat from a select multiple
=============================

.. contents::
 :local:
 
You can create a repeats from a select multiple question.  So if the user selects 2 choices then
two repeat instances can be automatically be created to collect further details.

.. csv-table:: Survey Worksheet
  :header: type, name, label, repeat_count, calculation

  select_multiple experience, experience, What experience do you have,,
  begin repeat, exp_repeat, Experience, count-selected(${experience}),
  calculation,item,,,"jr:choice-name(selected-at(${experience},(position(..)-1)),'${experience}')
  decimal, exp_years, Years of experience in ${item},
  text, exp_desc, Describe in detail your experience in ${item},
  end repeat,,,
