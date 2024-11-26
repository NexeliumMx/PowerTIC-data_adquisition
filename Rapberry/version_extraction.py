import json
from azure.storage.blob import BlobServiceClient
import subprocess
from datetime import datetime
import requests

# Path to your Bash script
bash_script_path = "./version_update.sh"





OUTPUT_JSON_FILE = "version.json"
INPUT_JSON_FILE = "version.json"

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

def read_json_from_file():
    """Reads and returns data from the specified JSON file."""
    try:
        with open(INPUT_JSON_FILE, "r") as json_file:
            data = json.load(json_file)
            print("JSON data successfully loaded:")
            print(json.dumps(data, indent=4))
            return data
    except FileNotFoundError:
        print(f"Error: The file '{INPUT_JSON_FILE}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file '{INPUT_JSON_FILE}' is not a valid JSON file.")
        return None
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
        return None

def call_api(api_url, params=None):
    """Call an API and return the JSON response."""
    try:
        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            print("API executed successfully.")
            return response.json()
        else:
            print(f"API execution failed, status code: {response.status_code}. Response: {response.text}")
            return None
    except requests.RequestException as e:
        print(f"An error occurred during API execution: {e}")
        return None

def list_blob_details():
    """Lists blob details, updates the JSON file if needed, and runs a Bash script."""
    stored_data = read_json_from_file()
    stored_version_date = None

    api_url = "power-tick-api-py.nexelium.mx/api/versioncheck?"

    # Call the API
    api_response = call_api(api_url)
    if not api_response:
        print("No data returned from the API.")
        return

    print("Response from API:", json.dumps(api_response, indent=4))

    if stored_data and len(stored_data) > 0:
        try:
            stored_version_date = datetime.fromisoformat(stored_data[0]['last_modified'])
            print(f"Stored Version Date: {stored_version_date}")
        except Exception as ex:
            print(f"Error parsing stored version date: {ex}")
    else:
        print("No valid stored data found. Proceeding with cloud data.")

    # Parse the cloud version date
    try:
        cloud_timestamp = api_response[0]['last_modified']
        cloud_version_date = datetime.fromisoformat(cloud_timestamp)
        print(f"Cloud Version Date: {cloud_version_date}")
    except Exception as ex:
        print(f"Error parsing cloud version date: {ex}")
        return

    # Compare the stored version date with the cloud version date
    if not stored_version_date or stored_version_date < cloud_version_date:
        # Update the local JSON file
        with open(OUTPUT_JSON_FILE, "w") as json_file:
            json.dump(api_response, json_file, indent=4)
        print("Version data saved successfully to", OUTPUT_JSON_FILE)

        # Run the Bash script
        run_bash_script(bash_script_path)
    else:
        print("Local version is up-to-date.")

if __name__ == "__main__":
    list_blob_details()