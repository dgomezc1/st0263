# ST0263 Tópicos Especiales en Telematica, 2022-2

__Estudiantes:__

 David Gómez Correa, dgomezc10@eafit.edu.co  
 Samuel Meneses Diaz, smenesesd@eafit.edu.co

__Profesor:__

 Edwin Nelson Montoya Munera, emontoya@eafit.edu.co

---

# Laboratorio #2 - RabbitMQ
__Middleware Orientados a mensajes (MOM)__

- [Laboratorio 2](#laboratorio-2---rabbitmq)
  - [Descripción de la actividad](#1-descripción-de-la-actividad)
  - [información general](#2-información-general-de-diseño-de-alto-nivel-arquitectura-patrones-mejores-prácticas-utilizadas)
  - [Descripcion ambiente desarrollo y tecnico](#3-descripción-del-ambiente-de-desarrollo-y-técnico-lenguajes-de-programación-librerías-paquetes-etc-con-sus-números-de-versiones)
  - [Descripcion ambiente en produccion](#4-descripción-del-ambiente-de-ejecución-en-producción-lenguaje-de-programación-librerías-paquetes-etc-con-sus-números-de-versiones)
  - [Informnacion relevante](#5-nota-importante)

--- 

## 1. Descripción de la actividad
### 1.1 Requerimientos funcionales y no funcionales
Se desplego un middleware orientado a mensajes (MOM) para así afianzar el desarrollo y despliegue de un sistema distribuido con un intermediario que en este caso sería el middleware RabbitMQ 

- Se implementa un servidor MOM con RabbitMQ. Dicho servidor cumple con las siguientes funciones:
  
    - Recibir peticiones AMQP desde un dispositivo IOT por el puerto 5672. 

    - Realizar el encolamiento de las peticiones con el algoritmo FIFO. 

    - Tener un backup de los mensajes entrantes, mientras estos no superen el tamaño de la cola. Dicha backup en caso de 
 que el consumer no se encuentre disponible. 

    - Realizar el enrutamiento de los mensajes al consumer. 

-  Se implementa dos simuladores de un sistema IOT con las siguientes características:

    -  Crear datos aleatorios acerca de un sensor ultrasónico y un sensor de voltaje. 

    - Encapsular los mensajes bajo el protocolo ARMQ (protocolo de servicios MOM), utilizando una estructura de datos tipo JSON 

    - Enviar los mensajes al servidor Rabbit MQ corriendo en una virtual machine de AWS 

- Se implementa un consumer con las siguientes características: 

    - Consumir los mensajes almacenados en la queue del servidor RabbitMQ 

    - Desencapsular los mensajes entrantes 

    - Procesar los mensajes entrantes e imprimirlos por pantalla. 


### 1.2 Requerimientos funcionales y no funcionales que no se cumplieron

El requerimiento funcionales que no se pudo llevar a cabo fue hacer la interfaz gráfica tipo ubidots, en cambio los datos serán imprimidos por pantalla 
 

---
## 2.  Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas. 
Como propuesta de solución, se implementó un middleware para ser el intermediario entre dos aplicaciones. Esto con el fin de crear dos aplicaciones desacopladas entre sí. Se crea un cliente, el cual es capaz de enviar mensajes a un servidor MOM por medio del protocolo AMQP (Arquitectura producer - consumer ). Dicho servidor será el encargado de la comunicación y de guardar en cola los mensajes que no han sido retirados (Middleware). Por último, se implementó un consumidor el cual es capaz de retirar los mensajes enviados por el cliente, para posteriormente ser mostrados en consola.

---
## 3. Descripción del ambiente de desarrollo y técnico: lenguajes de programación, librerías, paquetes, etc. con sus números de versiones. 
El laboratorio fue realizado utilizando el lenguaje de programación Python, para su ejecución es necesario tener instalado Python por defecto. La principal librería utilizada además de las que tiene Python por defecto es la librería pika la cual es utilizada para la comunicación con el servidor RabbitMQ. Para su instalación lo único que debe de hacer es en la terminal de su editor de código fuente con el cual va a ejecutar el código ingrese el siguiente comando: 

En este ejemplo de instalación, estamos usando el editor de código visual studio code: 

```bash 
Pip install pika 
```

Al momento de instalar pika, se le estará instalando la versión 1.3.0 de esta librería.  

El proyecto cuenta con dos paquetes principales, uno de ellos es GenerarNumerosRand y Consumer. El primero de ellos es el encargado de simular los dos sensores de tipo arduino, para poder recrear el sistema IOT. El segundo se encarga de simular nuestro consumidor. 

Dentro del paquete GenerarNumerosRand tenemos dos scripts: `script_iot1.py` y `script_iot2.py`. Ambos scripts tienen un flujo de proceso similar y efectos prácticos vamos a explicar uno de ellos a continuación.

Funciones principales `script_iot1.py`:  

- **connection:** Esta función es la encargada de establecer la conexión con nuestro servidor RabbitMQ, para ello es necesario ingresar los siguientes datos:
    - Usuario ("user")
    - Contraseña ("password")
    - Exchange ("my_exchange")
    - Direccion IP ("35.174.100.150")
    - Routing key ("test")

- **tiempo:** Esta función es la encargada de tomar el tiempo actual y formatearlo.

- **envio_datos:** Esta función es la encargada de enviar el mensaje al servidor RabbitMQ. Para ello utiliza el diccionario como estructura de datos, para posteriormente almacenar cada uno de los datos (Id, fecha, hora, dato, tipo). Igualmente, es la encargada de generar el numero random para simular nuestro sistema IOT. Una vez los datos estén en el diccionario, procede a codificarlos con base al utf-8. Para finalizar realiza la publicación de los datos hacia el exchange con base a la routing key. 

- **main:** Esta función es nuestro controlador de flujo, se encargar básicamente de redirigir el proceso a la función correspondiente.

Dentro del paquete Consumer se encuentra nuestro script `Consumidor.py`. Dicho script es el encargado de simular nuestro consumidor. Para ello emplea la función mensaje_rec, que se encarga de conectarse con el servidor rabbitMQ y realizar el procesamiento de los mensajes entrantes de nuestro sistema IOT.

- **mensaje_rec:** Esta función es la encargada de establecer la conexión con nuestro servidor RabbitMQ, para ello es necesario ingresar los siguientes datos:
    - Usuario ("user")
    - Contraseña ("password")
    - Exchange ("my_exchange")
    - Direccion IP ("35.174.100.150")

__Directorios:__
- **/Laboratorio2/GenerarNumerosRand:** Directorio donde se encuentran los scripts de simulación de datos IOT 
- **/Laboratorio2/Consumer:** Directorio donde se encuentra el script del `Consumidor.py`
 

---
## 4. Descripción del ambiente de ejecución (en producción) lenguaje de programación, librerías, paquetes, etc. Con sus números de versiones. 



__librerías usadas:__
- Pika: Librería utilizada para la comunicación con el servidor RabbitMQ 

__IP:__ 35.174.100.150

__Guía de uso:__
1. Para iniciar, es necesario inicializar máquina de AWS. Para iniciar correctamente el servicio MOM del servidor RabbitMQ es necesario ejecutar los siguientes comandos: 

2. En la maquina de aws debe iniciar el docker con el siguiente comando:

    - `sudo docker start cbea1cb41973676516439a6d52d9abbe9dd4567b1642f6a01152d59330ad658c`

    - `docker ps`

3. Ejecución de simuladores sistema IOT, ejecutar los siguientes comandos: 

    - `sudo python3 script_iot1.py`

    - `sudo python3 script_iot2.py`

4. Ejecución de sistema consumidor: 

    - `sudo python3 consumidor.py`

Posterior a la ejecución del archivo script_iot1.py y script_iot2.py (sudo python3 script_iot1.py), es necesario ingresar por pantalla los datos correspondientes a: Dirección ip, usuario, contraseña, Exchange. Una vez digitados dichos datos, el script iniciara a enviar datos de manera aleatoria del sensor correspondiente.  

Para finalizar, es necesario ejecutar el archivo consumer.py (sudo python3 consumer.py), es necesario ingresar por pantalla los siguientes datos: Dirección IP, usuario, contraseña y nombre de queue. Una vez ingresados dichos datos, el servicio iniciara a consumir los mensajes almacenados en la cola. Una vez consumidos, empezara a procesarlos y mostrarlos por pantalla. 

---
## 5. NOTA IMPORTANTE!!.

Para poder conectarse al servidor de RabbitMQ es necesario ingresar unos datos tanto en los scripts de sistemas IOT, como en el consumidor. Dichos datos se listan acontinuacion:

- **Usuario =** "user"
- **Contraseña =** "password"
- **Exchange =** "my_exchange"
- **Direccion IP =** "35.174.100.150"
- **Routing key =** "test"



#### versión README.md -> 1.0 (2022-agosto)