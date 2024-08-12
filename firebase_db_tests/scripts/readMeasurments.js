import { readFile } from 'fs/promises';

// Path to the SQL file
const filePath = '../data/measurement_address.sql';

// Function to read the SQL file and print parameter descriptions
async function printParameterDescriptions() {
  try {
    // Read the file asynchronously
    const data = await readFile(filePath, 'utf8');

    // Split the file content into lines
    const lines = data.split('\n');

    console.log('Parameter Descriptions:');
    // Iterate over each line to find relevant parameter descriptions
    lines.forEach(line => {
      // Check if the line contains a parameter description
      if (/^\s*\d+/.test(line.trim())) {
        // Extract and print the parameter description
        const description = line.trim().split(/\s+/)[1];
        console.log(description);
      }
    });
  } catch (err) {
    console.error('Error reading the file:', err);
  }
}

// Call the function to print the parameter descriptions
printParameterDescriptions();