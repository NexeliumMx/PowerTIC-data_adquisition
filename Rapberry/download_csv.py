import requests
import json
from  version_extraction import call_api, read_json_from_file
from datetime import datetime

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

def csv_version(rtu_file):
    OUTPUT_JSON_FILE = "modbusrtu_commands_version.json"
    input_json = "modbusrtu_commands_version.json"

    stored_data = read_json_from_file(input_json)
    stored_version_date = None
    print("Stored data: ", stored_data)
        
    if stored_data and len(stored_data) > 0:
        try:
            stored_version_date = datetime.fromisoformat(stored_data['last_modified'])
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
    # Compare the stored version date with the cloud version date
    if not stored_version_date or stored_version_date < cloud_version_date:
        # Update the local JSON file
        with open(OUTPUT_JSON_FILE, "w") as json_file:
            json.dump(rtu_file, json_file, indent=4)
        print("Version data saved successfully to", OUTPUT_JSON_FILE)

        # Run the Bash script
        download_csv()
    else:
        print("Local version is up-to-date.")

#if __name__ == "__main__":
 #  csv_version()
   #download_csv()