import socket


def send_exit(my_socket):
    my_socket.send("04EXIT".encode())
    return "EXIT"


def send_get_msg(my_socket, client_msg):
    length_msg = len(client_msg)

    if length_msg >= 100:
        print("The length is over 99 chars so the message will not be sent :(")
        return

    length_msg = str(length_msg).zfill(2)
    msg = length_msg + client_msg
    my_socket.send(msg.encode())

    length_server_msg = int(my_socket.recv(2).decode())
    server_msg = my_socket.recv(length_server_msg).decode()
    print("The server sent the message: " + server_msg)


def messages_for_server(port):
    client_msg = None
    print("If you want to stop send messages, just type the word: 'EXIT' ")

    my_socket = socket.socket()
    my_socket.connect(('127.0.0.1', port))

    while client_msg != "EXIT":

        client_msg = input("please type your message: \n")

        if client_msg.upper() == "EXIT":
            client_msg = send_exit(my_socket)
            print("done with sending messages :)")

        else:
            send_get_msg(my_socket, client_msg)

    my_socket.close()


if __name__ == '__main__':
    messages_for_server(9999)
