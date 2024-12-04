#!/bin/bash
source /home/pi/MICO/.venv/bin/activate
python ./modbus16bit.py
echo "Port processes killed"
python ./ComsTest.py