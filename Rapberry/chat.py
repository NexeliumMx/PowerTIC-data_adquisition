import serial

def compute_crc(data):
    """
    Compute the Modbus RTU CRC16 checksum for the given data.
    """
    crc = 0xFFFF
    for pos in data:
        crc ^= pos
        for _ in range(8):
            lsb = crc & 0x0001
            crc >>= 1
            if lsb:
                crc ^= 0xA001
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

# Modbus RTU frame components
slave_address = 0x01        # Change this to your slave address if different
function_code = 0x10        # Function code 03H
data = [0x02]               # Data to send (0x02)

# Build the message without CRC
message = bytes([slave_address, function_code] + data)

# Compute CRC16 checksum
crc = compute_crc(message)
crc_low = crc & 0xFF
crc_high = (crc >> 8) & 0xFF

# Append CRC to the message
full_message = message + bytes([crc_low, crc_high])

# Send the message over serial port
ser.write(full_message)
print("Sent: ", full_message)
# Optionally, read response from the slave device
response = ser.read(100)  # Adjust the number of bytes to read as needed
print("Received:", response)

# Close the serial port
ser.close()