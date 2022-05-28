import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 7777))
print("Conectado!!! \n")

namefile = file='lista2.txt'


client.send(namefile.encode())

with open(namefile, 'rb') as file:
    for data in file.readlines():
        client.send(data)


print(f'{namefile} recebido!\n')