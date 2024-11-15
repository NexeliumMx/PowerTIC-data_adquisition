import serial 
import struct
import time
import csv
ser = serial.Serial(
    port = '/dev/ttyUSB1',
    baudrate=19200,
    bytesize = serial.EIGHTBITS,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    timeout=5
)
def modbus_commands():
    with open('Modbusqueries.csv', newline='') as csvfile:
        rows = csv.DictReader(csvfile)
    return rows

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

def decode_modbus_response(response, slave_address: int):
    
    if response != None:
        print("Decoding response: ")
        # Extract header information
        device_address = response[0]
        function_code = response[1]
        byte_count = response[2]
        data_bytes = response[3:3 + byte_count]
        crc = response[-2:]
    else:

        print("No response received")
        return
    # Decode data based on byte count
    data_value = None
    try:
        if byte_count == 2:
            data_value = struct.unpack(">H", data_bytes)[0]  # 16-bit integer
        elif byte_count == 4:
            data_value = struct.unpack(">I", data_bytes)[0]  # 32-bit integer
        elif byte_count == 8:
            data_value = struct.unpack(">Q", data_bytes)[0]  # 64-bit integer
        else:
            data_value = data_bytes  # Raw bytes if size does not match standard sizes
    except ValueError:
        print("Error decoding data from meter: ", slave_address)

    # Display the results
    print(f"Device Address: {device_address}")
    print(f"Function Code: {function_code}")
    print(f"Byte Count: {byte_count}")
    print(f"Data Value: {data_value if isinstance(data_value, int) else data_value.hex()}")
    print(f"CRC: {crc.hex()}")

def modbus_multiple_read(slave_address:int):
    commands = modbus_commands()
    function_code = 0x03
    for address in commands:
        datatype = address["datatype"]
        quantity_of_registers = address["register_length"]
        starting_address = address["modbus_address"]
        print(address, datatype, quantity_of_registers)

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

        
        decode_modbus_response(response, slave_address)

    # Close the serial port
    ser.close()

slave_address = 0x05
function_code = 0x03

modbus_read(slave_address=slave_address,function_code=function_code,starting_address=0x1073,quantity_of_registers=2)