#!/bin/bash

# Activate virtual environment
source /home/pi/MICO/.venv/bin/activate || { echo "Failed to activate virtual environment"; exit 1; }
path="/home/pi/MICO/PowerTIC-data_adquisition/Rapberry"

if [ "$PWD" != "$path" ]; then
    cd "$path" || exit
fi
# Run modbus16bit.py
if ! python ./modbus16bit.py; then
    free -h
    echo "modbus16bit.py failed"
    exit 1
fi

echo "Port processes killed"

# Run ComsTest.py
if ! python ./ComsTest.py; then
    echo "ComsTest.py failed"
    exit 1
fi

echo "Script executed successfully"