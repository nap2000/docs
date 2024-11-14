.. _server-problems:

Customisation
=============

.. contents::
 :local:

You can add your own code to override the contents of a Smap distribution.  These should be placed in a directory called
"custom" in the location where you unzipped the tar file.

Web Pages
---------

Under the custom directory add "/web".  The contents of this directory will overwrite the web files that are copied to /var/www/smap/.  A good place to start would be to copy
/var/www/smap/index.html to /web and then edit it.  You can add other html files, javascript files and css files remembering to mirror
the directory structure under /var/www/smap

