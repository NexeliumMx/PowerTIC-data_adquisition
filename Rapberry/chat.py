from pymodbus.client import ModbusSerialClient
from pymodbus.pdu import ModbusRequest, ModbusResponse, ModbusExceptions
from pymodbus.exceptions import ModbusException
import struct
import logging

# Enable logging for debugging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# Custom Modbus Response
class CustomModbusResponse(ModbusResponse):
    function_code = 3  # Function code 3 (Read Holding Registers)

    def __init__(self, values=None, **kwargs):
        super().__init__(**kwargs)
        self.values = values or []

    def encode(self):
        # Build the response PDU
        byte_count = len(self.values) * 2
        result = struct.pack(">B", byte_count)
        for value in self.values:
            result += struct.pack(">H", value)
        return result

    def decode(self, data):
        # Decode the response PDU
        byte_count = data[0]
        self.values = []
        for i in range(1, 1 + byte_count, 2):
            self.values.append(struct.unpack(">H", data[i:i+2])[0])

    def __str__(self):
        return f"CustomModbusResponse(values={self.values})"

# Custom Modbus Request
class CustomModbusRequest(ModbusRequest):
    function_code = 3  # Function code 3 (Read Holding Registers)

    def __init__(self, address=None, count=1, **kwargs):
        super().__init__(**kwargs)
        self.address = address
        self.count = count

    def encode(self):
        # Build the request PDU
        return struct.pack(">HH", self.address, self.count)

    def decode(self, data):
        # Decode the request PDU
        self.address, self.count = struct.unpack(">HH", data)

    def __str__(self):
        return f"CustomModbusRequest(address={self.address}, count={self.count})"

# Create ModbusSerialClient for RTU
client = ModbusSerialClient(
    port='/dev/ttyUSB0',
    baudrate=19200,
    parity='N',
    stopbits=1,
    bytesize=8,
    timeout=5
)

if client.connect():
    print("Connected to Modbus RTU slave.")
else:
    print("Failed to connect to Modbus RTU slave.")
    exit(1)

# Register the custom response class with the client's decoder
client.framer.decoder.register(CustomModbusResponse)

# Prepare and send the custom request
slave_id = 1
start_address = 523  # Starting register address
register_count = 16  # Number of registers to read

try:
    # Create the custom request
    request = CustomModbusRequest(address=start_address, count=register_count, unit=slave_id)
    
    # Send the request and receive the response
    response = client.execute(request)

    # Process the response
    if isinstance(response, CustomModbusResponse):
        print(f"Received response: {response}")
        print(f"Values: {response.values}")
    elif response.isError():
        print(f"Error received: {response}")
    else:
        print(f"Unexpected response: {response}")

except ModbusException as e:
    print(f"Modbus exception occurred: {e}")
except Exception as e:
    print(f"General exception occurred: {e}")
finally:
    client.close()