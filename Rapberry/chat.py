import serial

def compute_crc(data):
    crc = 0xFFFF
    for pos in data:
        crc ^= pos
        for _ in range(8):
            if (crc & 0x0001):
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return crc

# Serial port configuration
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=19200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=5
)

# Modbus RTU frame components for Function Code 0x10
slave_address = 0x01             # Slave address
function_code = 0x10             # Function code for Write Multiple Registers
starting_address = 0x020A        # Starting register address (e.g., 42)
quantity_of_registers = 0x0001   # Number of registers to write
data_value = 0x0002              # The value to write to the register

# Build the message without CRC
message = bytearray()
message.append(slave_address)
message.append(function_code)
message.append((starting_address >> 8) & 0xFF)  # Starting address high byte
message.append(starting_address & 0xFF)          # Starting address low byte
message.append((quantity_of_registers >> 8) & 0xFF)  # Quantity high byte
message.append(quantity_of_registers & 0xFF)          # Quantity low byte
message.append(quantity_of_registers * 2)             # Byte count
message.append((data_value >> 8) & 0xFF)          # Data high byte
message.append(data_value & 0xFF)                 # Data low byte

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

# Read the response (expected to be 8 bytes for function code 0x10)
response = ser.read(8)
print("Received:", response)

# Close the serial port
ser.close()