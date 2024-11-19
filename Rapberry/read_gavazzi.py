from pymodbus.client import ModbusSerialClient

#Conexión con el medidor mediante modbus
client = ModbusSerialClient(
    port='/dev/ttyUSB1',
    baudrate=19200,
    parity='N',
    stopbits=1,
    bytesize=8,
    timeout=5
)


result = client.read_holding_registers(0x0002,1,3)
if not result.isError():
    value = result.registers[0]
    print("value: ", value)
else: 
    print("Communication error", result)
