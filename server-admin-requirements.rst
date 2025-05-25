
Server Requirements
===================

.. contents::
 :local:

The following pre-requisites are required by the install script and the infrastructure components that it
installs.  You can modify this script yourself to use other Linux distros or for a different
chip architecture.

*  One of the following Ubuntu LTS Server versions

   *  24.04
   *  22.04
   *  20.04
   *  18.04

*  2GB of Memory
*  10GB of disk
*  Chip Architecture: X86

Small Server (2 GB RAM)
-----------------------

Max connections in postgresql.conf: 400

/var/lib/tomcat[x]/conf/context.xml

*  Max Active Survey Definitions: 60
*  Max Active Results: 60

/etc/default/tomcat[x]

*  JAVA_OPTS="-Djava.awt.headless=true -Xms768m -Xmx768m"

Medium Server (4 GB RAM)
------------------------

Max connections in postgresql.conf: 600

/var/lib/tomcat[x]/conf/context.xml

*  Max Active Survey Definitions: 100
*  Max Active Results: 100

/etc/default/tomcat[x]

*  JAVA_OPTS="-Djava.awt.headless=true -Xms2048m -Xmx3072m"

Large Server (8 GB RAM)
-----------------------

Max connections in postgresql.conf: 800

/var/lib/tomcat[x]/conf/context.xml

*  Max Active Survey Definitions: 120
*  Max Active Results: 120

/etc/default/tomcat[x]

*  JAVA_OPTS="-Djava.awt.headless=true -Xms4096m -Xmx4096m"

