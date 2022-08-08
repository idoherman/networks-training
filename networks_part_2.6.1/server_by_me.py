import socket
import datetime
import random


def send_time(client_socket):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    reply = "My time here is: " + current_time + " :)"
    client_socket.send(reply.encode())


def send_name(client_socket):
    name = "Ido's Server"
    reply = "The server name is: " + name + " :)"
    client_socket.send(reply.encode())


def send_random_num(client_socket):
    num = random.randint(0, 10)
    reply = f"My random num is:  {num} :)"
    client_socket.send(reply.encode())


def server_run():
    server_socket = socket.socket()

    server_socket.bind(('0.0.0.0', 11111))
    server_socket.listen()
    print("server is up and running")
    while True:
        (client_socket, client_address) = server_socket.accept()
        print(f"Client connected with ip: {client_address[0]} and with port: {client_address[1]}")

        is_exit = False
        while not is_exit:
            data = client_socket.recv(4).decode()
            print("Client sent: " + data)
            if data == "TIME":
                send_time(client_socket)

            elif data == "WHOU":
                send_name(client_socket)

            elif data == "RAND":
                send_random_num(client_socket)

            elif data == "EXIT":
                is_exit = True
                client_socket.close()

    server_socket.close()


if __name__ == '__main__':
    server_run()
