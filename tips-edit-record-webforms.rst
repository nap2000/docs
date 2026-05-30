Edit a record from WebForms
===========================

.. contents::
 :local:

You can select and edit records directly from WebForms. The following video takes you through how to do this.

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/1POwyhSK5BI?start=173" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

In brief the instructions are:

#.  Use a select question to look up the instanceID in another survey. This is the record identifier
#.  Add a launch form question (Either parent or child is fine)
#.  In the parameters for this question specify the survey to be launched and the record using the parameter

::

  instance=${the name of the question that holds the instanceID}

