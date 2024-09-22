import requests
import json

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
    response = requests.post(url, json=data)
    response.raise_for_status()  # Raises HTTPError if the status is 4xx, 5xx
    print('Success:', response.text)
except requests.exceptions.RequestException as e:
    print('HTTP Request failed:', e)

