#!/bin/bash

kill_process() {
    fuser $1
    fuser -k $1
    echo "Process in port $1 killed succesfully"
}

kill_process "$1"