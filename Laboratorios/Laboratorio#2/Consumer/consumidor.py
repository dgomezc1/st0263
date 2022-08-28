import pika
import json

def mensaje_rec(channel):   
    def callback(ch, method, properties, body):
        recData = True
        mensaje = json.loads(body.decode('utf-8'))
        print("-------------------------------------------")
        print(f'Id: {mensaje["id"]}\nFecha: {mensaje["fecha"]}\nHora: {mensaje["hora"]}\nValor: {mensaje["datos"]}{mensaje["tipod"]}')
    channel.basic_consume(queue="my_app", on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


def __main__(): 
    print("########## INICIO CONSUMER ############\n")
    print("PARA CONMENZAR INGRESE LOS SIGUENTES DATOS: \n")
    while True:
        try:
            ip = input("1.Ingrese la direccion IP: ")         #Se solicita direccion IP del servicio RabbitMQ
            usuario = input("2. Ingrese el usaurio del servicio RabbitMQ: ")
            contra = input("3. Ingrese la contraseña del usuario de RabbitMQ: ")
            connection = pika.BlockingConnection(pika.ConnectionParameters(ip, 5672, '/',
            pika.PlainCredentials(usuario, contra)))
            channel = connection.channel()
            break
        except:
            print("Error en la conexion, ingrese los datos nuevamente...")
    queue = input("Ingrese el exchange: ")
    mensaje_rec(channel)
__main__()