.. _survey_keys:

Survey Keys
===========

Keys uniquely identify a record of data which can represent a "case". More generally the record can be linked
to a "real" thing such as a person, some infrastructure or a complaint.  Then if a second record is submitted 
with the same key, it will be combined with the existing data in a manner determined by the key policy. 

These can be constructed automatically from the answers to questions in the
survey.  A very simple case is when the key is recognised externally to Smap.  For example an identify number.  Then the key 
could be specified as::

  ${id_no}
  
Once you have specified a key then you can specify a **key policy** for your survey. 

Survey Key Policy
-----------------

none
++++ 

This is the default policy.  New records are simply appended even if that creates a duplicate key.

merge
+++++ 

Any submissions that match an existing record using the key will be merged.  That is the data in the 
new record will replace the old record except where the question in the new record was not answered. Then the old
data will be retained. For Example.

Old record::

  id: 1
  name: Tom
  age: 20
  Address: 5 Smith St.
  
New submission::

  id:  1
  name: Tom
  age:  21
  Address:
  
Results in::

  id: 1
  name: Tom
  age: 21
  Address: 5 Smith St.
  
Discard
+++++++

The new record will be discarded.  This prevents updates to records so should probably not be a common option.
It can be used when you want the first record submitted for a key to be the authoratative record.

Replace
+++++++

Similar to discard but this time the original record is replaced by the new one.

Specifying keys
---------------

Generating a unique key
+++++++++++++++++++++++

If you don't have an external unique key that you can use then you can generate one from the data in the record, For example::

  ${country}-${name}
  
Unique keys with a serial number
++++++++++++++++++++++++++++++++

Sometimes there is not enough information in a survey to guarantee a unique key.  In this case you can use the serial() function
to guarantee that a submission will be unique. For example::

  ${name} serial(50)   

The above serial function will add a unique number to every record starting from 50.

.. note::

  Using serial will make the key policy redundant for new submissions because every new submission will be unique.  
  However these keys can be used as references since they are a unique identifier for a record that can be more 
  human readable than the primary key. 
  
Specifying a non unique sequence number
+++++++++++++++++++++++++++++++++++++++

You may want a sequence number to be created starting from 1 each time another question response changes.
For example a new sequence number for each product::

  product_a-1
  product_a-2
  product_b-1
  product_a-3

These can be generated using the seq() function::

  ${product}-seq(product)

The function takes a single parameter which is the question name that determine whose values will determine 
the sequence.  So in the product example there are 3 product_a records.  The next time a record for product_a
is submitted the sequence number will be 4.  The next time a product_b record is submitted the sequence number
will be 2.

Specifying the key and key policy
---------------------------------

In the online editor select the menu **File** then **Keys**

In the XLSForm editor use the settings sheet.

*  The key goes under the heading **key**
*  The key policy goes under the heading **key_policy**

Direct Updates
--------------

A record can be selected to be updated directly either in a task or directly from the console or analysis page.  In this case the old record is
always replaced.  This happens even if the survey has a key and a different key policy such as "merge".
