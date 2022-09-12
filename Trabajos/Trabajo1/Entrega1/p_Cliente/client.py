# ********************************************************************************************
    # Proyecto 2
    # Course: ST0255 - Telemática
    # MultiThread TCP-SocketServer
    #Samuel Meneses Diaz
    #David Gomez Correa
# ********************************************************************************************

# Import libraries for networking communication and concurrency...

import socket
import constants

def validador(h):
    return True

def main(direccion, port):
    try: 
        command_to_send = ""
        while command_to_send != constants.QUIT : 
            command_to_send = input("DB>>")
            client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)           
            if validador(command_to_send) and command_to_send != constants.QUIT: 
                client_socket.connect((direccion,port))                                        
                client_socket.send(bytes(command_to_send,constants.ENCONDING_FORMAT))   #Se codifica el mensaje y se envia
                data_received = client_socket.recv(10000000)
                print(data_received.decode("utf-8"))                            #Recibimos la informacion que llega del servidor
                client_socket.close()                                           
            elif command_to_send == constants.QUIT:
                break
            else:       
                print('Please enter a valid command')                                   #En caso de ingresar un comando invalido
            #client_socket.connect((direccion,port, host_send))  
    except Exception as e:                                                              #Excepcion en caso de ocurrir un error
        print(e)
        print('Error, please try again...')

    print('Closing connection...BYE BYE...')                                            #Final del programa
    client_socket.close()     

if __name__ == '__main__':
    print('***********************************')            #Inicio del programa
    print('Client is running...')
    direccion = input('Enter the IP Address: ')             #Se le pide por pantalla al usuario direccion y puerto
    port = int(input('Enter the Port: '))
    print('***********************************') 
    print('\nEnter \"QUIT\" to exit')                                       #Impresion con mensajes para ususrio
    print('Input commands:')
    print('QUIT, GET, SET, UPDATE, DELETE\n')                                               #Ingreso del comando por parte del usuario
    main(direccion, port)