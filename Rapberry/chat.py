import serial
import struct

def crc16(data: bytes) -> int:
    """Compute the Modbus RTU CRC16 checksum."""
    crc = 0xFFFF
    for pos in data:
        crc ^= pos
        for _ in range(8):
            lsb = crc & 0x0001
            crc >>= 1
            if lsb:
                crc ^= 0xA001
    return crc

def main():
    # Serial port configuration
    port = '/dev/ttyUSB0'  # Replace with your serial port
    baudrate = 19200        # Replace with your baud rate

    # Modbus message components
    slave_address = 0x01   # Replace with your slave address
    function_code = 0x03   # Function code 0x03
    data = bytes([0x02])   # Data to send (value 0x02)

    # Construct the Modbus RTU frame
    message = struct.pack('B', slave_address) + struct.pack('B', function_code) + data

    # Calculate CRC16 checksum
    crc = crc16(message)
    crc_bytes = struct.pack('<H', crc)

    # Complete message with CRC
    full_message = message + crc_bytes

    # Open the serial port
    with serial.Serial(port, baudrate, timeout=1) as ser:
        # Send the message
        ser.write(full_message)
        print(f"Sent: {full_message.hex()}")

        # Read the response (optional)
        response = ser.read(256)
        if response:
            print(f"Received: {response.hex()}")
        else:
            print("No response received.")

if __name__ == '__main__':
    main()