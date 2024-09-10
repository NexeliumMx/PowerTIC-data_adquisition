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

connection = client.connect()
if connection:
    print("Connection Succesful")

response = client.write_register(4211,0,1)
if response.isError():
    print(f"Vlaió madre: {response}")
else:
    print("Te la rifaste fernando")
client.close()