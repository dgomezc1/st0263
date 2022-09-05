Readme:
# ST0263 Tópicos Especiales en Telemática, 2022-2
#
# Estudiantes:
David Gómez Correa, dgomezc10@eafit.edu.co  
Samuel Meneses Diaz, smenesesd@eafit.edu.co
#
# Profesor:
Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#
## Proyecto 1 – 5. Simulación de MOM con características de redis

# 1. Descripción de la actividad 
## 1.1 Requerimientos funcionales y no funcionales 
Se hizo uso del middleware creado en el lab2 (MOM) y se le agregaron métodos para ser así compatible con redis.
-	Se implementa un servidor MOM con redis. Dicho servidor cumple con las siguientes funciones:
o	Recibir peticiones AMQP desde un dispositivo IOT por el puerto 5672.
o	Realizar el encolamiento de las peticiones con el algoritmo FIFO.
o	Tener un backup de los mensajes entrantes, mientras estos no superen el tamaño de la cola. Dicha backup en caso de que el consumer no se encuentre disponible.
o	Realizar el enrutamiento de los mensajes al consumer.
-	Se implementa dos simuladores de un sistema IOT con las siguientes características:
o	Crear datos aleatorios acerca de un sensor ultrasónico y un sensor de voltaje.
o	Encapsular los mensajes bajo el protocolo ARMQ (protocolo de servicios MOM), utilizando una estructura de datos tipo JSON
o	Enviar los mensajes al servidor redis corriendo en una virtual machine de AWS
-	Se implementa un consumer con las siguientes características:
o	Consumir los mensajes almacenados en la queue del servidor redis
o	Desencapsular los mensajes entrantes
o	Procesar los mensajes entrantes e imprimirlos por pantalla.


## 1.2 Requerimientos funcionales y no funcionales que no se cumplieron
Se puedo implementar todo lo solicitado en esta sección numero 5
# 2. Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
Como propuesta de solución, se implementó un middleware para ser el intermediario entre dos aplicaciones. Esto con el fin de crear dos aplicaciones desacopladas entre sí. Se crea un cliente, el cual es capaz de enviar mensajes a un servidor MOM por medio del protocolo AMQP. Dicho servidor será el encargado de la comunicación y de guardar en cola los mensajes que no han sido retirados. Por último, se implementó un consumidor el cual es capaz de retirar los mensajes enviados por el cliente, para posteriormente ser mostrados en consola. 

# 3. Descripción del ambiente de desarrollo y técnico: lenguajes de programación, librerías, paquetes, etc. con sus números de versiones.

El proyecto fue realizado utilizando el lenguaje de programación Python, para su ejecución es necesario tener instalado Python por defecto. La principal librería utilizada además de las que tiene Python por defecto es la librería redis la cual es utilizada para la comunicación con el servidor redis . Para su instalación lo único que debe de hacer es en la terminal de su editor de código fuente con el cual va a ejecutar el código ingrese el siguiente comando:
En este ejemplo de instalación, estamos usando el editor de código visual code:
```bash
Pip install redis
```
Al momento de instalar redis, se le estará instalando la version 4.3.4 de esta librería. 
Y la segunda librería seria Json, la cual nos fue útil para encapsular el diccionario, y después ser encapsulado con el utf-8.
En caso de no tener instalado Python, utilice los siguientes comandos en su terminal:
```bash
Sudo apt install Python
```


# 4. Descripción del ambiente de ejecución (en producción) lenguaje de programación, librerías, paquetes, etc. Con sus números de versiones.
Directorios:

•	/Ante-proyecto1 /MOM: Directorio donde se encuentran los scripts de consumidor y de MOM 

•	/Ante-proyecto1 /Scripts_redis: Directorio donde se encuentran los scripts de todo lo que tiene que ver con redis, como lo son, las listas el unión, los sets, entre otros. 

__Librerías utilizadas:__

•	redis: Librería utilizada para la comunicación con el servicio Redis

__IP: 18.215.164.6__

__Guia de uso:__
-	Para iniciar, es necesario inicializar máquina de AWS. Para iniciar correctamente el servicio Redis es necesario ejecutar el siguiente comando:
```bash
Redis-server
```

-	Una vez iniciado el servidor, ingresamos al directorio /Script_redis/ y ejecutamos cada uno de los scripts de la siguiente manera:
Para iniciar, es necesario inicializar máquina de AWS. Para iniciar correctamente el servicio	 MOM del servidor redis es necesario ejecutar los siguientes comandos:
•	Sudo python3 script1.py
•	Sudo python3 expiry.py
•	Sudo python3 hash.py
•	Sudo python3 listas.py
•	Sudo python3 multi.py
•	Sudo python3 sets.py
•	Sudo python3 sorted.py
•	Sudo python3 union.py

-	Para finalizar, es necesario ejecutar el archivo consumer.py (sudo python3 consumer.py), es necesario ingresar por pantalla los siguientes datos: Dirección IP,puerto, y nombre de queue. Una vez ingresados dichos datos, el servicio iniciara a consumir los mensajes almacenados en la cola. Una vez consumidos, procesara a procesarlos y mostrarlos por pantalla.

# 5.  Evidencia

__Consumidor:__
![imagen del consumidor](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/MOM/img/consumidor.png)

__Script IOT1:__
![imagen del Script IOT1](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/MOM/img/iot1.png)

__Script IOT2:__
![imagen del Script IOT2](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/MOM/img/iot2.png)

__CarpetasRedis:__
![imagen de las carpetas de redis](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/MOM/img/scriptredis.png)
 

# Referencias:
Djuric, P. (2022, 30 marzo). How to use Redis Pub/Sub in your Python Application. Medium. https://blog.devgenius.io/how-to-use-redis-pub-sub-in-your-python-application-b6d5e11fc8de


#### versión README.md -> 1.0 (2022-agosto)