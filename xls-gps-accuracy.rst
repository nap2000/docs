GPS Accuracy
============

By default a GPS reading will be recorded in FieldTask when the accuracy reaches 5 meters.  However you can specify
a different distance by adding a column to the xlsForm with heading: body::accuracyThreshold.  The user can also manually 
accept a lower accuracy if the GPS reading is taking a long time.  

.. csv-table:: GPS Accuracy:
  :width: 160
  :widths: 40,40,40,40
  :header-rows: 1
  :file: tables/accuracy.csv
  
.. note::

  GPS readings may take a long time to record if the device has a poor GPS receiver or there is a lot of interference 
  from buildings or sometimes even trees.
  


