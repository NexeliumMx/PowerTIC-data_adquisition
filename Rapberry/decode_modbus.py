import serial
import struct
import csv
import logging
import numpy as np

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def modbus_commands(model:str):
    """Read Modbus commands from a CSV file and filter rows by model."""
    try:
        with open('modbusrtu_commands.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = []
            for row in reader:
                # Normalize key names and handle missing keys
                row = {key.strip().lower(): value.strip() for key, value in row.items() if key and value}
                # Parse modbus_address if in brackets
                if "modbus_address" in row and row["modbus_address"].startswith("[") and row["modbus_address"].endswith("]"):
                    row["modbus_address"] = row["modbus_address"][1:-1]  # Remove brackets
                # Filter rows where model is "EM210-72D.MV5.3.X.OS.X"
                if row.get("model") == model:
                    rows.append(row)
            return rows
    except FileNotFoundError as e:
        logger.error(f"CSV file not found: {e}")
        return []
    except Exception as e:
        logger.error(f"Error reading CSV file: {e}")
        return []

def compute_crc(data):
    """Compute CRC-16 for Modbus."""
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
    """Decode a Modbus response based on the specified data type."""
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
                logger.error("Invalid data length for float------------------------------------")
                return
            data_value = struct.unpack('>f', data_bytes[:4])[0]
        elif datatype.lower() == 'word':
            if len(data_bytes) < 2:
                logger.error("Invalid data length for word------------------------------------")
                return
            data_value = struct.unpack('>H', data_bytes[:2])[0]
        elif datatype.lower() in ['uint16', 'Uint16']:
            if len(data_bytes) > 2:
                logger.error(f"Invalid data length for uint16 {len(data_bytes)} ------------------------------------")
                return
            data_value = struct.unpack('>H', data_bytes[:2])[0]
        elif datatype.lower() == 'int':
            if len(data_bytes) < 4:
                logger.error(f"Invalid data length for int {len(data_bytes)} ------------------------------------")
                return
            data_value = struct.unpack('>i', data_bytes[:4])[0]
        elif datatype.lower() == 'int32':
            if len(data_bytes) < 4:
                logger.error(f"Invalid data length for int {len(data_bytes)} ------------------------------------")
                return
            data_value = struct.unpack('<i', data_bytes[:4])[0]
        elif datatype.lower() in ['int16', 'sunssf']:
            if len(data_bytes) != 2:
                raise ValueError("int16 requires exactly 2 bytes of data------------------------------------")
            data_value = struct.unpack('>h', data_bytes[:2])[0]
        elif datatype.lower() == 'uint':
            if len(data_bytes) < 4:
                logger.error("Invalid data length for uint------------------------------------")
                return
            data_value = struct.unpack('>I', data_bytes[:4])[0]
        elif datatype.lower() == 'string':
            data_value = ''.join(chr(b) for b in data_bytes if b != 0)
        elif datatype.lower() == 'acc32':
            if len(data_bytes) > 4:
                raise ValueError("ACC32 data length invalid------------------------------------")
            data_value = struct.unpack('>I', data_bytes[:4])[0]
        elif datatype.lower() in ['dword', 'Dword']:
            if len(data_bytes) == 6:
                logger.debug("Timestamp detected in Dword response------------------------------------")
                data_value = struct.unpack('>I', data_bytes[:4])[0]  # Decode first 4 bytes
                timestamp = struct.unpack('>H', data_bytes[4:6])[0]  # Remaining 2 bytes as timestamp
                logger.info(f"Timestamp: {timestamp}")
            elif len(data_bytes) == 4:
                data_value = struct.unpack('>I', data_bytes[:4])[0]
            else:
                logger.error("Invalid data length for Dword------------------------------------")
                return
        else:
            data_value = data_bytes  # Raw bytes
            logger.debug("Unprocessed data type------------------------------------------------------------------------")

    except struct.error as e:
        logger.error(f"Error decoding data: {e}")
        return

    # Display the results
    logger.info(f"Byte Count: {byte_count}")
    logger.info(f"Data Value: {data_value}")

def modbus_multiple_read(slave_address: int):
    """Perform multiple Modbus reads based on commands from the CSV file."""
    commands = modbus_commands("acurev-1313-5a-x0") #EM210-72D.MV5.3.X.OS.X
    #print("Modbus Command: ", commands)
    function_code = 0x03  # Read holding registers

    with serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=19200,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=0.05
    ) as ser:
        for address in commands:
            try:
                parameter = address.get('parameter', 'Unknown')
                logger.info(f"Parameter: {parameter}")
                datatype = address.get("data_type", "raw")
                quantity_of_registers = int(address.get("register_length", "0"), 0)
                modbus_address = eval(address["modbus_address"])
                starting_address = modbus_address[0] if isinstance(modbus_address, list) else modbus_address
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
    try:
        slave_address = 0x03
        modbus_multiple_read(slave_address=slave_address)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")