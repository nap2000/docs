#!/bin/sh
sudo rm -rf /mnt/c/Program\ Files/Apache\ Software\ Foundation/httpd/Apache24/htdocs/docs/*
sudo cp -rf _build/html/* /mnt/c/Program\ Files/Apache\ Software\ Foundation/httpd/Apache24/htdocs/docs
tar -zcf docs.tgz _build/html
sudo mkdir /mnt/c/Program\ Files/Apache\ Software\ Foundation/httpd/Apache24/htdocs/docs/admin

