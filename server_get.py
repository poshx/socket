import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 7777))
print('ouvindo')
server.listen(1)

connection, addres = server.accept()

namefile = connection.recv((100000000))

with open(namefile, 'wb') as file:
    while 1:
        data = server.recv(100000000)
        if not data:
            break
        file.write(data)

    print("Arquivo recebido")