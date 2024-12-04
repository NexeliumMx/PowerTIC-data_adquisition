#!/bin/bash
python ./modbus16bit.py
echo "Port processes killed"
source /home/pi/MICO/.venv/bin/activate
python ./ComsTest.py