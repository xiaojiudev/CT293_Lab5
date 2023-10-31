import socket


# Define function
def get_and_display_html(url):
    # Extract the host and path from the URL
    if "://" in url:
        parts = url.split('/')
        host = parts[2]
        path = '/' + '/'.join(parts[3:])
    else:
        # Assuming HTTP if no protocol is specified
        parts = url.split('/')
        host = parts[0]
        path = '/' + '/'.join(parts[1:])

    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the web server on port 80 (HTTP)
        client_socket.connect((host, 80))

        # Send an HTTP GET request for the specified path
        request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
        client_socket.send(request.encode())

        # Receive and display the response
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(data.decode(), end='')

    except socket.error as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()


# Run function
get_and_display_html("http://streamhd4k.com")
