from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusException, ModbusIOException
from pymodbus.pdu import ExceptionResponse
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder

import struct

# Initialization of Modbus
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

try:
    # Define the register address and the value to write
    register_address = 0x20B  # Adjust for 0-based if necessary
    value_to_write = 0b0000000000000000

    response = client.write_registers(register_address, value_to_write, 1)

    # Check if the write was successful
    if isinstance(response, ExceptionResponse):
        exception_code = response.exception_code
        print(f"Failed to write to register {register_address}: Exception code {exception_code}")
    elif response.isError():
        print(f"Failed to write to register {register_address}: {response}")
    else:
        print(f"Successfully wrote {value_to_write} to register {register_address}")

    # Write to register 0x20A
    register_address = 0x20A
    value_to_write = 2
    response = client.write_registers(register_address, value_to_write, 1)

    if isinstance(response, ExceptionResponse):
        exception_code = response.exception_code
        print(f"Failed to write to register {register_address}: Exception code {exception_code}")
    elif response.isError():
        print(f"Failed to write to register {register_address}: {response}")
    else:
        print(f"Successfully wrote {value_to_write} to register {register_address}")

    # Write to register 0x20B again
    register_address = 0x20B
    value_to_write = 0b0000000000000000
    response = client.write_registers(register_address, value_to_write, 1)

    if isinstance(response, ExceptionResponse):
        exception_code = response.exception_code
        print(f"Failed to write to register {register_address}: Exception code {exception_code}")
    elif response.isError():
        print(f"Failed to write to register {register_address}: {response}")
    else:
        print(f"Successfully wrote {value_to_write} to register {register_address}")

    # Write to register 0x20D
    register_address = 0x20D
    value_to_write = 0b1100110000000000
    response = client.write_registers(register_address, value_to_write, 1)

    if isinstance(response, ExceptionResponse):
        exception_code = response.exception_code
        print(f"Failed to write to register {register_address}: Exception code {exception_code}")
    elif response.isError():
        print(f"Failed to write to register {register_address}: {response}")
    else:
        print(f"Successfully wrote {value_to_write} to register {register_address}")

except ModbusIOException as e:
    print(f"Modbus IO Exception caught: {e}")
except ModbusException as e:
    print(f"Modbus Exception caught: {e}")
except Exception as e:
    print(f"General Exception caught: {e}")
finally:
    # Close the Modbus connection
    client.close()