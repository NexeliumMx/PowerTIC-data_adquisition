from pymodbus.client import ModbusSerialClient
import json
import requests
import datetime
from datetime import timezone
import os
import csv

#Conexión con el medidor mediante modbus
client = ModbusSerialClient(
    port='/dev/ttyUSB0',
    baudrate=19200,
    parity='N',
    stopbits=1,
    bytesize=8,
    timeout=5
)

def timestamp(sn):
    if client.connect():
        meter_time = {}
        with open('Modbusqueries.csv', newline='') as csvfile:
            rows = csv.DictReader(csvfile)

            try:
                for row in rows:
                    if row["timestamp"] == "t":
                        time = True
                    elif row["timestamp"] == "f":
                        time = False

                    if time:
                        parameter_description = row['parameter_description']

                        modbus_address = json.loads(row['modbus_address'])[0]
                        registers = int(row['register_number'])
                        value = ''
                        try:
                            meas = client.read_holding_registers(modbus_address, 1)
                            if not meas.isError():
                                value = meas.registers[0]
                                meter_time[f"{parameter_description}"] = value
                                print(f"{parameter_description}: {value}")
                            else:
                                print(f"Error reading {parameter_description} at {modbus_address}: {meas}")
                        except Exception as e:
                            print(f"Invalid address for { parameter_description}: {modbus_address}")
            except Exception as e:
                print("Exception during data acquisition: ", e)
            finally:
                client.close()
                year = meter_time["clock: year"]
                month = meter_time["clock: month"]
                date = meter_time["clock: date"]
                hour = meter_time["clock: hour"]
                minute = meter_time["clock: minute"]
                second = meter_time["clock: second"]
                print(f"{year}-{month}-{date} {hour}:{minute}:{second}Z")
                timestamp = f"{year}-{month}-{date} {hour}:{minute}:{second}Z"
                print(timestamp)
    return timestamp

timestamp("E3T15060693")