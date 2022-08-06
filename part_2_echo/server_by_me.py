import socket
server_socket = socket.socket()

server_socket.bind(('0.0.0.0', 8820))
server_socket.listen()
print("server is up and running")
while True:
    (client_socket, client_address) = server_socket.accept()
    print(f"Client connected with ip: {client_address[0]} and with port: {client_address[1]}")

    data = client_socket.recv(1024).decode()
    print("Client sent: " + data)
    reply = "Hello " + data
    client_socket.send(reply.encode())
    client_socket.close()

server_socket.close()
