.. _creating-external-app:

Creating an External App
========================

.. contents::
 :local:

This documentation assumes that you are using Android Studio and developing your app in Java.  To launch the app refer to

.. seealso:: :doc:`external-applications`

Create Project
--------------

*  In Android Studio click on the menu  "File" -> "New" -> "New Project"
*  Select "Empty Views Activity"
*  Specify Java as the language and set the project name etc.
*  Click "Finish"

Add an Activity that responds to an Intent from FieldTask
---------------------------------------------------------

Add an activity to the project, for example ``MainActivity``, and in ``AndroidManifest.xml`` give it an intent
filter with an action name of your own choosing::

  <activity
      android:name=".MainActivity"
      android:exported="true">
      <intent-filter>
          <action android:name="org.example.myapp.GET_VALUE" />
          <category android:name="android.intent.category.DEFAULT" />
      </intent-filter>
  </activity>

The action name is what goes after ``ex:`` in the appearance of the question, for example
``ex:org.example.myapp.GET_VALUE(type='text')``.  ``android:exported="true"`` is required so that fieldTask
can start the activity.

In onCreate, of the activity, get any parameters passed from fieldTask::

  Intent intent = getIntent();
  String type = intent.getStringExtra("type");   // Get the value of parameter "type"

Then your activity can do its magic and get a value to return. So at the end of onCreate
return this value to fieldTask.  Case 1 returning a text value::

  Intent returnIntent = new Intent();
  returnIntent.putExtra("value", "The text value to be returned");
  setResult(Activity.RESULT_OK, returnIntent);
  finish();



Case 2 returning an image, for a question of type image.  Save the image to a file, share it through a
``FileProvider`` and return its URI in the clip data of the result::

  Uri uri = FileProvider.getUriForFile(this, "org.example.myapp.fileprovider", imageFile);
  Intent returnIntent = new Intent();
  returnIntent.setClipData(ClipData.newRawUri("image.png", uri));
  returnIntent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
  setResult(Activity.RESULT_OK, returnIntent);
  finish();

The ``FileProvider`` has to be declared in the manifest with ``android:grantUriPermissions="true"`` so that
fieldTask is allowed to read the file.
