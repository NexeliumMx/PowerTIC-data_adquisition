import time
import json
from azure.iot.device import IoTHubDeviceClient, Message

# Azure IoT Hub setup
CONNECTION_STRING = 'HostName=Powertic.azure-devices.net;DeviceId=Raspberry_pi5-8;SharedAccessKey=gfGS5hFLrLy7jMf17Vq6XQ/kaUiIaPA7YAIoTGYVBHU='
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

sending_message = False
message_id = 0

def get_message():
    global message_id
    message_id += 1
    
    # Replace these with actual data if needed
    temperature = 25.0  # Placeholder temperature value
    humidity = 50.0     # Placeholder humidity value
    
    message = {
        "messageId": message_id,
        "deviceId": "Raspberry Pi Web Client",
        "temperature": temperature,
        "humidity": humidity
    }

    temperature_alert = temperature > 30
    return json.dumps(message), temperature_alert

def send_message():
    if not sending_message:
        return

    content, temperature_alert = get_message()
    message = Message(content)
    message.custom_properties["temperatureAlert"] = str(temperature_alert)

    print("Sending message: " + content)
    try:
        client.send_message(message)
        print("Message sent to Azure IoT Hub")
    except Exception as e:
        print("Failed to send message to Azure IoT Hub: " + str(e))

def on_start():
    global sending_message
    print("Starting message sending...")
    sending_message = True

def on_stop():
    global sending_message
    print("Stopping message sending...")
    sending_message = False

def receive_message_callback(message):
    print("Received message: " + message.data.decode())

# Attach the callbacks
client.on_message_received = receive_message_callback

# Start the client
client.connect()

# Start sending messages every 2 seconds
try:
    while True:
        if sending_message:
            send_message()
        time.sleep(2)
except KeyboardInterrupt:
    pass

finally:
    client.shutdown()