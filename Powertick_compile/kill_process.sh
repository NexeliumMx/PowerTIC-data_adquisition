#!/bin/bash

kill_process() {
    local port=$1

    # Get the processes using the specified port
    pids=$(fuser $port 2>/dev/null)

    # Loop through each PID and check if it should be killed
    for pid in $pids; do
        # Get the command name of the process
        cmd=$(ps -p $pid -o comm=)

        # Skip Python processes
        if [[ $cmd == "python" ]]; then
            echo "Skipping Python process (PID: $pid) using port $port"
        else
            echo "Killing process (PID: $pid, Command: $cmd) using port $port"
            kill -9 $pid
        fi
    done

    echo "Finished processing port $port"
}

# Check if a port was provided
if [[ -z "$1" ]]; then
    echo "Usage: $0 <port>"
    exit 1
fi

kill_process "$1"