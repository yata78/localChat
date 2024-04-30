import socket
import os
from faker import Faker

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = 'tmp/socket_file'
print('connecting to {}'.format(server_address))

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('Starting up on {}'.format(server_address))

sock.bind(server_address)

sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        while True:
            data = connection.recv(500)
            data_str = data.decode('utf-8')
            print('Received ' + data_str)

            if data:
                fake = Faker('jp-JP')
                if data_str == '名前':
                    response = str(fake.name())
                elif data_str == 'アドレス':
                    response = str(fake.address())
                else:
                    response = data_str
                connection.sendall(response.encode())
            else:
                print('no data from', client_address)
                break
    finally:
        print("Closing current connection")
        connection.close()