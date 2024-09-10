import csv
import ast

with open(r'Rapberry/CSV_tests/measurement_address.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    address = []
    for row in reader:
        # Intenta convertir la cadena de texto a una lista de enteros o un entero
        try:
            modbus_addresses = ast.literal_eval(row['modbus_address_DEC'])
        except (ValueError, SyntaxError):
            modbus_addresses = int(row['modbus_address_DEC'])

        # Verifica si es una lista o un entero
        if isinstance(modbus_addresses, list):
            # Itera sobre cada dirección en la lista
            for modbus_address in modbus_addresses:
                address.append(modbus_address)
                print(modbus_address, row['parameter_description'])
            # Imprime la cantidad de elementos en la lista
            print(f"Número de elementos en la lista: {len(modbus_addresses)}")
        else:
            # Si es un entero, agrégalo directamente
            address.append(modbus_addresses)
            print(modbus_addresses, row['parameter_description'])
        
    # Imprime la lista completa de direcciones
    print(address)
