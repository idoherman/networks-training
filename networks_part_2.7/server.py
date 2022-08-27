import socket
import glob
import os


def get_send_msg(client_socket):

    client_msg = client_socket.recv(1024).decode()
    print("The client sent the message: " + client_msg)

    if client_msg.upper() == "EXIT":
        return True

    elif client_msg[0:3:].upper() == "DIR":

        if os.path.exists(client_msg[3::]):
            files_format = os.path.join(client_msg[3::], "*")
            files_list = glob.glob(files_format)
            files_in_dir = ""

            for name_of_file in files_list:
                files_in_dir += name_of_file + "\n"

            client_socket.send(files_in_dir.encode())
            return False
        else:
            client_socket.send("The path doesn't exist :(".encode())
    elif client_msg[0:6:].upper() == "DELETE":

        if os.path.exists(client_msg[6::]):
            os.remove(client_msg[6::])
            client_socket.send("The file deleted :)".encode())
        else:
            client_socket.send("The path doesn't exist :(".encode())


def server_run():
    server_socket = socket.socket()

    server_socket.bind(('0.0.0.0', 7777))
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


