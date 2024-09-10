from pymodbus.client import ModbusSerialClient
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
register_address = 0x1073  # The first register address (adjust for 0-based if necessary)
value_to_write = 0  # The 32-bit value you want to write

# Convert the 32-bit value into two 16-bit registers
high_word = (value_to_write >> 16) & 0xFFFF  # High 16 bits
low_word = value_to_write & 0xFFFF           # Low 16 bits

# Write the two registers using function code 16 (0x10)
response = client.write_registers(register_address, [high_word, low_word], 1)

# Check if the write was successful
if response.isError():
    print(f"Failed to write to register {register_address}: {response}")
else:
    print(f"Successfully wrote {value_to_write} to registers {register_address} and {register_address+1}")

# Close the Modbus connection
client.close()