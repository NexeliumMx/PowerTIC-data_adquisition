
import json
from azure.storage.blob import BlobServiceClient
import subprocess
from datetime import datetime
import requests

# Path to your Bash script
bash_script_path = "./version_update.sh"





OUTPUT_JSON_FILE = "version.json"
input_json = "version.json"


def run_bash_script(script_path):
    """Run a Bash script using subprocess."""
    try:
        result = subprocess.run(["bash", script_path], capture_output=True, text=True, check=True)
        print("Script Output:")
        print(result.stdout)
        if result.stderr:
            print("Script Error Output:")
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running the script: {e}")
        print("Error Output:")
        print(e.stderr)

def read_json_from_file(input_json):
    print(f"extracting data from: ", input_json)
    """Reads and returns data from the specified JSON file."""
    try:
        with open(input_json, "r") as json_file:
            data = json.load(json_file)
            print("JSON data successfully loaded:")
            print(json.dumps(data, indent=4))
            return data
    except FileNotFoundError:
        print(f"Error: The file '{input_json}' was not found.")
        return False
    except json.JSONDecodeError:
        print(f"Error: The file '{input_json}' is not a valid JSON file.")
        return None
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
        return None

import requests
import json

def call_api():
    api_url = "https://power-tick-api-py.nexelium.mx/api/versioncheck"
    """Call an API and return the JSON response."""
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            print("API executed successfully.")
            api_response = response.json()  # Parse the JSON response
            print("Response from API:", json.dumps(api_response, indent=4))
            
            # Find the "Coms.py" file
            version_file = next((item for item in api_response if item["name"] == "Coms.py"), None)
            if version_file:
                print("Found version file (Coms.py):")
                print(json.dumps(version_file, indent=4))
            else:
                print("Version file not found.")
            
            # Find the "modbusrtu_commands.csv" file
            rtu_file = next((item for item in api_response if item["name"] == "modbusrtu_commands.csv"), None)
            if rtu_file:
                print("Found RTU file (modbusrtu_commands.csv):")
                print(json.dumps(rtu_file, indent=4))
            else:
                print("RTU file not found.")

            # Return the parsed data
            return api_response, rtu_file, version_file
        else:
            print(f"API execution failed. Status code: {response.status_code}. Response: {response.text}")
            return None
    except requests.RequestException as e:
        print(f"An error occurred during API execution: {e}")
        return None
    

def version_check(version_file):
    """Lists blob details, updates the JSON file if needed, and runs a Bash script."""
    stored_data = read_json_from_file(input_json=input_json)
    stored_version_date = None
   
    if stored_data and len(stored_data) > 0:
        try:
            stored_version_date = datetime.fromisoformat(stored_data['last_modified'])
            print(f"Stored Version Date: {stored_version_date}")
        except Exception as ex:
            print(f"Error parsing stored version date: {ex}")
    else:
        print("No valid stored data found. Proceeding with cloud data.")

    # Parse the cloud version date
    try:
        cloud_timestamp = version_file['last_modified']
        cloud_version_date = datetime.fromisoformat(cloud_timestamp)
        print(f"Cloud Version Date: {cloud_version_date}")
    except Exception as ex:
        print(f"Error parsing cloud version date: {ex}")
        return

    # Compare the stored version date with the cloud version date
    if not stored_version_date or stored_version_date < cloud_version_date:
        # Update the local JSON file
        with open(OUTPUT_JSON_FILE, "w") as json_file:
            json.dump(version_file, json_file, indent=4)
        print("Version data saved successfully to", OUTPUT_JSON_FILE)

        # Run the Bash script
        run_bash_script(bash_script_path)
    else:
        print("Local version is up-to-date.")

#if __name__ == "__main__":
 #   version_check()