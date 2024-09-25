import csv

with open('/Users/luissanchez/MICO/PowerTIC/Rapberry/Modbusqueries.csv', newline='') as csvfile:
    modbus_queries = csv.DictReader(csvfile)
    for row in modbus_queries:
        print(row['parameter_description'], row['modbus_address'])
