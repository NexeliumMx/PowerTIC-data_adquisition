import asyncio
import struct

from pymodbus import FramerType
from pymodbus.client import ModbusSerialClient
from pymodbus.pdu import ModbusExceptions, ModbusRequest, ModbusResponse
from pymodbus.pdu.bit_read_message import ReadCoilsRequest

class CustomModbusResponse(ModbusResponse):
    """Custom modbus response."""

    function_code = 3
    _rtu_byte_count_pos = 2

    def __init__(self, values=None, slave=1, transaction=0, skip_encode=False):
        """Initialize."""
        ModbusResponse.__init__(self, slave, transaction, skip_encode)
        self.values = values or []

    def encode(self):
        """Encode response pdu.

        :returns: The encoded packet message
        """
        res = struct.pack(">B", len(self.values) * 2)
        for register in self.values:
            res += struct.pack(">H", register)
        return res

    def decode(self, data):
        """Decode response pdu.

        :param data: The packet data to decode
        """
        byte_count = int(data[0])
        self.values = []
        for i in range(1, byte_count + 1, 2):
            self.values.append(struct.unpack(">H", data[i : i + 2])[0])

class CustomModbusRequest(ModbusRequest):
    """Custom modbus request."""

    function_code = 3
    _rtu_frame_size = 8

    def __init__(self, address=None, slave=1, transaction=0, skip_encode=False):
        """Initialize."""
        ModbusRequest.__init__(self, slave, transaction, skip_encode)
        self.address = address
        self.count = 16

    def encode(self):
        """Encode."""
        return struct.pack(">HH", self.address, self.count)

    def decode(self, data):
        """Decode."""
        self.address, self.count = struct.unpack(">HH", data)

    def execute(self, context):
        """Execute."""
        if not 1 <= self.count <= 0x7D0:
            return self.doException(ModbusExceptions.IllegalValue)
        if not context.validate(self.function_code, self.address, self.count):
            return self.doException(ModbusExceptions.IllegalAddress)
        values = context.getValues(self.function_code, self.address, self.count)
        return CustomModbusResponse(values)

client = ModbusSerialClient(
    port='/dev/ttyUSB0',
    baudrate=19200,
    parity='N',
    stopbits=1,
    bytesize=8,
    timeout=5
)

client.connect()


CustomModbusResponse()

# new modbus function code.
client.register(CustomModbusResponse)
slave=1
request = CustomModbusRequest(523, slave=slave)
result = client.execute(request)
print(result)