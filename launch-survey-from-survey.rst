.. _launch-survey:

Launch a Survey from inside a Survey
====================================

.. contents::
 :local:
 
While completing a survey you may find that another survey also needs to be completed.  You can launch this second survey from 
within the first, complete it, and then be returned automatically to your location in that first survey.  

There are many applications for this feature. For example you could create a survey whose sole purpose was to 
decide which survey really needs to be completed.

.. warning::

  Only works with FieldTask and not on WebForms

.. note::

  This capability is similar to entering a subform using **begin repeat** (:ref:`xls-repeats`).  However sub forms are included within the main 
  survey whereas here we are starting a completely different survey.

Linking data between the surveys
--------------------------------

When you launch another survey you may want to be able to connect the data between the two surveys.
This is done by specifying a question in one of the surveys that will hold a key pointing to a record in the other.

.. note::

  If you specify a question to hold a linking key then the relationship between the two surveys is one to many.  That is a single record in one of
  the surveys can be referenced by many records in the other.  The question is: which survey has the single record and which has the many?  This leads
  to the concept of a **parent** survey and a **child** survey.  The parent can have many children but, in this world of surveys, a
  child can have only one parent.

  When launching a new survey you can choose that it be a child or a parent of the first survey.  If you are not linking the data between the
  surveys then it does not matter which one you choose.

  the following examples are going to be based on the **parent** survey being a class in a school and the **child** survey being a pupil
  in that school.

Example 1 - Launch the Class Survey(Parent) from a Pupil Survey (Child)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Lets assume you are completing a survey to get details on a pupil and you want to note the class that they are attending.  However that class is not
currently available to be picked.  Hence the class survey is launched as a **parent form/survey** and you specify that the key created by the
class survey should be stored in the **class** question of the **Pupil survey**.

The :ref:`online-editor` offers good support for launching surveys.  So first create the Pupil survey using the online editor 
then add a Parent Survey question type.

.. figure::  _images/launch1.png
   :align:   center
   :width: 	 300px
   :alt:     Select the Parent Survey / Form Question Type

   Select the Parent Survey / Form Question Type

You will then be asked to add parameters.

.. figure::  _images/launch2.png
   :align:   center
   :width: 	 300px
   :alt:     Set the paremeters

   Set the parameters
   
#.  Select the survey to launch, in this example its the **class** survey
#.  Select the question in the child survey in which to store the key. Optional, but since we want to link the pupil to the class
    we are going to do this.  This question has to accept an answer that is of type text.  As well as text questions, select_one,
    calculates, barcodes all store their data as text.	The online editor will present the valid questions that you can select. 
#.  Select Auto Play if you want the class survey to be launched without the user having to press a button.


Example 2 - Launch a Child Survey
+++++++++++++++++++++++++++++++++

Alterntively you may be completing a survey on classes and realise that you have not registered a child that you want to enroll in the class.
Follow the same steps as for creating the parent survey but this time select the **child survey / form** question type.   When you are asked
where you want to place the key, the questions shown will be from the child survey.

Making use of linkages between Surveys
++++++++++++++++++++++++++++++++++++++

If you are analysing your data in a Business Intelligence tool then you can join the data using the key question.  Alternatively in the console
you can **drill down** from parent survey to child survey or from child survey up to parent survey to see the connected data.

Hiding the launched Surveys on the phone
----------------------------------------

Commonly you will not want the user to start up a "launched" survey independently.  You can hide launched surveys 
so that they are not directly visible in fieldTask.  To do this go to the survey settings and select "Hide on device".

Passing data to the launched survey
-----------------------------------

Initial Data
++++++++++++

Available with Smap Server 20.09+

You can specify the initial data that the launched survey receives in the "initial" parameter. For example::

  initial=name:${qname},vegetable:parsnip

The format is 1 or more comma separated value specifications consisting of:

* The name of the question in the launched form that is going to receive the default value
* A colon separator
* The value

This value can be static like "parsnip" in the above example or by using the ${} notation you can specify that the value can be taken from the 
launching form.  In the above example the question called "name" in the launched survey will get its initial value from the question called 
"qname".

.. note::

  When getting intial data from the launching form you can only refer to data in it's top level form.  That is not within a repeating group.

Update an existing Record
+++++++++++++++++++++++++

Available with Smap Server 24.01+ Only available with webforms.

You can specify the instance of the record to be updated as a parameter called "instance"::

  instance=${instance_to_update}

You can pass initial data, as described above, which will override the data pulled from the instance.

`Video showing how to edit an existing record from webforms <https://youtu.be/1POwyhSK5BI>`_

Tutorial - Launching a Parent Survey
------------------------------------

In this example the user will be filling out details on a pupil.  When it comes to adding the class, if the class does not exist, then 
they will launch the class form to add it and also to automatically add the pupil as being a member of that class.

1. First create a survey called "Class". Add some questions including a text question called class_id.  Edit the keys for this survey
and set the key to "${class_id}".

2. Using the online editor create a survey called "Pupil".  Add some questions that you might want to record about the pupil such as their
name.

3. Now in the Pupil form we are going to select the class attended by the pupil.  Add a question called "class" of type select_one and specify that it
get its choice list from the **Class** form.  This is great, if there is an existing class the Pupil can be assigned to it.  However if there is
not an existing class then we want to launch a survey to create that task and automatically assign our pupil to it.

.. note::

  The online editor will guide you through getting a choice list from another survey.  To do this edit the appearance for the select question
  and select the **search** tab.
  
4. Create a question of type select_one with a label "Is a new class needed?".  

5. Add a question of type "parent_form".  Make it relevant only if a new class is needed. Edit the parameters
to specify:

*  Survey to launch:  Set to "Class"
*  Question to store the returned key: Set this to the question in the Pupil form also called "class".

Sample surveys as described above can be downloaded from:

*  `Finished class survey <https://docs.google.com/spreadsheets/d/1oh6oH9dM3-Kvs1-mN-J2GbOEBI19byId-d_YxXBFHU8/edit?usp=sharing>`_
*  `Finished pupil survey <https://docs.google.com/spreadsheets/d/1skiRy3WimY-rPZM8msjTZV93l-qmbxv8Sf7Wn-n4PuU/edit?usp=sharing>`_

Testing
+++++++

*  Complete the **Class** survey a couple of times to add some classes.
*  Complete the **Pupil** survey and select an existing task.
*  Complete the **Pupil** survey and specify that a new class is needed.  Add a new class from within the **Pupil** survey.
*  Using the console drill down from each pupil to see details on the class that they are enrolled in.  This should work for
   all of the Pupils even those for whom a class was created at the same time as the pupil.
   
.. figure::  _images/launch3.png
   :align:   center
   :width: 	 600px
   :alt:     Drilling down to get the class details
   
   Drilling down to get the class details
   
*  Export the data collected for each survey into a spreadsheet.  You should see that the **class** question in the **Pupil**
   survey holds the **class_id** for all pupils.  Using spreadsheets this data would be difficult to combine however if you used
   a business intelligence tool you would be able to join the data from the two surveys using the class_id questions.
   
.. figure::  _images/launch4.png
   :align:   center
   :width: 	 300px
   :alt:     Class Data

   Class Data
   
.. figure::  _images/launch5.png
   :align:   center
   :width: 	 600px
   :alt:     Pupil Data

   Pupil Data
   
.. note::

  The Pupil data contains a value for the question that launched the class form. This question was called "launch" in the 
  example survey.  The value in this question is used by the Smap system during the linking of
  of the data in the two surveys and it can be ignored for analysis.
