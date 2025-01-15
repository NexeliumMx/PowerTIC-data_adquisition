#!/bin/bash

# Activate virtual environment
source /home/pi/MICO/.venv/bin/activate || { echo "Failed to activate virtual environment"; exit 1; }
path="/home/pi/MICO/PowerTIC-data_adquisition/Rapberry"

if [ "$PWD" != "$path" ]; then
    cd "$path" || exit
fi

# Run mainfun_copy.py
if ! python ./mainfun_copy.py; then
    echo "mainfun_copy.py failed"
    exit 1
fi

echo "Script executed successfully"