Recovering from submitting data to an old survey version
========================================================

.. contents::
 :local:
 
Situation
---------

A common issue that people find themselves in is that an enumerator has used an old deleted version of a survey and cannot submit the data.

Solution
--------

Don't get into this situation in the first place!
+++++++++++++++++++++++++++++++++++++++++++++++++

Ok this is easier said than done.  However using an old version of a survey will presumably have some impact on data quality.  So before
your enumerators start collecting data and while they have access to wi-fi make sure they all press the **refresh** button in fieldTask.
Downloading of changed surveys should then complete without error and they are ok to go.

Mitigate the impact
+++++++++++++++++++

If you have already started collecting data and you need to make a change then you can **replace** (:ref:`replacing-surveys`) the survey rather than deleting it and
creating a new one.  This way the data that you have already collected is preserved.  You can also use **replace** while you are 
developing your survey so that if an enumerator ends up using the wrong version they can still upload the data.

Recovering
++++++++++

Ok so if neither of the above two solutions apply we need to recover.  

*  Presumably the old survey is deleted so you will need to un-delete it.  (:ref:`restoring-surveys`).  Deleted surveys are called by their original name
   and then the date and time (UTC) that they were deleted.  You may need to try undeleting a few old versions before you find the one that 
   the enumerator was using.

*  Once the survey is undeleted the enumerator should be able to refresh and send all their data. You can view the data submitted in analysis.  But this data
   is not in the same table as the rest of your data.  In fact as far as the system is concerned this old survey is completely different from the current
   version.

*  The next step is to backup the data from the old survey and import it into the current survey.  (:ref:`backup-import`)
   Make sure you do not select the checkbox to replace the data.
