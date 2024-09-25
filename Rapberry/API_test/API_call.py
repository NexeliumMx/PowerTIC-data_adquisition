import requests
import json
import os

def info_backup(data,file_path):
    file_path = r"PowerTIC/Raspberry_backup/clients.json"  # Corrected directory name
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    if not os.path.exists(file_path):
        # Write the data as a list
        with open(file_path, 'w') as f:
            json.dump([data], f, indent=4)
        print(f"Created {file_path} and backed up info.")
    else:
        # Read existing data
        with open(file_path, 'r') as f:
            try:
                existing_data = json.load(f)
            except json.JSONDecodeError:
                existing_data = []
        # Append new data
        existing_data.append(data)
        # Write back to the file
        with open(file_path, 'w') as f:
            json.dump(existing_data, f, indent=4)
        print(f"Data ({data}) was backed up successfully.")

# Define the data with your specific fields
data =[
    {
        "table": "clients"
    }, {
        "client": "SA de CV",
        "broker": "DEF",
        "cloud_services": False,
        "payment": True,
        "payment_amount": 1000
    }
]

# URL of the API endpoint
url = "https://powertic-apis-js.azurewebsites.net/api/sql_manager"
try:
    info_backup(data=data)
except Exception as e:
    print("Error: ", e)

try:
    response = requests.post(url, json=data)
    response.raise_for_status()  # Raises HTTPError if the status is 4xx, 5xx
    print('Success:', response.text)
    
except requests.exceptions.RequestException as e:
    print('HTTP Request failed:', e)

