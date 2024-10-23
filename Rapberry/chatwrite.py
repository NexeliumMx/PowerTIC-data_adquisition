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

print("Check Seal status")
modbus_read(slave_address=0x01,function_code=0x03,starting_address=0x101,quantity_of_registers=0x01)
print("Modify Seal status, Communication revise authority, password")
write_modbus(slave_address=slave_address,function_code=function_code,starting_address=starting_address, quantity_of_registers=quantity_of_registers,byte_count=byte_count,payload1=payload1,payload2=payload2,payload3=payload3)
print("read Seal status, Communication revise authority, password status")
modbus_read(slave_address=slave_address,function_code=0x03,starting_address=starting_address,quantity_of_registers=quantity_of_registers)

