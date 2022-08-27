import socket


def send_exit(my_socket):
    my_socket.send("EXIT".encode())
    return "EXIT"


def send_get_msg(my_socket, client_msg):
    if client_msg[0:3:].upper() == "DIR":
        my_socket.send(client_msg.encode())
        server_msg = my_socket.recv(1024).decode()
        print("The server sent the message: " + server_msg)

    elif client_msg[0:6:].upper() == "DELETE":
        my_socket.send(client_msg.encode())
        server_msg = my_socket.recv(1024).decode()
        print("The server sent the message: " + server_msg)


def messages_for_server(port):
    client_msg = None
    print("If you want to stop send messages, just type the word: 'EXIT' ")

    my_socket = socket.socket()
    my_socket.connect(('127.0.0.1', port))

    while client_msg != "EXIT":

        client_msg = input("Please type your command and the path (command = DIR/DELETE): \n")

        if client_msg.upper() == "EXIT":
            client_msg = send_exit(my_socket)
            print("done with sending messages :)")

        else:
            if client_msg[0:3:].upper() == "DIR":
                client_msg = "DIR" + client_msg[3:].strip(" ")
                send_get_msg(my_socket, client_msg)

            elif client_msg[0:6:].upper() == "DELETE":
                client_msg = "DELETE" + client_msg[6:].strip(" ")
                send_get_msg(my_socket, client_msg)
            else:
                print(f"There isn't a command like that: {client_msg}")

    my_socket.close()


if __name__ == '__main__':
    messages_for_server(7777)
