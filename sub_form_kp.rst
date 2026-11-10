Sub Form Key Policy
===================

If you have a survey with a key and a key policy of, for example, "merge",  then you may not always want sub forms or repeating groups
to be treated the same way as the main form.

.. note::

  When a submitted record has the same key as an existing record, the Sub form key policy has no effect unless the
  :ref:`survey_keys` policy is set to "merge" or "replace".  When an existing record is edited the Sub form key policy always applies.

Using
-----

Set as a parameter called "key_policy on a question of type "begin repeat". This parameter can have one of 3 values

#.  **replace**.  Each record in the sub-form is progressively merged with records previously recorded
#.  **merge**, Each record previously recorded is merged with the new records.  
    Unlike "replace", if the new record has an unanswered question then the previous answer will be kept
#.  **append**. Records in the subform are appended to the existing sub-form records. 


For example::

  key_policy=merge
  key_policy=replace
  key_policy=append

Defaults
++++++++

If you don't specify a key policy for a subform then the default is applied.  This default depends on whether the submitted survey was
an edit of an existing record or just happened to have the same key as an existing record.

#.  Editing an existing record.  This is a record edited in the webform, a task that updates a record, or a later form in a case
    management process.  The existing sub form records were loaded into the form, so the sub form records that are submitted replace
    them.  Rows that were not changed are kept, and rows that were deleted in the form are removed.  The exception is a sub form
    with an "instance_count" parameter, as then only some of the existing records were loaded.  Here the survey key policy
    applies: "replace" replaces them, otherwise the submitted records are appended.

#.  Submitted record happens to have the same key as an existing record.  In this case the user did not have access to the existing sub form
    records hence it seems reasonable to just append the new new records.


Example 1 - Append sub form records
-----------------------------------

  *  You have a survey that is used to manage equipment.
  *  If a new photograph of that equipment is taken, (in the main form) then you want that to replace the existing photo.
  *  So a key of the equipment id is specified with a key policy of "merge".
  *  However each time you use the survey you want to record a new meter reading and append it to all the other readings.
  *  In this case you can put the meter reading in a "begin repeat" group and leave the sub form key policy unspecified (none) or set to "append"
     which will append new records.

Example 2 - Merge sub form records
----------------------------------

This example is based on the `medical clinics product <http://www.smap.com.au/medicalclinics.shtml>`_ 

  *  A survey is used by a doctor to prescribed medication to a patient during a consultation.  Each consultation is recorded in a sub form.
  *  A second survey then updates the data in the sub form to indicate which medications were dispensed
  *  Set the survey key of both surveys to the patient identifier.  This is specified in the survey settings.
  *  Set the survey key policy on both surveys to merge.  
  *  In the second dispensing survey, add the parameter "key_policy=merge" to the **begin repeat** that contains the results of the consultation.

