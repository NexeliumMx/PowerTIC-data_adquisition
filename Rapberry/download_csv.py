import requests

def download_csv():
    url = 'http://localhost:7071/api/csvDownload?model=acurev-1313-5a-x0'
    try:
        # Send a GET request to the API endpoint
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        filename = 'modbusqueries_acurev-1313-5a-x0.csv'

        # Save the response content to a CSV file
        with open(filename, 'w') as file:
            file.write(response.content)

        print(f"file downloaded successfully as '{filename}'.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while downloading the file: {e}")

if __name__ == "__main__":
    download_csv()