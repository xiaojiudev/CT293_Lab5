import socket

serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while True:
    user_input = input("Enter a calculation (e.g., 100 + 200) or 'q' to quit: ")

    if user_input.lower() == 'q':
        break

    try:
        operator, operands = user_input.split()[1], user_input.split()[:1] + user_input.split()[2:]
        formatted_message = f"{operator} {' '.join(operands)}"

        message = formatted_message.encode('utf-8')
        UDPClientSocket.sendto(message, serverAddressPort)

        response, _ = UDPClientSocket.recvfrom(bufferSize)
        print(f"\nServer response: {response.decode('utf-8')}\n")
    except ValueError:
        print("Invalid input. Use 'Operand1 Operator Operand2' format.\n")
