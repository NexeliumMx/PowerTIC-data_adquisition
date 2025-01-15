import requests
import json
import os

# Azure Function endpoint URL
FUNCTION_URL = " https://power-tick-api-py.nexelium.mx/api/versioncheck?"



def post_blob_request(file_name):
    """
    Sends a POST request to the Azure Function to download a blob file.
    
    Args:
        file_name (str): The name of the blob file to download.

    Returns:
        bool: True if successful, False otherwise.
    """
    # Local file to save the downloaded blob content
    DOWNLOAD_PATH = f"./File_downloads/{file_name}"
    try:
        # JSON payload
        payload = {"file": file_name}

        # Send POST request
        response = requests.post(FUNCTION_URL, json=payload)

        # Check response status
        if response.status_code == 200:
            print(f"Blob '{file_name}' downloaded successfully.")
            
            # Save content to a local file
            with open(DOWNLOAD_PATH, "wb") as file:
                file.write(response.content)
            
            print(f"Blob content saved to: {os.path.abspath(DOWNLOAD_PATH)}")
            return True
        elif response.status_code == 400:
            print("Error: Bad Request. Make sure the file name is correct.")
            print("Response:", response.json())
        elif response.status_code == 404:
            print("Error: Blob not found.")
        else:
            print(f"Failed to download blob. Status code: {response.status_code}")
            print("Response:", response.text)
        return False

    except requests.RequestException as e:
        print(f"An error occurred while sending the request: {e}")
        return False

if __name__ == "__main__":
    # File name to download (update with a valid blob name from your container)
    blob_name = "Coms.py"

    # Call the POST request function
    success = post_blob_request(blob_name)

    if success:
        print("Blob processing completed.")
    else:
        print("Blob processing failed.")