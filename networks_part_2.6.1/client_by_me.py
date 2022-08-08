import socket


def get_time(my_socket):
    my_socket.send("TIME".encode())
    server_time = my_socket.recv(1024).decode()
    print(server_time)


def get_server_name(my_socket):
    my_socket.send("WHOU".encode())
    server_name = my_socket.recv(1024).decode()
    print(server_name)


def get_random_num(my_socket):
    my_socket.send("RAND".encode())
    server_random_num = my_socket.recv(1024).decode()
    print(server_random_num)


def send_exit(my_socket):
    my_socket.send("EXIT".encode())


def requests_from_server(port):
    client_input = "nothing important"
    print("If you want to stop - send requests, just type the word: 'EXIT' ")

    my_socket = socket.socket()
    my_socket.connect(('127.0.0.1', port))

    while client_input != "EXIT":
        client_input = input("please type your request: \n")

        if client_input == "TIME":
            get_time(my_socket)

        elif client_input == "WHORU":
            get_server_name(my_socket)

        elif client_input == "RAND":
            get_random_num(my_socket)

        elif client_input == "EXIT":
            send_exit(my_socket)
            print("done requests :)")
        else:
            print(f"{client_input} is not an existing request")

    my_socket.close()


if __name__ == '__main__':
    requests_from_server(11111)
