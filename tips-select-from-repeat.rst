.. _select_ones_select_multiple_from_repeats:

Select ones, or select multiple, from repeats
=============================================

.. contents::
 :local:
 
You can create a list of choices for a select_one or select_multiple question from a repeat.  For example if you collected a list of people 
in a repeat group, you could then ask a question that selects one or more of those people.  This is done by setting the select's listname to
the name of the question that contains the choice values.  

The results can be filtered by putting the criteria in the choice filter column.


.. csv-table:: Survey Worksheet
  :header: type, name, label, choice_filter

  begin repeat, people, Person, 
  text, name, Name,
  integer, age, Age,
  end repeat,,,
  ,,,
  select_one ${name}, person_for_training, Select one of the people for training
  select_multiple ${name}, people_for_training, Select people who want training
  select_one ${name}, people_over_17_for_training, Select one of the people 18 or older for training, ${age} > 17



