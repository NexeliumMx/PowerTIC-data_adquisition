import requests
import json

# Define the data with your specific fields
data = {
    "client": 'ABC',         # Replace with actual client data
    "broker": 'DEF',         # Replace with actual broker data
    "cloud_services": False,     # Replace with actual cloud service data
    "payment": True,             # Replace with actual payment data
    "payment_amount": 1000      # Replace with actual payment amount
}

# URL of the API endpoint
url = "https://powertic.azurewebsites.net/api/sql_api"

# Send the POST request with the JSON-encoded data
response = requests.post(url, json=data)

# Check the response
if response.status_code == 200:
    print('Success:')  # If the response is in JSON format
else:
    print('Error:', response.status_code, response.text)