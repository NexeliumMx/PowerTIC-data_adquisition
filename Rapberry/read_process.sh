#!/bin/bash

# Activate virtual environment
source /home/pi/MICO/.venv/bin/activate || { echo "Failed to activate virtual environment"; exit 1; }
path="/home/pi/MICO/PowerTIC-data_adquisition/Rapberry"

if [ "$PWD" != "$path" ]; then
    cd "$path" || exit
fi

# Run mainfun_copy.py
if ! ./Powertick.dist/Powertick.bin; then
    echo "Powertick.bin failed"
    exit 1
fi

echo "Script executed successfully"