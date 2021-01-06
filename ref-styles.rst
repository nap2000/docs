..  _formatting:

Formatting
==========

.. contents::
 :local:
 
You can use a combination of **Markdown** and **HTML** to format the text in a question or choice label. 
There is quite a bit of duplication between them but you can use whichever approach you are most comfortable with.

Using Markdown
--------------

Headers::

  # Header H1  
  ## Header H2  
  ### Header H3  
  #### Header H4  
  ##### Header H5  
  ###### Header H6

Bold::

  Surround the text with **
  **Text to be marked as bold**

Italics::

  Surround the text with *
  *Text to be shown in italics*

Escaping Markdown
+++++++++++++++++

The problem with using markdown is that if you want to use a # or a * as part of your label then you might 
find it disappears and the label gets reformatted.  To resolve this put a “\\” in front of::

  #
  _
  *

HTML
----

.. csv-table:: HTML Formatting:
  :width: 160
  :widths: 30,40,40,50
  :header-rows: 1
  :file: tables/html.csv
  
Example
-------

The following example survey combines both markdown and HTML. 
`Formatting labels <https://docs.google.com/spreadsheets/d/1Jvxjc990GxFufGUUYg33zqL1p-Jw1YHaOmBXjRimfeQ/edit?usp=sharing>`_
