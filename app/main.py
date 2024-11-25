import socket  # noqa: F401


def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    connection, _ = server_socket.accept() # wait for client
    print("Accepted connection!")
    try:
        while True:
            connection.recv(1024)
            connection.sendall(b"+PONG\r\n") 
    except:
        pass
    finally:
        connection.close()


if __name__ == "__main__":
    main()
