#!/bin/bash

# Activate virtual environment
source /home/pi/MICO/.venv/bin/activate || { echo "Failed to activate virtual environment"; exit 1; }

# Run modbus16bit.py
if ! python ./modbus16bit.py; then
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