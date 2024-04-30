import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = 'tmp/socket_file'
print('connecting to {}'.format(server_address))

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    while True:
        message = input()
        sock.sendall(message.encode())

        try:
            while True:
                data = bytes(sock.recv(500))
    
                if data:
                    data_str = data.decode('utf-8')
                    print(data_str)
                else:
                    break
        except(TimeoutError):
            print('Socket timeout, ending listening for server messages')
    
finally:
    print('closing socket')
    sock.close()