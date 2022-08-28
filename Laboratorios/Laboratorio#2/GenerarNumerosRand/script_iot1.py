from datetime import date, datetime
import random
import time
import pika
import json

def __connection__():                   #Funcion para crear conexion con RabbitMQ
    while True:
        ip = input("Ingrese la direccion IP: ")         #Se solicita direccion IP del servicio RabbitMQ
        try:
            usuario = input("Ingrese el usaurio del servicio RabbitMQ: ")
            contra = input("Ingrese la contraseña del usuario de RabbitMQ: ")
            connection = pika.BlockingConnection(pika.ConnectionParameters(ip,5672,'/',pika.PlainCredentials(usuario,contra)))   #Intentamos conectarnos al servicio con usuario y contraseña ingresados
            channel = connection.channel()              #En caso de tener una conexion exitosa, creamos el canal
            queue = input("Ingrese el exchange: ")
            routing = input("Ingrese la routing_key: ")
            return channel, queue, routing                             #retornamos el  canal
        except:
            print("Error al conectarsea a la maquina :(\n Intente de nuevo...")

def __tiempo__():                                                       #Funcion para calcular la fecha y hora actual
    ahora = datetime.now()
    fecha = str(ahora.year)+'/'+str(ahora.month)+'/'+str(ahora.day)
    hora = str(ahora.hour)+":"+str(ahora.minute)+":"+str(ahora.second)
    return fecha,hora                                                   #Return de fecha y hora actual

def __envio_datos__(queue, distancia1, distancia2, ini, fin,channel, routing):
    sim = random.randrange(ini,fin)  
    for i in range(distancia1,distancia2,sim):
        if distancia2+sim<0 or distancia2+sim>100:
            break
        fecha,hora = __tiempo__()
        mensaje = {"id":1,"fecha":fecha,"hora":hora,"datos":i,"tipod":"cm"}                #Cargamos los datos del id, fecha, hora, distancia en un diccionario
        print(mensaje)                                                                  #Imprimimos el mensaje a enviar
        mensaje = json.dumps(mensaje).encode('utf-8')                                   #Codificamos en formato json de bytes para poder enviar el diccionario por el channel
        channel.basic_publish(exchange=queue,routing_key=routing,body=mensaje)           #Publicamos los datos a la cola correspondiente
        time.sleep(5.0)
        sim = random.randrange(ini,fin) 


def __main__():                                                                #Funcion pricipal (inicio de programa simulador iot), el simulador es de un sensor ultra sonico
    channel, queue, routing = __connection__()                                          #Se inicializa la conexion con el servicio de RabbitMQ
    distancia1 = random.randrange(0,100)                                       #Calculamos un numero random para iniciar el simulador
    while True:                                                                #Creamos loop infinito de ejecicion
        if distancia1+20>=100:                                                 #Limitamos la sensibilidad de nuestro sensor entre 0 cm y 100 cm
            distancia2 = random.randrange(80,100)
        else:
            distancia2 = random.randrange(distancia1-20,distancia1+20)
        if distancia1> distancia2:                                                              #Simulacion del disminucion de la distancia
            __envio_datos__(queue, distancia2, distancia1, -5, -1, channel, routing)
        else:
            __envio_datos__(queue, distancia1, distancia2, 1, 5, channel, routing)
        distancia1 = distancia2
        time.sleep(5.0)


__main__()