
Threads
=======

The "thread" of a record is the instanceid of the submission that first created the record.  Every time that record is updated
it will get a new instanceid but the thread will remain unchanged.  This can then be used to view the history of changes to a 
record.

History
-------

In the console when you view a record you can select the **history** tab to see the changes that been made to it.  Thread is also
included in the output of the data api.

Thread Created
--------------

The date that the record was first created is also recorded.  This is used in case management to trigger alerts if a case has not been closed
within a specified timeframe. 

