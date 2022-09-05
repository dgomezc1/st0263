import pika
import json
import redis

def mensaje_rec(channel, lista): 
    while True:  
        sub = channel.pubsub()
        sub.subscribe(lista)
        for message in sub.listen():
            if message['type'] == 'message':
                data  = message['data']
                #print("===================================")
                #print(f'Id: {data["id"]}\nFecha: {data["fecha"]}\nHora: {data["hora"]}\nValor: {data["datos"]}{data["tipod"]}')
                print(data)


def __main__(): 
    print("########## INICIO CONSUMER ############\n")
    print("PARA COMENZAR INGRESE LOS SIGUENTES DATOS: \n")
    while True:
        try:
            ip = input("1.Ingrese la direccion IP: ")         #Se solicita direccion IP del servicio RabbitMQ
            puerto = input("2. Ingrese el puerto : ")
            red = redis.StrictRedis(ip, puerto, charset="utf-8", decode_responses=True)
            break
        except:
            print("Error en la conexion, ingrese los datos nuevamente...")
    lista = input("Ingrese la queue a la que se desea subscribir: ")
    mensaje_rec(red, lista)
__main__()