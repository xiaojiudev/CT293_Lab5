import socket

HOST = "localhost"
PORT = 8000
PORT1 = 8001


def handle_get():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client1.connect((HOST, PORT1))

    filename = input("\nEnter the name of the file to retrieve: ")
    request = "GET " + filename
    client.send(request.encode("utf-8"))

    response = client.recv(1024).decode("utf-8")

    if response == "OK\n":
        with open(f"client_storage/{filename}", "w") as serverFile:
            while True:
                data = client1.recv(1024)
                if not data:
                    break
                serverFile.write(data.decode("utf-8"))
        print(f"\nFile received and saved in client_storage directory: {filename}")
        with open(f"client_storage/{filename}", "r") as clientFile:
            contents = clientFile.read()
            print(f"\nFile contents: {contents}")
    else:
        print("Server on port 8000 Response:", response)


def handle_delete():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client1.connect((HOST, PORT1))

    filename = input("\nEnter the name of the file to delete: ")
    request = "DELETE " + filename
    client.send(request.encode("utf-8"))

    response = client.recv(1024).decode("utf-8")

    if response == "OK\n":
        print("\nFile has been deleted on the server")
    else:
        print("Server on port 8000 Response:", response)


def handle_list():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client1.connect((HOST, PORT1))

    filename = input("\nEnter the folder name: ")
    request = "LIST " + filename
    client.send(request.encode("utf-8"))

    response = client.recv(1024).decode("utf-8")

    if response == "OK\n":
        file = client1.recv(1024)
        array = eval(file.decode("utf-8"))
        file_list = ', '.join(array)
        print(f'\nFiles in the {filename} directory are: {file_list}\n')
    else:
        print("Server on port 8000 Response:", response)


test = True
while test:
    print('\n' + '-' * 40 + '\n')
    print("Press 1 to choose the GET function\n")
    print("Press 2 to choose the DELETE function\n")
    print("Press 3 to choose the LIST function")
    print('\n' + '-' * 40 + '\n')
    a = (input("Choose one of the three functions to perform: "))
    if a == "1":
        handle_get()
    if a == "2":
        handle_delete()
    if a == "3":
        handle_list()
    if a == "":
        test = False
        print("End of work session")


