#!/bin/sh
sudo cp -rf _build/html/* /mnt/c/Program\ Files/Apache\ Software\ Foundation/httpd/Apache24/htdocs/docs
tar -zcf docs.tgz _build/html
mv docs.tgz ~/deploy

