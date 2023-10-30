import socket


def convert_to_word(data):
    conversion_dict = {
        '0': "zero",
        '1': "one",
        '2': "two",
        '3': "three",
        '4': "four",
        '5': "five",
        '6': "six",
        '7': "seven",
        '8': "eight",
        '9': "nine"
    }

    return conversion_dict.get(data, "Not an integer")


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8888))
    server_socket.listen(1)
    print("Server is listening on port 8888...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        data = client_socket.recv(1).decode()

        response = convert_to_word(data)
        client_socket.send(response.encode())

        client_socket.close()


if __name__ == "__main__":
    main()
