#!/bin/bash

# Define the required execution path as a variable
REQUIRED_PATH="/home/powertick/Powertickexe"

# Check if current directory is the required path
if [ "$(pwd)" != "$REQUIRED_PATH" ]; then
    echo "Not in the correct directory. Changing to $REQUIRED_PATH..."
    cd "$REQUIRED_PATH" || {
        echo "Failed to change to the required directory"
        exit 1
    }
fi

# Run Powertick.bin
if ! ./Powertick.bin; then
    echo "Powertick.bin failed"
    exit 1
fi

echo "Script executed successfully"