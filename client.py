import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 7777))
print("Conectado!!! \n")


namefile = str(input('Arquivo>'))

client.send(namefile.encode())



with open(namefile, 'wb') as file:
    while 1:
        data = client.recv(1000000)
        file.write(data)
        exit()


print(f'{namefile} recebido!\n')