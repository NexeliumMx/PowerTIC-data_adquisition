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
#register_address = 0x1073  # The first register address (adjust for 0-based if necessary)
value_to_write = 0x0002
register_address = 0x020A

"""for register_address in range(0x106B,0x107A):
    value_high = (value_to_write >> 8) & 0xFF
    value_low = (value_to_write & 0xFF) 
    response = client.write_registers(register_address, [value_high,value_low], 1)

    # Check if the write was successful
    if response.isError():
        print(f"Failed to write to register {register_address}: {response}")
    else:
        print(f"Successfully wrote {value_to_write} to registers {register_address} and {register_address+1}")"""
    # Close the Modbus connection


value_high = (value_to_write >> 8) & 0xFF
value_low = (value_to_write & 0xFF) 
response = client.write_registers(register_address, [0x0004,0x0000], 1)

# Check if the write was successful
if response.isError():
    print(f"Failed to write to register {register_address}: {response}")
else:
    print(f"Successfully wrote {value_to_write} to registers {register_address} and {register_address+1}")
# Close the Modbus connection

meas = client.read_holding_registers(register_address,1,1)
value_read = meas.registers[0]
# Check if the read was successful
if meas.isError():
    print(f"Failed to write to register {register_address}: {meas}")
else:
    print(f"Meas:  {value_read} ")
# Close the Modbus connection
client.close()
