import time
import datetime
from dotenv import dotenv_values
from azure.iot.device import IoTHubDeviceClient, Message

cn='HostName=powertic.azure-devices.net;DeviceId=Raspberry;SharedAccessKey=y/se5ABBrwX2kVXpG3i87JW2YK5ma/asgqoZDACkQVg='


CONNECTION_STRING = cn

#Payload definition
MSG_SND = '{{"timestr": {timestr}}}'
#IoT Hub Client definition
def iothub_client_init():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

#Send telemetry

def iothub_client_telemetry():
    try:
        client = iothub_client_init()
        print("Sending telemetry to IoT Hub")
        while True:
            print("Active connection")
            time1 = datetime.datetime.now()
            timestr = time1.strftime("%d/%m/%Y %H:%M:%S")
            msg_txt_formatted = MSG_SND.format(timestr=timestr)
            message = Message(msg_txt_formatted)
            print("Sending message: {}".format(message) )
            client.send_message(message)
            print( "Message succesfully sent" )
            time.sleep(1)
    except KeyboardInterrupt:
        print("Connection stopped")

iothub_client_telemetry()
