#!/bin/bash

# Activate virtual environment
source venv/bin/activate || { echo "Failed to activate virtual environment"; exit 1; }


# Run mainfun_copy.py
if ! ./Powertick.bin; then
    echo "Powertick.bin failed"
    exit 1
fi

echo "Script executed successfully"