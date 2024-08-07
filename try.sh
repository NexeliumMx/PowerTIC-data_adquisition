#!/bin/bash
shell=True
sleep 10s
git pull
echo "update success"
python deploy.py

fi
