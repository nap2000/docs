.. _fieldtask-api:

FieldTask APIs
==============

.. contents::
 :local:

Introduction
------------

To start a FieldTask activity:

1. Create a new intent using an appropriate action.
2. Set the type of the created intent.
3. Start an activity using the intent.

.. _form-instance-list:

Launching the form list
-----------------------
 
.. code-block:: java
 	
  Intent intent = new Intent(Intent.ACTION_VIEW);
  intent.setType("vnd.android.cursor.dir/vnd.odk.form");
  startActivity(intent);
 
This displays a list of forms and allows the user to select one and fill it in.
 
Launching the instance list
---------------------------

.. code-block:: java
 
  Intent intent = new Intent(Intent.ACTION_VIEW);
  intent.setType("vnd.android.cursor.dir/vnd.odk.instance");
  startActivity(intent);

This displays a list of saved forms and allows the user to select one and edit it.

Getting the URI of a form or instance chosen by the user
--------------------------------------------------------

.. code-block:: java
 
  Intent intent = new Intent(Intent.ACTION_PICK);
  intent.setType("vnd.android.cursor.dir/vnd.odk.form");

.. code-block:: java
 
  static final int PICK_FORM_REQUEST = 1;  // The request code
  startActivityForResult(intent, PICK_FORM_REQUEST);
 
To get the result, override ``onActivityResultMethod`` in the following way:

.. code-block:: java

  @Override
  protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    // Check which request we're responding to
    if (requestCode == PICK_FORM_REQUEST) {
      // Make sure the request was successful
      if (resultCode == RESULT_OK) {
        // The Intent's data URI identifies which form was selected.
        Uri formUri = data.getData();
        // Do something with the form here
      }
    }
  }

For an instance, change the intent type:
 
.. code-block:: java
 
  intent.setType("vnd.android.cursor.dir/vnd.odk.instance");

.. _use-form-uri:

Using a URI to edit a form or instance
--------------------------------------
 
If the URI of a form or instance is known, it can be viewed or edited. For example, a URI received in ``onActivityResult()`` as described above can be used.
 
.. code-block:: java
 
  Intent intent = new Intent(Intent.ACTION_EDIT);
  intent.setData("content://org.odk.collect.android.provider.odk.forms/forms/2");
  startActivity(intent);
 
The same thing can be done with a specific instance.
