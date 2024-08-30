
# Lectura de registros de Power Factor
SN1 = client.read_holding_registers(0x1034, 15, 1)
SN1_Val=""
if not SN1.isError():
    SN1_Val = ""

    for i in SN1.registers:
        SN1_Val += chr((i&0b1111111100000000)>>8)+chr(i&0b0000000011111111)
        # data['PF'] = SN1_Val
    print("SN:", SN1_Val)
else:
    print("Error de lectura (SN):", SN1)
