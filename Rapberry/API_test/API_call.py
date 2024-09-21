import requests
import json

# Define the data with your specific fields
data =[
    {
        "table": 'clients'
    }, {
        "client": 'HI',         # Replace with actual client data
        "broker": 'DEF',         # Replace with actual broker data
        "cloud_services": False,     # Replace with actual cloud service data
        "payment": True,             # Replace with actual payment data
        "payment_amount": 1000      # Replace with actual payment amount
    }
]

# URL of the API endpoint
url = "https://powertic-apis-js.azurewebsites.net/api/sql_manager"

try:
    response = requests.post(url, json=data)
    response.raise_for_status()  # Raises HTTPError if the status is 4xx, 5xx
    print('Success:', response.text)
except requests.exceptions.RequestException as e:
    print('HTTP Request failed:', e)