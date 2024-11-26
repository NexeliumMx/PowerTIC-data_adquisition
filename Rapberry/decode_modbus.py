import serial
import struct
import time
import csv
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def modbus_commands():
    with open('modbusqueries.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
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

def decode_modbus_response(response, slave_address: int, datatype: str):
    if not response:
        logger.error("No response received")
        return
    if len(response) < 5:
        logger.error("Incomplete response received")
        return

    # Validate CRC
    received_crc = response[-2:]
    response_data = response[:-2]
    calculated_crc = compute_crc(response_data)
    calculated_crc_bytes = calculated_crc.to_bytes(2, byteorder='little')
    if received_crc != calculated_crc_bytes:
        logger.error("CRC mismatch in response")
        return

    # Extract header information
    device_address = response[0]
    function_code = response[1]

    if device_address != slave_address:
        logger.error(f"Unexpected device address: {device_address}")
        return

    if function_code & 0x80:
        exception_code = response[2]
        logger.error(f"Modbus exception code: {exception_code}")
        return

    byte_count = response[2]
    data_bytes = response[3:-2]

    # Decode data based on datatype
    try:
        if datatype == 'float':
            data_value = struct.unpack('>f', data_bytes)[0]
        elif datatype == 'int':
            data_value = struct.unpack('>i', data_bytes)[0]
        elif datatype == 'uint':
            data_value = struct.unpack('>I', data_bytes)[0]
        else:
            data_value = data_bytes  # Raw bytes
    except struct.error as e:
        logger.error(f"Error decoding data: {e}")
        return

    # Display the results
    logger.info(f"Device Address: {device_address}")
    logger.info(f"Function Code: {function_code}")
    logger.info(f"Byte Count: {byte_count}")
    logger.info(f"Data Value: {data_value}")

def modbus_multiple_read(slave_address: int):
    commands = modbus_commands()
    #print("Commands: ", commands)
    
    function_code = 0x03
    with serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=19200,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=5
    ) as ser:
        for address in commands:
            print("Processing address: ", address)
            datatype = address["datatype"]
            quantity_of_registers = int(address["register_length"], 0)
            starting_address = int(address["modbus_address"], 0)
            logger.debug(f"Processing {address}")

            # Build the message
            message = bytearray()
            message.append(slave_address)
            message.append(function_code)
            message.append((starting_address >> 8) & 0xFF)
            message.append(starting_address & 0xFF)
            message.append((quantity_of_registers >> 8) & 0xFF)
            message.append(quantity_of_registers & 0xFF)

            # Compute CRC16 checksum
            crc = compute_crc(message)
            crc_low = crc & 0xFF
            crc_high = (crc >> 8) & 0xFF

            # Append CRC to the message
            message.append(crc_low)
            message.append(crc_high)

            logger.debug(f"Sent: {message.hex()}")

            # Send the message over serial port
            max_retries = 3
            for attempt in range(max_retries):
                ser.write(message)
                time.sleep(1)
                response_length = 5 + (quantity_of_registers * 2) + 2
                response = ser.read(response_length)
                if response:
                    logger.debug(f"Received: {response.hex()}")
                    break
                else:
                    logger.warning(f"No response, retrying ({attempt+1}/{max_retries})")
            else:
                logger.error("Failed to get response after retries")
                continue

            decode_modbus_response(response, slave_address, datatype)

if __name__ == "__main__":
    slave_address = 0x05
    modbus_multiple_read(slave_address=slave_address)