import requests
import json
from  version_extraction import call_api, read_json_from_file
from datetime import datetime

api_url = "https://power-tick-api-py.nexelium.mx/api/versioncheck?"
OUTPUT_JSON_FILE = "version.json"
INPUT_JSON_FILE = "version.json"

def download_csv():
    url = 'https://powertick-api-py.azurewebsites.net/api/downloadModbusRTUcsv?model=acurev-1313-5a-x0'
    try:
        # Send a GET request to the API endpoint
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        filename = 'modbusrtu_commands.csv'
        print(response.content)
        # Save the response content to a CSV file
        with open(filename, 'wb') as file:
            file.write(response.content)

        print(f"file downloaded successfully as '{filename}'.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while downloading the file: {e}")

def csv_version():
    stored_data = read_json_from_file()
    api_response = call_api(api_url=api_url)

    if not api_response:
        print("No API response.")
        return
    print("Response from API:", json.dumps(api_response, indent=4))
    rtu_file = next(item for item in api_response if item["name"] == "modbusrtu_commands.csv")
    if rtu_file:
        print("modbusrtu_commands.csv\n", json.dumps(rtu_file, indent=4))
    else:
        print("RTU file not found")
        return
    
    if stored_data and len(stored_data) > 0:
        try:
            stored_version_date = datetime.fromisoformat(stored_data[0]['last_modified'])
            print(f"Stored Version Date: {stored_version_date}")
        except Exception as ex:
            print(f"Error parsing stored version date: {ex}")
    else:
        print("No valid stored data found. Proceeding with cloud data.")

    try:
        cloud_timestamp = rtu_file['last_modified']
        cloud_version_date = datetime.fromisoformat(cloud_timestamp)
        print(f"Cloud Version Date: {cloud_version_date}")
    except Exception as ex:
        print(f"Error parsing cloud version date: {ex}")
        return

if __name__ == "__main__":
   csv_version()
   #download_csv()