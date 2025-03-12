#!/bin/bash

# Run Powertick.bin
if ! ./Powertick.bin; then
    echo "Powertick.bin failed"
    exit 1
fi

echo "Script executed successfully"
