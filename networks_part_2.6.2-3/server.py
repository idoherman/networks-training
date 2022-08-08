import socket
import datetime
import random


def send_time(client_socket):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    reply = "My time here is: " + current_time + " :)"
    length_msg = len(reply)
    length_msg = str(length_msg).zfill(2)
    reply = str(length_msg) + reply
    client_socket.send(reply.encode())


def send_name(client_socket):
    name = "Ido's Server"
    reply = "The server name is: " + name + " :)"
    length_msg = len(reply)
    length_msg = str(length_msg).zfill(2)
    reply = str(length_msg) + reply
    client_socket.send(reply.encode())


def send_random_num(client_socket):
    num = random.randint(0, 10)
    reply = f"My random num is:  {num} :)"
    length_msg = len(reply)
    length_msg = str(length_msg).zfill(2)
    reply = str(length_msg) + reply
    client_socket.send(reply.encode())


def send_no_request(client_socket, client_msg):
    reply = f"'{client_msg}' is not an existing request"
    length_msg = len(reply)
    length_msg = str(length_msg).zfill(2)
    reply = str(length_msg) + reply
    client_socket.send(reply.encode())


def get_send_msg(client_socket):
    length_client_msg = int(client_socket.recv(2).decode())
    client_msg = client_socket.recv(length_client_msg).decode()
    print("The client sent the message: " + client_msg)
    if client_msg.upper() == "EXIT":
        return True
    elif client_msg.upper() == "TIME":
        send_time(client_socket)
        return False
    elif client_msg.upper() == "WHORU":
        send_name(client_socket)
        return False
    elif client_msg.upper() == "RAND":
        send_random_num(client_socket)
        return False
    else:
        send_no_request(client_socket, client_msg)


def server_run():
    server_socket = socket.socket()

    server_socket.bind(('0.0.0.0', 9999))
    server_socket.listen()
    print("server is up and running")

    while True:
        (client_socket, client_address) = server_socket.accept()
        print(f"Client connected with ip: {client_address[0]} and with port: {client_address[1]}")

        is_exit = False
        while not is_exit:
            is_exit = get_send_msg(client_socket)

        client_socket.close()
        print("The client left the server :(")

    server_socket.close()


if __name__ == '__main__':
    server_run()
