from Coms import meter_param
print("start")
SN=meter_param('powertic.modbusqueries')
f=open("sn.txt","x")
f.write(SN)