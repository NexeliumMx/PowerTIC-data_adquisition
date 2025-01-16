#!/bin/bash

# Define the log file
LOG_FILE="./execution_log.txt"

# Log the starting time
echo "Execution started at $(date)" >> $LOG_FILE

# Log the stat command output
echo "Checking initial file status..." >> $LOG_FILE
stat ./mainfun_copy.dist/Powertick.bin >> $LOG_FILE 2>&1

# Remove the file and log the result
echo "Removing file..." >> $LOG_FILE
rm ./mainfun_copy.dist/Powertick.bin >> $LOG_FILE 2>&1

# Execute the Python script and log its output
echo "Running image_download.py..." >> $LOG_FILE
python ./image_download.py >> $LOG_FILE 2>&1

# Log the success message
echo "File Downloaded successfully" >> $LOG_FILE

# Log the final stat command output
echo "Checking final file status..." >> $LOG_FILE
stat ./mainfun_copy.dist/Powertick.bin >> $LOG_FILE 2>&1
chmod ./mainfun_copy.dist/Powertick.bin >> $LOG_FILE 
# Log the ending time
echo "Execution ended at $(date)" >> $LOG_FILE

