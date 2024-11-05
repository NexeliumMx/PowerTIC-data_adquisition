import os
import json
import requests
def uploadbackup():
    files=os.listdir(r"vals/nfail")
    url = "https://powertic-api.azurewebsites.net/api/pushdata"
    for i in files:
        temp=open(rf'vals/nfail/{i}')
        data=json.load(temp)
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                print('Success')
                f=open(rf'vals/success/{i}.json',"x")
                f.write(data) 
                f.close()
                os.remove(rf'vals/nfail/{i}')
            else:
                print('Error:', response.status_code, response.text)
                f=open(rf'vals/apifail/{i}.json',"x")
                f.write(data)
                
                f.close()
        except requests.exceptions.RequestException as e:
                return None