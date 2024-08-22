import socket

SERVER_IP = '0.0.0.0'
SERVER_PORT = 58106


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(1)

    print(f"Server is listening form {SERVER_IP} on port :{SERVER_PORT}")

    connection, client_address = server_socket.accept()

    try:
        print(f"Connection from : {client_address}")

        while True:
            data = connection.recv(1024)

            if data:
                print(f"Received : {data.decode()}")

            else:
                break
    finally:
        connection.close()


if __name__ == "__main__":
    main()


