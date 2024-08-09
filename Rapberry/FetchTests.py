import re

# Cargar el contenido del archivo SQL
file_path = '/home/luis08islas/VScode/PowerTIC/Rapberry/measurement_address.sql'

with open(file_path, 'r') as file:
    sql_content = file.read()

# Extraer los datos de las sentencias INSERT INTO
insert_statements = re.findall(
    r"INSERT INTO measurements_address \((.*?)\) VALUES \((.*?)\);",
    sql_content,
    re.DOTALL
)

# Extraer los nombres de las columnas
columns = [col.strip() for col in insert_statements[0][0].split(',')]

# Extraer las filas de datos
data = []
for statement in insert_statements:
    values = re.findall(r"'(?:[^'\\]|\\.)*'|[^,]+", statement[1])
    values = [val.strip().strip("'") for val in values]
    if len(values) == len(columns):
        data.append(values)
    else:
        print(f"Skipping a row due to mismatched column count: {values}")

# Convertir los datos a una lista de diccionarios
data_dicts = [dict(zip(columns, row)) for row in data]

# Crear un diccionario que mapea cada parameter_description a su correspondiente modbus_address_hex
parameter_to_address = {row['parameter_description']: row['modbus_address_dec'] for row in data_dicts}

# Imprimir el diccionario resultante
for parameter, address in parameter_to_address.items():
    print(f"{parameter}: {address}")
    print(parameter)
    print(address)
