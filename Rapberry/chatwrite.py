import serial
from chatread import modbus_read
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
function_code = 0x03             # Function code for Read in your device
starting_address = 0x020B        # Starting register address
quantity_of_registers = 0x1   # Number of registers to read
byte_count = 0x2
payload = 0x0000

def write_modbus(slave_address, function_code, starting_address, quantity_of_registers, byte_count, payload):
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
    message.append((payload >> 8) & 0xFF)                # Payload high
    message.append(payload & 0xFF)
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

write_modbus(slave_address=slave_address,function_code=function_code,starting_address=starting_address, quantity_of_registers=quantity_of_registers,byte_count=byte_count,payload=payload)

write_modbus(slave_address=0x01,function_code=0x10,starting_address=0x020A,quantity_of_registers=0x01,byte_count=0x0002,payload=0x04)
# Close the serial port
ser.close()

modbus_read(slave_address=0x01,function_code=0x10,starting_address=0x020A,quantity_of_registers=0x1)