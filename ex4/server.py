import socket
import os

HOST = 'localhost'
PORT = 8000
PORT1 = 8001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server1.bind((HOST, PORT1))

server.listen(1)
server1.listen(1)

print('Server on port 8000 is ready to accept connections')

while True:
    conn, add = server.accept()
    conn1, add1 = server1.accept()

    request = conn.recv(1024).decode('utf-8')
    filename = request.split()[1]
    method = request.split()[0]

    if method == 'GET':
        if os.path.isfile("server_storage/" + filename):
            conn.send(b'OK\n')
            with open("server_storage/" + filename, 'r') as f:
                data = f.read()
                conn1.send(data.encode('utf-8'))
            print('File sent to', add)
            print('Content:', data)
        else:
            print('File not found:', filename)
            conn.send(b'ERROR\n')

    if method == 'DELETE':
        file_path = os.path.join("server_storage", filename)
        if os.path.isfile(file_path):
            conn.send(b'OK\n')
            os.remove(file_path)
            print("File", filename, "has been deleted from the server's server_storage directory")
        else:
            conn.send(b'ERROR\n')
            print('File not found:', filename)

    if method == 'LIST':
        if os.path.isdir(filename):
            conn.send(b'OK\n')
            files = os.listdir(filename)
            print(files)
            data = (str(files).encode('utf-8'))
            conn1.send(data)
        else:
            conn.send('ERROR\n'.encode('utf-8'))
            print('Folder not found:', filename)
    conn.close()
    conn1.close()
