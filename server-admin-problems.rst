.. _server-problems:

Diagnosing Problems
===================

.. contents::
 :local:

Five problems that will stop the server, or limit its usability, are:

*  Out of memory for the Tomcat application server (most likely)
*  Maxed out CPU
*  Out of local disk
*  Out of database resources
*  Hardware fault

Tomcat Out of Memory
--------------------

This is the most common problem that will stop the server.  You can find evidence of memory issues by:

Inspecting /var/log/syslog
++++++++++++++++++++++++++

Entries such as the following indicate an out of memory:

*  Under memory pressure, flushing caches
*  tomcat9.service: A process of this unit has been killed by the OOM killer
*  oom-kill:constraint=CONSTRAINT_NONE,nodemask=(null),cpuset=/,mems_allowed=0,global_oom,task_memcg=/system.slice/tomcat9.service,task=java,pid=2159900,uid=1001
*  Out of memory: Killed process 2159900 (java) total-vm:2774660kB, anon-rss:534720kB, file-rss:2824kB, shmem-rss:0kB, UID:1001 pgtables:1488kB oom_score_adj:0

Maxed Out CPU
-------------

*  apachetop  can be used to see what requests are currently adding load to the system

Out of local disk
-----------------

These can sneak up on you.  Especially if you have been doing text only surveys for a while and then 
start collecting images without specifying a reduced image size.  It will be resolved once you add more disk.

For my servers, when this happens, I use AWS S3 to store media attachments. There are multiple alternatives that provide
lower cost infinitely expandable storage.  To use S3 you will need to add AWS credentials that can access S3 to your 
server.  You can then add a file called "bucket" in /smap/settings that contains the name of the S3 bucket where your
attachments will be stored.  Further details can be found here: :ref:`disk-storage`
