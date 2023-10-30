import socket

HOST = 'localhost'
PORT = 8000
PORT1 = 8001


def handle_get():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client1.connect((HOST, PORT1))

    filename = input('Enter the name of the file to retrieve: ')
    request = 'GET ' + filename
    client.send(request.encode('utf-8'))

    response = client.recv(1024).decode('utf-8')

    if response == 'OK\n':
        with open(filename, 'w') as f:
            while True:
                data = client1.recv(1024)
                if not data:
                    break
                f.write(data.decode('utf-8'))
        print('File received and saved:', filename)
        with open(filename, 'r') as a:
            contents = a.read()
            print("File contents:", contents, "\n")
    else:
        print("Server on port 8000 Response:", response)


def handle_delete():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client1.connect((HOST, PORT1))

    filename = input('Enter the name of the file to delete: ')
    request = 'DELETE ' + filename
    client.send(request.encode('utf-8'))

    response = client.recv(1024).decode('utf-8')

    if response == 'OK\n':
        print("File has been deleted on the server")
    else:
        print("Server on port 8000 Response:", response)


def handle_list():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client1.connect((HOST, PORT1))

    filename = input('Enter the folder name: ')
    request = 'LIST ' + filename
    client.send(request.encode('utf-8'))

    response = client.recv(1024).decode('utf-8')

    if response == 'OK\n':
        file = client1.recv(1024)
        array = eval(file.decode('utf-8'))
        print("Files in ", filename, "are:")
        for f in array:
            print(f)
        print("\n")
    else:
        print("Server on port 8000 Response:", response)


test = True
while test:
    print("Press 1 to choose the GET function\n")
    print("Press 2 to choose the DELETE function\n")
    print("Press 3 to choose the LIST function\n")
    a = (input("Choose one of the three functions to perform: "))
    if a == '1':
        handle_get()
    if a == '2':
        handle_delete()
    if a == '3':
        handle_list()
    if a == '':
        test = False
        print("End of work session")
