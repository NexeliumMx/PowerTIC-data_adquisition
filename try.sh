#!/bin/bash
shell=True
exec 3>&1 1>"log.log" 2>&1
pkill -9 -f deploy.py
cd ~
cd MICO/PowerTIC
git remote set-url origin git@github.com:AVargas-C/PowerTIC.git
ssh-agent -s
ssh-add /.ssh/id_ed25519
git stash 
git stash pop
git checkout OTA
git pull
echo 'MAMO'
echo "update success"
source .venv/bin/activate
python Rapberry/deploy.py & echo "running" && fg
