import serial
from chatread import modbus_read
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
# Modbus RTU frame components for Function Code 0x10 (Read) with possible adjustments
slave_address = 0x01             # Slave address
function_code = 0x10             # Function code for Read in your device
starting_address = 0x0209        # Starting register address
quantity_of_registers = 0x3   # Number of registers to read
byte_count = 0x6
payload1 = 0x7F
payload2 = 0x0002
payload3 = 0x0000

def write_modbus(slave_address, function_code, starting_address, quantity_of_registers, byte_count, payload1, payload2, payload3):
    def compute_crc(data):
        crc = 0xFFFF
        for pos in data:
            crc ^= pos
            for _ in range(8):
                if crc & 0x0001:
                    crc >>= 1
                    crc ^= 0xA001
                else:
                    crc >>= 1
        return crc




    # Build the message (adjusted if necessary)
    #format: Addr|Fun|Data start reg hi|Data start reg lo|Data # of regs hi|Data # of regs lo|Byte Count|Value Hi|Value Lo|CRC16 Hi|CRC16 Lo
    message = bytearray()
    message.append(slave_address)
    message.append(function_code)
    message.append((starting_address >> 8) & 0xFF)  # Starting address high byte
    message.append(starting_address & 0xFF)          # Starting address low byte
    message.append((quantity_of_registers >> 8) & 0xFF)  # Quantity high byte
    message.append(quantity_of_registers & 0xFF)         # Quantity low byte
    message.append(byte_count)                           # Byte Count parameter
    message.append((payload1 >> 8) & 0xFF)                # Payload 1  high
    message.append(payload1 & 0xFF)
    message.append((payload2 >> 8) & 0xFF)                # Payload 2 high
    message.append(payload2 & 0xFF)
    message.append((payload3 >> 8) & 0xFF)                # Payload 2 high
    message.append(payload3 & 0xFF)
    # If your device requires additional fields, include them here
    # For example, if a Byte Count is required:
    # message.append(0x00)  # Byte Count (speculative)

    # Compute CRC16 checksum
    crc = compute_crc(message)
    crc_low = crc & 0xFF
    crc_high = (crc >> 8) & 0xFF

    # Append CRC to the message
    message.append(crc_low)
    message.append(crc_high)

    print("Sent: ", message)

    # Send the message over serial port
    ser.write(message)

    # Read the response
    response = ser.read(5 + (quantity_of_registers * 2) + 2)  # Adjust length as needed
    print("Received:", response)

def write_modbus_registers(slave_address, function_code, starting_address, quantity_of_registers, byte_count, payload1):
    def compute_crc(data):
        crc = 0xFFFF
        for pos in data:
            crc ^= pos
            for _ in range(8):
                if crc & 0x0001:
                    crc >>= 1
                    crc ^= 0xA001
                else:
                    crc >>= 1
        return crc




    # Build the message (adjusted if necessary)
    #format: Addr|Fun|Data start reg hi|Data start reg lo|Data # of regs hi|Data # of regs lo|Byte Count|Value Hi|Value Lo|CRC16 Hi|CRC16 Lo
    message = bytearray()
    message.append(slave_address)
    message.append(function_code)
    message.append((starting_address >> 8) & 0xFF)  # Starting address high byte
    message.append(starting_address & 0xFF)          # Starting address low byte
    message.append((quantity_of_registers >> 8) & 0xFF)  # Quantity high byte
    message.append(quantity_of_registers & 0xFF)         # Quantity low byte
    message.append(byte_count)                           # Byte Count parameter
    if byte_count > 1:
        message.append((payload1 >> 8) & 0xFF)                # Payload 1  high
        message.append(payload1 & 0xFF)
    else:
        message.append(payload1)
    # If your device requires additional fields, include them here
    # For example, if a Byte Count is required:
    # message.append(0x00)  # Byte Count (speculative)

    # Compute CRC16 checksum
    crc = compute_crc(message)
    crc_low = crc & 0xFF
    crc_high = (crc >> 8) & 0xFF

    # Append CRC to the message
    message.append(crc_low)
    message.append(crc_high)

    print("Sent: ", message)

    # Send the message over serial port
    ser.write(message)

    # Read the response
    response = ser.read(5 + (quantity_of_registers * 2) + 2)  # Adjust length as needed
    print("Received:", response)

def write_modbus_reset(slave_address, function_code, starting_address, quantity_of_registers, byte_count, payload1, payload2):
    def compute_crc(data):
        crc = 0xFFFF
        for pos in data:
            crc ^= pos
            for _ in range(8):
                if crc & 0x0001:
                    crc >>= 1
                    crc ^= 0xA001
                else:
                    crc >>= 1
        return crc




    # Build the message (adjusted if necessary)
    #format: Addr|Fun|Data start reg hi|Data start reg lo|Data # of regs hi|Data # of regs lo|Byte Count|Value Hi|Value Lo|CRC16 Hi|CRC16 Lo
    message = bytearray()
    message.append(slave_address)
    message.append(function_code)
    message.append((starting_address >> 8) & 0xFF)  # Starting address high byte
    message.append(starting_address & 0xFF)          # Starting address low byte
    message.append((quantity_of_registers >> 8) & 0xFF)  # Quantity high byte
    message.append(quantity_of_registers & 0xFF)         # Quantity low byte
    message.append(byte_count)                           # Byte Count parameter

    message.append(payload1)                # Payload 1  high
    message.append(payload2)
  
    # If your device requires additional fields, include them here
    # For example, if a Byte Count is required:
    # message.append(0x00)  # Byte Count (speculative)

    # Compute CRC16 checksum
    crc = compute_crc(message)
    crc_low = crc & 0xFF
    crc_high = (crc >> 8) & 0xFF

    # Append CRC to the message
    message.append(crc_low)
    message.append(crc_high)

    print("Sent: ", message)

    # Send the message over serial port
    ser.write(message)

    # Read the response
    response = ser.read(5 + (quantity_of_registers * 2) + 2)  # Adjust length as needed
    print("Received:", response)
print("Check Seal status")
modbus_read(slave_address=0x01,function_code=0x03,starting_address=0x101,quantity_of_registers=0x01)
print("Modify Seal status, Communication revise authority, password")
write_modbus(slave_address=slave_address,function_code=function_code,starting_address=starting_address, quantity_of_registers=quantity_of_registers,byte_count=byte_count,payload1=payload1,payload2=payload2,payload3=payload3)
print("read Seal status, Communication revise authority, password status")
modbus_read(slave_address=slave_address,function_code=0x03,starting_address=starting_address,quantity_of_registers=quantity_of_registers)
#time.sleep(5)
print("reset meter registers")
write_modbus_reset(slave_address=0x1,function_code=0x10,starting_address=0x020D,quantity_of_registers=0x0001,byte_count=0x0002,payload1=0x00,payload2=0x00)
#write_modbus(slave_address=0x1,function_code=0x10,starting_address=0x1073,quantity_of_registers=0x0002,byte_count=0x04,payload1=0x0000,payload2=0x0000)
#write_modbus(slave_address=0x01,function_code=function_code,starting_address=0x020A,quantity_of_registers=0x01,byte_count=0x0002,payload=0x04)
# Close the serial port



ser.close()