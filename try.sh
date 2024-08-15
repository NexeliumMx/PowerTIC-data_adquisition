#!/bin/bash
shell=True
exec 3>&1 1>"log.log" 2>&1
pkill -9 -f deploy.py
cd ~
cd MICO/PowerTIC
git remote set-url origin git@github.com:AVargas-C/PowerTIC.git
git stash 
git stash pop
git checkout OTA
git pull
echo "update success"

