import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

while True:
    data, address = UDPServerSocket.recvfrom(bufferSize)
    message = data.decode('utf-8').strip()

    try:
        parts = message.split()

        print("Client request: ", parts)  # format: ['+', '100', '200']

        result = 0

        if (len(parts) == 3
                and parts[0] in ('+', '-', '*', '/')
                and parts[1].isdigit()
                and parts[2].isdigit()):
            operand1, operator, operand2 = int(parts[1]), parts[0], int(parts[2])

            if operator == '+':
                result = operand1 + operand2
            elif operator == '-':
                result = operand1 - operand2
            elif operator == '*':
                result = operand1 * operand2
            elif operator == '/':
                if operand2 != 0:
                    result = operand1 / operand2
                else:
                    UDPServerSocket.sendto("Division by zero error".encode('utf-8'), address)
                    continue

            UDPServerSocket.sendto(str(result).encode('utf-8'), address)
        else:
            UDPServerSocket.sendto("Invalid format. Use 'Operand1 Operator Operand2' format.".encode('utf-8'),
                                   address)
    except (ValueError, IndexError):
        UDPServerSocket.sendto("Invalid format. Use 'Operand1 Operator Operand2' format.".encode('utf-8'),
                               address)
