.. _creating-external-app:

Creating an External App
========================

.. contents::
 :local:

This documentation assumes that you are using Android Studio and developing your app in Java.

Create Project
--------------

*  In Android Studio click on the menu  "File" -> "New" -> "New Project"
*  Select "Empty Views Activity"
*  Specify Java as the language and set the project name etc.
*  Click "Finish"

Add an Activity that responds to an Intent from FieldTask
---------------------------------------------------------

Add an Intent to your manifest to start the activity

Add the activity

In onCreate, of the activity, get any parameters passed from fieldTask::

  Intent intent = getIntent();
  String type = intent.getStringExtra("type");   // Get the value of parameter "type"

Then your activity can do its magic and get a value to return. So at the end of onCreate
return this value to fieldTask.  Case 1 returning a text value::

  Intent returnIntent = new Intent();
  returnIntent.putExtra("value", "The text value to be returned");
  setResult(Activity.RESULT_OK, returnIntent);
  finish();


