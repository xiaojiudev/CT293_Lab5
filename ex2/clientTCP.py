import socket


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8888))

    user_input = input("Enter a numeric character (0-9): ")

    if len(user_input) == 1 and user_input.isnumeric():
        client_socket.send(user_input.encode())
        response = client_socket.recv(1024).decode()
        print(f"Server response: {response}")
    else:
        print("Invalid input. Please enter a single numeric character (0-9).")

    client_socket.close()


if __name__ == "__main__":
    main()
