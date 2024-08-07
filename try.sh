#!/bin/bash
shell=True
exec 3>&1 1>"log.log" 2>&1
pkill -9 -f deploy.py
cd ~
cd MICO/PowerTIc/PowerTIC
git remote set-url origin git@github.com:AVargas-C/PowerTIC.git
git pull
echo 'MAMO'
git checkout JSOTA
git pull
echo "update success"
source .venv/bin/activate
python Rapberry/deploy.py
