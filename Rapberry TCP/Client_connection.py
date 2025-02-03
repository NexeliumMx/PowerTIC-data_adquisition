import socket

SERVER_IP = "192.168.68.61"

PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((SERVER_IP, PORT))
print(f"Connected to server at {SERVER_IP}: {PORT}")

payload = 0xC8
message = bytearray()
message.append(payload)
client_socket.sendall(message)

data = client_socket.recv(1024)
integer_value = int.from_bytes(data, byteorder='big')

print("Received data from server: ", integer_value)

client_socket.close()