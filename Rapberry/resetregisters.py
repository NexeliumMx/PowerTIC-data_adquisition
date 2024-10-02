from pymodbus.client import ModbusSerialClient
import pymodbus.client
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder

import struct
# Inicialización de Modbus
client = ModbusSerialClient(
    port='/dev/ttyUSB0',
    baudrate=19200,
    parity='N',
    stopbits=1,
    bytesize=8,
    timeout=5
)
# Connect to the client
connection = client.connect()

if connection:
    print("Modbus client connected successfully")
else:
    print("Failed to connect to Modbus client")

# Define the register address and the value to write
register_address = 0x20B  # The first register address (adjust for 0-based if necessary)
value_to_write = 0b0000000000000000  
response = client.write_registers(register_address, value_to_write, 1)

# Check if the write was successful
if response.isError():
    print(f"Failed to write to register {register_address}: {response}")
else:
    print(f"Successfully wrote {value_to_write} to registers {register_address} and {register_address+1}")
# Close the Modbus connection
register_address = 0x20A  # The first register address (adjust for 0-based if necessary)
value_to_write =2
response = client.write_registers(register_address, value_to_write, 1)
if response.isError():
    print(f"Failed to write to register {register_address}: {response}")
else:
    print(f"Successfully wrote {value_to_write} to registers {register_address} and {register_address+1}")
register_address = 0x20B  # The first register address (adjust for 0-based if necessary)
value_to_write = 0b0000000000000000  
response = client.write_registers(register_address, value_to_write, 1)

# Check if the write was successful
if response.isError():
    print(f"Failed to write to register {register_address}: {response}")
else:
    print(f"Successfully wrote {value_to_write} to registers {register_address} ")
register_address = 0x20D  # The first register address (adjust for 0-based if necessary)
value_to_write = 0b1100110000000000  
response = client.write_registers(register_address, value_to_write, 1)

if response.isError():
    print(f"Failed to write to register {register_address}: {response}")
else:
    print(f"Successfully wrote {value_to_write} to registers {register_address} ")
client.close()
