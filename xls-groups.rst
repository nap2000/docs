Groups
======

Groups do as their name implies, they collect questions together into a group.  This has 2 purposes

1.  Allow a **relevance** to be applied to a lot of questions at once
2.  Show multiple questions on the screen at once

A group is defined using two question types.  A **begin group** that indicates the start of the group and an **end group**
that indicates its end.

.. figure::  _images/groups1.jpg
   :align:   center
   :width:   500px
   :alt:     Groups
   
   Groups
   
All the questions between **begin group** and **end group** are within the group.

*  To add relevance to an entire group put it on the **begin group**
*  To put all questions in a group onto the same screen add **field-list** as an appearance
*  In the special case where all the questions are select_one or select multiple and they refer to the same
   list then you can put them into a table setting an appearance of **table-list**
   
.. note::

  An end group type question does not need a name.  However it is a good idea to give it the same name
  as the question of type "begin group".  "end group" and "end repeat" are the only question types that
  do not need a unique name.

.. note::

  A "begin group" question does not need a label.  If you do include a label then it will be shown at the top of the
  screen in FieldTask for every question in the group.




