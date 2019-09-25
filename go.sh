#!/bin/sh
make html
sudo cp -rf _build/html/* /mnt/c/Program\ Files/Apache\ Software\ Foundation/httpd/Apache24/htdocs/docs

