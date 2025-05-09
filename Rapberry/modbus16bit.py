import serial
from decode_modbus import decode_modbus_response, modbus_commands
import subprocess


ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=19200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    #timeout=0.070
    timeout=1
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
    if not ser.is_open:
        ser.open()
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

    max_retries = 5
    for attempt in range(max_retries):
        # Send the message over serial port
        ser.write(message)

        # validate response
        
        response = ser.read(5 + (quantity_of_registers * 2) + 2)  # Adjust length as needed
        if response:
            print("Received:", response)
            decoded_response = decode_modbus_response(
                response=response,
                slave_address=slave_address,
                datatype='uint16',  # Keep as uint16 for reset validation
                parameter="reset_validation"  # Changed from "serial_number"
            )
            ser.close()
            return decoded_response 
        else:
            kill_processes()
            print(f"Error reading, retrying ({attempt+1}/{max_retries})")
    else: 
        print("Wirte process failed")
        ser.close()  
        return None 
    

def write_modbus_multiple(slave_address:int, function_code:int, starting_address:int, quantity_of_registers:int, byte_count:int, payload:list):
    # Build the message (adjusted if necessary)
    #format: Addr|Fun|Data start reg hi|Data start reg lo|Data # of regs hi|Data # of regs lo|Byte Count|Value Hi|Value Lo|CRC16 Hi|CRC16 Lo
    if not ser.is_open:
        ser.open()
    message = bytearray()
    message.append(slave_address)
    message.append(function_code)
    message.append((starting_address >> 8) & 0xFF)  # Starting address high byte
    message.append(starting_address & 0xFF)          # Starting address low byte
    message.append((quantity_of_registers >> 8) & 0xFF)  # Quantity high byte
    message.append(quantity_of_registers & 0xFF)         # Quantity low byte
    message.append(byte_count)  
    for i in payload:# Byte Count parameter
        message.append((i >> 8) & 0xFF)                # Payload 1  high
        message.append(i & 0xFF)
    
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

    max_retries = 5
    for attempt in range(max_retries):
        # Send the message over serial port
        ser.write(message)

        # validate response
        
        response = ser.read(5 + (quantity_of_registers * 2) + 2)  # Adjust length as needed
        if response:
            print("Received:", response)
            ser.close()
            return response 
        else:
            kill_processes()
            print(f"Error wirting, retrying ({attempt+1}/{max_retries})")
    else: 
        print("Wirte process failed")
        ser.close()  
        return None 

def write_single_modbus(slave_address:int, function_code:int, starting_address:int, quantity_of_registers:int, payload:int):
    # Build the message (adjusted if necessary)
    #format: Addr|Fun|Data start reg hi|Data start reg lo|Data # of regs hi|Data # of regs lo|Byte Count|Value Hi|Value Lo|CRC16 Hi|CRC16 Lo
    if not ser.is_open:
        ser.open()
    message = bytearray()
    message.append(slave_address)
    message.append(function_code)
    message.append((starting_address >> 8) & 0xFF)  # Starting address high byte
    message.append(starting_address & 0xFF)          # Starting address low byte
    #message.append((quantity_of_registers >> 8) & 0xFF)  # Quantity high byte
    #message.append(quantity_of_registers & 0xFF)         # Quantity low byte
    message.append((payload>> 8) & 0xFF)                # Payload 1  high
    message.append(payload& 0xFF)

    # Compute CRC16 checksum
    crc = compute_crc(message)
    crc_low = crc & 0xFF
    crc_high = (crc >> 8) & 0xFF

    # Append CRC to the message
    message.append(crc_low)
    message.append(crc_high)

    print("Sent: ", message)

    max_retries = 5
    for attempt in range(max_retries):
        # Send the message over serial port
        ser.write(message)

        # validate response
        
        response = ser.read(5 + (quantity_of_registers * 2) + 2)  # Adjust length as needed
        if response:
            print("Received:", response)
            ser.close()
            return response 
        else:
            kill_processes()
            print(f"Error writing, retrying ({attempt+1}/{max_retries})")
    else: 
        print("Wirte process failed")
        ser.close()  
        return None 
        


def reset_instruction(slave_address:int,model:str):
    if not ser.is_open:
        ser.open()
    commands, reset = modbus_commands(model)
    print("reset command: ", reset, type(reset))

    address = int(reset.get("modbus_address"))
    print("Reset address: ", address, type(reset))

    register_length = int(reset.get("register_length"))
    print("Register Length: ", register_length, type(register_length))
    
    write_function = int(reset.get("write_command"))
    print("write command: ", write_function, type(write_function))
    
    read_function = int(reset.get("read_command"))
    print("read command: ", read_function, type(read_function))
    
    payload = int(reset.get("value_weight"))
    print("Reset payload: ", payload, type(payload))
    rsp = write_single_modbus(slave_address=slave_address,function_code=write_function,starting_address=address,quantity_of_registers=register_length,payload=payload)
    if not rsp:
        print("Error during reset process. No response from slave device")
        return False
    elif rsp:
        validation = modbus_read(slave_address=slave_address,
                               function_code=read_function,
                               starting_address=address,
                               quantity_of_registers=register_length)
        print("Validation response:", validation)
        
        # Fix: Compare actual value, not hex string
        if validation is None:
            print("Reset validation failed - no response")
            return False
        elif validation == 0:  # Changed from 0x0000
            print("Device reset process successful")
            return True
        else:
            print(f"Reset process failed. Got value: {validation}")
            return False

def kill_processes():
    serial_port = ser.port
    #print(serial_port)
    try:
        bash_rsp = subprocess.run(
            ['./kill_process.sh', serial_port],
            text=True,
            capture_output=True,
            check=True
        )
        #print("Bash response: ",bash_rsp.stdout)
        return bash_rsp.stdout
    except subprocess.CalledProcessError as e:
        print("Error: ", e.stderr)
        return None

#Reset meter attempt
#kill_processes()
#write_single_modbus(slave_address=0x03,function_code=0x06,starting_address=0x1002,quantity_of_registers=0x0001,payload=0x0002)

#current transform set
#read


#write_modbus(slave_address=0x03,function_code=0x10,starting_address=0x1003,quantity_of_registers=0x0001,byte_count=0x0002,payload=[0x00C8])
#write_single_modbus(slave_address=0x03,function_code=0x06,starting_address=0x4000,quantity_of_registers=0x0001,payload=0x0001)

#modbus_read(slave_address=0x02,function_code=0x03,starting_address=0x5000,quantity_of_registers=0x0007)
#reset_instruction(0x02,'EM330DINAV53HS1X')
# Close the serial port

ser.close()