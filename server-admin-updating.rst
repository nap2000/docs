
Updating
========

.. contents::
 :local:

::

  rm -rf old
  mv smap old
  rm *.tgz
  wget {link to tar file}
  tar -zxf {tar file}
  cd smap/deploy
  sudo ./patchdb.sh
  sudo ./deploy.sh

patchdb will update the database.  deploy.sh will replace the programs.  When you run deploy it will cause an outage of around 20 seconds for your users.
