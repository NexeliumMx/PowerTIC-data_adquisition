import serial
import struct
import time
import csv
import logging
import numpy as np

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def modbus_commands():
    with open('modbusqueries.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = []
        for row in reader:
            # Normalize key names
            row = {key.strip().lower(): value.strip() for key, value in row.items()}
            # Parse modbus_address if in brackets
            if "modbus_address" in row and row["modbus_address"].startswith("[") and row["modbus_address"].endswith("]"):
                row["modbus_address"] = row["modbus_address"][1:-1]  # Remove brackets
            rows.append(row)
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

    # Debugging: Show raw data bytes
    logger.debug(f"Data type: {datatype}")
    logger.debug(f"Raw data bytes: {data_bytes}")

    # Decode data based on datatype
    try:
        if datatype.lower() == 'float':
            if len(data_bytes) < 4:
                logger.error("Invalid data length for float")
                return
            data_value = struct.unpack('>f', bytes(data_bytes[:4]))[0]
        elif datatype.lower() == 'word':
            if len(data_bytes) < 2:
                logger.error("Invalid data length for word")
                return
            data_value = struct.unpack('>H', bytes(data_bytes[:2]))[0]
        elif datatype.lower() == 'int':
            if len(data_bytes) < 4:
                logger.error("Invalid data length for int")
                return
            data_value = struct.unpack('>i', bytes(data_bytes[:4]))[0]
        elif datatype.lower() == 'uint':
            if len(data_bytes) < 4:
                logger.error("Invalid data length for uint")
                return
            data_value = struct.unpack('>I', bytes(data_bytes[:4]))[0]
        elif datatype.lower() == 'string':
            data_value = ''.join(chr(b) for b in data_bytes if b != 0)
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
    
    function_code = 0x03
    with serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=19200,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=0.1
    ) as ser:
        for address in commands:
            logger.debug(f"Processing address: {address}")
            try:
                datatype = address["data_type"]
                quantity_of_registers = int(address["register_number"], 0)
                modbus_address = eval(address["modbus_address"])
                if not isinstance(modbus_address, list):
                    starting_address = modbus_address
                elif isinstance(modbus_address, list):
                    starting_address = modbus_address[0]
            except KeyError as e:
                logger.error(f"Missing key in address: {e}")
                continue
            except ValueError as e:
                logger.error(f"Invalid value in address: {e}")
                continue
            
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