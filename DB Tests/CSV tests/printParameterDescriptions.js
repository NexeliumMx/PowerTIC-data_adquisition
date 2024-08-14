// measurement_address.js
// This script reads a selected CSV file and prints all values under the "parameter_description" column.

import fs from 'fs';
import path from 'path';
import csv from 'csv-parser';
import readline from 'readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function printParameterDescriptions(filePath) {
    const parameterDescriptions = [];

    fs.createReadStream(filePath)
        .pipe(csv())
        .on('data', (row) => {
            const description = row['parameter_description'];
            if (description && description.trim()) {
                parameterDescriptions.push(description);
            }
        })
        .on('end', () => {
            console.log('Parameter Descriptions:');
            parameterDescriptions.forEach(description => {
                console.log(description);
            });
            rl.close();
        });
}

function askUserForFile() {
    rl.question('Which CSV file do you want to read?\n1 readings_addresses.csv\n2 device_info_addresses.csv\nType 1 or 2: ', (answer) => {
        let filePath;

        switch (answer.trim()) {
            case '1':
                filePath = path.join(process.cwd(), 'readings_addresses.csv');
                break;
            case '2':
                filePath = path.join(process.cwd(), 'device_info_addresses.csv');
                break;
            default:
                console.log('Invalid selection. Please type 1 or 2.');
                rl.close();
                return;
        }

        printParameterDescriptions(filePath);
    });
}

// Start the process by asking the user which file to read
askUserForFile();