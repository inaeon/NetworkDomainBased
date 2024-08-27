# Client Program

import socket

SERVER_IP = '192.168.8.194' #System IP which needs to communicate
SERVER_PORT = 58106


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))

    try:
        message = "Hello From Tom!"
        client_socket.sendall(message.encode())
        print(f"Sent: {message}")

    finally:
        client_socket.close()


if __name__ == "__main__":
     main()

