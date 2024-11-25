import socket  # noqa: F401


def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    connection, _ = server_socket.accept() # wait for client
    decoded_data = connection.recv(1024).decode("utf-8").split("\n")
    for command in decoded_data:
        if command == "PING":
            connection.sendall(b"+PONG\r\n")


if __name__ == "__main__":
    main()
