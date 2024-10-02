from pymodbus.client import ModbusTcpClient, ModbusSerialClient
from pymodbus.pdu import ModbusRequest, ModbusResponse
from pymodbus.exceptions import ModbusException
from pymodbus.factory import ClientDecoder
from pymodbus.transaction import ModbusRtuFramer  # For RTU
from pymodbus.constants import Defaults

class WriteRegistersWithFunctionCode03Request(ModbusRequest):
    function_code = 0x03  # Custom use of function code 0x03

    def __init__(self, address, values, **kwargs):
        super().__init__(**kwargs)
        self.address = address
        self.values = values  # List of register values

    def encode(self):
        # Build the request payload
        result = b''
        result += self.address.to_bytes(2, byteorder='big')  # Start address
        result += len(self.values).to_bytes(2, byteorder='big')  # Quantity of registers
        for value in self.values:
            result += value.to_bytes(2, byteorder='big')  # Register values
        return result

    def decode(self, data):
        pass  # No need to decode request on client side

    def get_response_pdu_size(self):
        # Size of the response PDU (function code + data)
        # Adjust based on expected response size
        return 5  # For example
    
class WriteRegistersWithFunctionCode03Response(ModbusResponse):
    function_code = 0x03  # Must match the request's function code

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.address = None
        self.quantity = None

    def encode(self):
        # Build the response payload
        result = b''
        result += self.address.to_bytes(2, byteorder='big')
        result += self.quantity.to_bytes(2, byteorder='big')
        return result

    def decode(self, data):
        # Decode the response data
        self.address = int.from_bytes(data[0:2], byteorder='big')
        self.quantity = int.from_bytes(data[2:4], byteorder='big')

    def __str__(self):
        return f"WriteRegistersWithFunctionCode03Response(address={self.address}, quantity={self.quantity})"
# Register the custom response with the client decoder
ClientDecoder.register(WriteRegistersWithFunctionCode03Response.function_code, WriteRegistersWithFunctionCode03Response)

client = ModbusSerialClient(
    method='rtu',
    port='/dev/ttyUSB0',
    baudrate=19200,
    parity='N',
    stopbits=1,
    bytesize=8,
    timeout=5,
    framer=ModbusRtuFramer
)

if not client.connect():
    print("Failed to connect to Modbus server")
    exit(1)

try:
    # Define the starting address and values to write
    start_address = 522  # Replace with your starting register address
    values_to_write = 0x02  # List of values to write

    # Create the custom request
    request = WriteRegistersWithFunctionCode03Request(
        address=start_address,
        values=values_to_write,
        unit=1  # Replace with your device's unit ID
    )

    # Execute the request
    response = client.execute(request)

    # Process the response
    if isinstance(response, WriteRegistersWithFunctionCode03Response):
        print(f"Custom write response received: {response}")
        print(f"Written {response.quantity} registers starting at address {response.address}")
    elif response.isError():
        print(f"Error response received: {response}")
    else:
        print(f"Unexpected response: {response}")

except ModbusException as e:
    print(f"Modbus exception occurred: {e}")
except Exception as e:
    print(f"General exception occurred: {e}")
finally:
    client.close()