.. _webforms:

WebForms
==========

.. contents::
 :local:

Introduction
------------

Webforms allows you to complete surveys in a web browser.  The webforms launch page can be found by selecting the menu **modules** then
**webforms**. To access this page you will need the **enum** security group.  Smap's webforms uses the enketo-core library.

.. figure::  _images/webforms1.jpg
   :align:   center
   :width: 	 600px
   :alt:     Launching Webforms

   Launching Webforms
   
There are 3 tabs on this page.  The Web Forms tab itself which allows launching of a blank survey.  The tasks tab where tasks
can be selected for completion.  Finally a settings page where settings that can be changed by a user who only has **enum** privilege
can be updated by that user.

Styling the Survey
------------------

Grids
+++++

.. figure::  _images/webforms2.jpg
   :align:   center
   :width: 	 600px
   :alt:     Webform styled as a grid

   Webform styled as a grid
   
To enable grids set **theme-grid** as the style in the XLSForm settings sheet.  Alternatively in the online editor
select menu **File**, then **Settings** then set style to **Grid**.

.. figure::  _images/webforms3.jpg
   :align:   center
   :width: 	 400px
   :alt:     Enabling Grids in XLSForm

   Enabling Grids in XLSForm

Once grids are enabled you can use **groups** (begin group, end group) to form the questions into the grid you want.

*  Enclose the questions that you want to appear in a single row within a group
*  Set the width of the group using w1, w2, w3, w4, w5, w6 etc in the appearance column for that group. w4
   will set the width to 4.  These widths i the group appearance set a number for the width of the row.  When
   the widths of the questions exceed that number then the question will be shown on the next row.
*  Then set the width of each question in the group also using w1, w2 etc.  Normally you would make these widths
   add up to the group width.
   
`Example Grid WebForm (From Enketo) <https://drive.google.com/file/d/1ppkrE6jmi3AuftMEF9hIt7wZ9NydxIDB/view>`_

Pages
+++++

To enable pages set **pages** as the style in the XLSForm settings sheet.  Alternatively in the online editor
select menu **File**, then **Settings** then set style to **Pages**.

Once you have set the style to **pages** then every question will appear on its own page with a **next** and
a **back** button to navigate.  You can then use groups with the field-list appearance to put multiple questions on 
a single page in exactly the same way that you can do for fieldTask.

Styling Webforms Itself
-----------------------

Webform style options can be found on the users page in the "Webform Options" tab.  

.. figure::  _images/webforms4.jpg
   :align:   center
   :width: 	 600px
   :alt:     Webforms Styling Options

   Styling WebForms


.. note::

  If you have "organisational admin" privilege then you won't see the above tab instead you can change the webform style in the organisations
  tab by selecting the organisation that you want to modify.
  
The following properties can be changed:

*  The page background colour
*  The paper background colour
*  The position of the footer icon
