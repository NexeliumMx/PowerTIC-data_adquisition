/**
 * Author: Arturo Vargas Cuevas
 * Last Modified: 2024-09-06, by Arturo Vargas Cuevas
*/

import pkg from 'pg';
const { Client } = pkg;

// PostgreSQL database connection configuration
const client = new Client({
  user: 'superadmin', // Your PostgreSQL username
  host: 'powerticpgtest1.postgres.database.azure.com',
  database: 'powerticapp', // The correct database name
  password: 'vafja6-hexpem-javdyN', // Your PostgreSQL password
  port: 5432, // PostgreSQL default port
  ssl: {
    rejectUnauthorized: false // Azure uses trusted SSL certificates
  }
});

// Export the client to be used in other files
export default client;