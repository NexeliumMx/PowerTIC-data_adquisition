#!/bin/bash
sh ./kill_process.sh
echo "Port processes killed"
source /home/pi/MICO/.venv/bin/activate
python "./ComsTest.py"