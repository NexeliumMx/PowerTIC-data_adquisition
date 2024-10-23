import serial
from Rapberry.modbus16bit import modbus_read,write_modbus
import time
# Serial port configuration (as before)
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=19200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=5
)
slave_address = 0x01             # Slave address
function_code = 0x10             # Function code for Read in your device
starting_address = 0x0209        # Starting register address
quantity_of_registers = 0x3   # Number of registers to read
byte_count = 0x6
payload1 = 0x7F
payload2 = 0x0002
payload3 = 0x0000
print("Check Seal status")
modbus_read(slave_address=0x01,function_code=0x03,starting_address=0x101,quantity_of_registers=0x01)
print("Modify Seal status, Communication revise authority, password")
write_modbus(slave_address=slave_address,function_code=function_code,starting_address=starting_address, quantity_of_registers=quantity_of_registers,byte_count=byte_count,payload=[payload1,payload2,payload3])
print("read Seal status, Communication revise authority, password status")
modbus_read(slave_address=slave_address,function_code=0x03,starting_address=starting_address,quantity_of_registers=quantity_of_registers)

