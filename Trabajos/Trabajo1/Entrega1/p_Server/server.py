
from email.mime import base
from database import Databases
import socket
import configuracion

# Defining a socket object...
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)           #AF_INET define el tipo de direccion (ipv4), y modo TCP
server_address = configuracion.direccion                                       #Define la direccion del servidor
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)        #Configuracion del socket
baseDeDatos = Databases()

def main():
    print("***********************************")
    print("Server is running...")
    print("Dir IP:", server_address)
    print("Port:", configuracion.PORT)
    server_execution()

def manejador(client_connection, client_address):
    print(f'New incomming connection is coming from: {client_address[0]}:{client_address[1]}')
    is_connected = True    
    data_recevived = client_connection.recv(configuracion.RECV_BUFFER_SIZE)             
    print (f'Data received from: {client_address[0]}:{client_address[1]}')
    command  = str(data_recevived.decode(configuracion.ENCONDING_FORMAT))
    print(command)
    command = command.split()
    operacion = command[0]
    if(operacion==configuracion.GET):
        print("get")
        response  = baseDeDatos.get(command[1])
        client_connection.sendall(response)
    elif(operacion==configuracion.SET):
        print("set")
        response  = baseDeDatos.save(command[1], command[2])
        client_connection.sendall(response)
    elif(operacion==configuracion.UPDATE):
        print("update")
        response  = baseDeDatos.save(command[1], command[2])
        client_connection.sendall(response)
    else:
        response  = baseDeDatos.delete(command[1])
        client_connection.sendall(response)
    print(f'Now, client {client_address[0]}:{client_address[1]} is disconnected...\n')
    client_connection.close()                          

def server_execution():
    tuple_connection = (server_address, configuracion.PORT)                      
    server_socket.bind(tuple_connection)                                    
    print ('Socket is bind to address and port...')
    server_socket.listen(5)                                                 
    print('Socket is listening...')
    while True:
        client_connection, client_address = server_socket.accept()
        manejador(client_connection, client_address)


    print('Socket is closed...')
    server_socket.close()


if __name__ == "__main__":
    main()
