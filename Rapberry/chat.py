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

# Modbus RTU frame components for Function Code 0x10
slave_address = 0x01             # Slave address
function_code = 0x10             # Function code for Write Multiple Registers
starting_address = 0x02A        # Starting register address (e.g., 0x02AC)
quantity_of_registers = 0x0001   # Number of registers to write
data_value = 0x0002              # The value to write to the register

# Break down data_value into high and low bytes
data_high = (data_value >> 8) & 0xFF
data_low = data_value & 0xFF

# Build the message without CRC
message = [
    slave_address,
    function_code,
    (starting_address >> 8) & 0xFF,
    starting_address & 0xFF,
    (quantity_of_registers >> 8) & 0xFF,
    quantity_of_registers & 0xFF,
    quantity_of_registers * 2,  # Byte count: number of registers * 2
    data_high,
    data_low
]

message_bytes = bytes(message)

# Compute CRC16 checksum
crc = compute_crc(message_bytes)
crc_low = crc & 0xFF
crc_high = (crc >> 8) & 0xFF

# Append CRC to the message
full_message = message_bytes + bytes([crc_low, crc_high])

print("Sent: ", full_message)

# Send the message over serial port
ser.write(full_message)

# Read the response (expected to be 8 bytes for function code 0x10)
response = ser.read(8)
print("Received:", response)

# Close the serial port
ser.close()