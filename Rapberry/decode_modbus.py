import serial 
import struct
import time
ser = serial.Serial(
    port = '/dev/ttyUSB1',
    baudrate=19200,
    bytesize = serial.EIGHTBITS,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    timeout=5
)

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

def modbus_read(slave_address:int, function_code:int, starting_address:int, quantity_of_registers:int):
    # Build the message (adjusted if necessary)
    #format: Addr|Fun|Data start reg hi|Data start reg lo|Data # of regs hi|Data # of regs lo|CRC16 Hi|CRC16 Lo
    message = bytearray()
    message.append(slave_address)
    message.append(function_code)
    message.append((starting_address >> 8) & 0xFF)  # Starting address high byte
    message.append(starting_address & 0xFF)          # Starting address low byte
    message.append((quantity_of_registers >> 8) & 0xFF)  # Quantity high byte
    message.append(quantity_of_registers & 0xFF)         # Quantity low byte
    # Compute CRC16 checksum
    crc = compute_crc(message)
    crc_low = crc & 0xFF
    crc_high = (crc >> 8) & 0xFF

    # Append CRC to the message
    message.append(crc_low)
    message.append(crc_high)

    print("Sent: ", message)

    # Send the message over serial port
    if not ser.is_open:
        ser.open()
    ser.write(message)

    time.sleep(1)

    # Read the response
    response = ser.read(5 + (quantity_of_registers * 2) + 2)  # Adjust length as needed
    print("Received:", response)

    # Unpack the relevant bytes
    device_address = response[0]
    function_code = response[1]
    byte_count = response[2]
    data_bytes = response[3:3 + byte_count]
    crc = response[-2:]

    # Interpret the data (usually as a single 16-bit integer)
    data_value = struct.unpack(">I", data_bytes)[0]

    # Display the results
    print(f"Device Address: {device_address}")
    print(f"Function Code: {function_code}")
    print(f"Byte Count: {byte_count}")
    print(f"Data Value: {data_value}")
    print(f"CRC: {crc.hex()}")
    # Close the serial port
    ser.close()

slave_address = 0x05
function_code = 0x03

modbus_read(slave_address=slave_address,function_code=function_code,starting_address=0x104C,quantity_of_registers=1)