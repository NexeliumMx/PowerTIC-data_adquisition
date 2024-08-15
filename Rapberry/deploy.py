from Coms import reading_meter
file = open("sn.txt", "r")
sn= file.read()
print(sn)
print("start")
reading_meter('powertic.modbusqueries',sn)
print("lei")


