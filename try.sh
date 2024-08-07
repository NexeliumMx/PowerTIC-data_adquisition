#!/bin/bash
shell=True
exec 3>&1 1>"log.log" 2>&1
cd ~
cd MICO/PowerTIc/PowerTIC
git remote set-url origin git@github.com:user/repo.git
git pull https://github.com/AVargas-C/PowerTIC
echo 'MAMO'
git checkout JSOTA
git pull
echo "update success"
source .venv/bin/activate
python Rapberry/deploy.py
