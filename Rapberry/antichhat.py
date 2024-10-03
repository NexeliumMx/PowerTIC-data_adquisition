import tinymodbusrtu as modbus
import serial
serialPort = serial.Serial(
    port='/dev/ttyUSB0', baudrate=19200, bytesize=8, timeout=1, stopbits=serial.STOPBITS_ONE)
a=modbus.TinyModbusClient(serial_connection=serialPort,
                                       crc_enabled=True,
                                       timeout=1.0)
d=b'0x02/0x0B/0x00/0x01/0x01/0x00/0x02'
a.send_custom_message(1,3,d)