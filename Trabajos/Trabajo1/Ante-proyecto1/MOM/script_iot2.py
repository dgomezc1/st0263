from datetime import date, datetime
import random
import time
import redis
import json


def __connection__():               #Funcion para crear conexion con RabbitMQ
    while True:
        try:
            ip = input("Ingrese la direccion IP: ")             #Se solicita direccion IP del servicio RabbitMQ
            puerto = input("Ingrese el puerto: ")
            red = redis.StrictRedis(ip,puerto, charset="utf-8", decode_responses=True)   
            queue = input("Ingrese el queue: ")
            return red, queue                               #Retornamos el canal
        except: 
            print("Error al conectarse a la maquina ;(\n intente de nuevo...")

def __tiempo__():                                               #Funcion para calcular la fecha y hora actual
    ahora = datetime.now()
    fecha = str(ahora.year)+'/'+str(ahora.month)+'/'+str(ahora.day)
    hora = str(ahora.hour)+":"+str(ahora.minute)+":"+str(ahora.second)
    return fecha,hora                                           #Return de fecha y hora actual


def __main__():                                                 #Funcion principal (inicio de programa simulador iot), el simulador es de voltaje
    channel, queue = __connection__()                           #Se inicializa la conexion con el servidor RabbitMQ
    i = 10
    while(i >= 0):                                              #Creamos un loop infinito para la creacion de numeros random de voltaje
        i = round(random.uniform(1,40),2)                       #Se redondea i a dos decimales y sacara un numero random decimal de 1-40
        fecha,hora = __tiempo__()
        mensaje = {"id":2,"fecha":fecha,"hora":hora,"datos":i,"tipod":"V"}  #Cargamos los datos del id, fecha, hora, distancia en un diccionario
        print(mensaje)                                          #Imprimimos el mensaje a enviar
        mensaje = json.dumps(mensaje)           #Codificamos en formato json de bytes para poder enviar el diccionario por el channel
        channel.publish(queue, mensaje)  #Publicamos los datos a la cola correspondiente
        time.sleep(5.0)

__main__()




