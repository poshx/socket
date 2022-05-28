import socket
import threading
def inicio():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(('localhost', 7777))
    print('ouvindo')
    server.listen(3)

    connection, addres = server.accept()




    namefile = connection.recv(1024).decode()

    with open(namefile, 'rb') as file:
        for data in file.readlines():
            connection.send(data)

        print("Arquivo enviado")
        connection.close()


def start():
    inicio()

    while(True):
            thread = threading.Thread(target=start)
            thread.start()
start()