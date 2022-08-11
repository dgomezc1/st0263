# ST0263 Tópicos Especiales en Telemática

__Estudiante: David Gomez Correa, dgomezc10@eafit.edu.co__

__Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co__

----

## Laboratorio 1 ##

----

- [Laboratorio 1](#laboratorio-1)
  - [Descripción de la actividad](#1-descripción-de-la-actividad)
  - [información general](#2-información-general-de-diseño-de-alto-nivel-arquitectura-y-patrones)
  - [descripción del ambiente de desarrollo](#3-descripción-del-ambiente-de-desarrollo-y-técnico-lenguaje-de-programación-librerias-paquetes-etc-con-sus-numeros-de-versiones)
  - [descripción del ambiente en produccion](#4-descripción-del-ambiente-de-ejecución-en-producción-lenguaje-de-programación-librerias-paquetes-etc-con-sus-numeros-de-versiones)
  - [información relevante](#5-informacion-relevante)

---

### 1. Descripción de la actividad ###

__1.1. Requerimientos funcionales y no funcionales__

- Se implementa un Mini-servidor web minimalista, que implementa el método GET (versión 0.9). Dicho servidor cumple con las siguientes funciones:
    - Recibe peticiones HTTP a nivel de sockets TCP en el puerto 80
    - Procesa los mensajes entrares por sockets, en este caso un HTTP request
    - Es capaz localizar el recurso del HTTP request
    - Envia HTTP Response con el recurso pedido
    - El servidor es concurrente, permite múltiples conexiones al tiempo
    - El servidor imprime por panta las peticiones entrantes y las respuestas salientes
    - El servidor se encuentra desplegado en una maquina virtual de AWS (Dir ip: `54.145.202.4`)
    - El servidor entrega los siguientes tipos de archivos:
        - mp4
        - png
        - jpg
        - pdf
        - html

----

### 2. información general de diseño de alto nivel, arquitectura y patrones. ###

Como propuesta de solucion, se plantea un servidor minimalista, que con base al protocolo HTTP v0.9 es capaz de procesar Resquest GET, y retornar el recurso solicitado (en caso de existir) utilizando un HTTP Response. además, se utiliza un patrón de arquitectura por capas, en la cual se distinguen en la capa de control de flujo y la capa de procesamiento

----

### 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerías, paquetes, etc, con sus números de versiones. ###

El laboratorio fue realizado utilizando el lenguaje de programación de Python, para su ejecución, únicamente es necesario tener instalado Python por defecto, ya que este incluye las librerías necesarias para su ejecución. Para correrlo, únicamente es necesario ejecutar el archivo Server.py con el siguiente comando `python Server.py`, con el cual iniciara la ejecución del proyecto.

Dicho archivo Server.py es el controlador de flujo principal, el se encarga de las funciones más relevantes a nivel de conexión, como lo son:
- **creación de Socket y configuración de socket:** Se encarga de crear el socket, con base a una dirección IP preestablecida en el archivo *constans.py*, y un puerto también definido dentro de este mismo archivo. Cabe aclarar que dicho socket se configura para funcionar sobre el protocolo TCP.
- **Apertura de socket:** Se inicializa el socket con la dupla puerto - IP, posterior a ello se define un pull de conexiones máximo de 5, y se coloca visible dicho puerto.
- **Servidor concurrente:** Para poder configurar nuestro servidor como concurrente, dentro de la función *server_execution*, se utiliza la librería threading, que nos permite crear hilos, logrando de esta manera ejecutar el control de flujo de aplicación en un nuevo hilo, permitiendo de esta manera crear un servidor concurrente.
- **Control de flujo:**  La función *handler_client_connection*, es la encargada del control de flujo de las peticiones entrantes al servidor. Dicha funcion se encarga de decodificar el Request para evaluar si es aceptado el método utilizado, y en caso de serlo, reedirecionarlo a la clase get.py

Igualmente se tiene la clase *get.py*, que es la encargada de procesar las solicitudes get entrantes, dicha función se encarga de:
- **Procesamiento y lectura de archivos:** Con base a la dirección entregada dentro del HTTP Request, el método *get_object* se encarga de reescribir el path para posteriormente intentar leer el archivo y abrirlo; seguido a esto, se realiza la codificación del encabezado de respuesta y se adiciona el archivo en formato binario.

Para la configuración de puertos y demás parámetros relevantes, se cuenta con el archivo `constans.py`, en el cual se encuentra especificado el puerto, valores del buffer Reader y otros parámetros constantes.

distribución de carpetas:
- **/:** Dentro del Directorio raíz se tienen los archivos Server.py (control de flujo principal) y constans.py (Contenedor de variables constantes utilizadas por el programa)
- **/ServerMet:** Dentro de este directorio se encuentra el archivo get.py (control de flujo de las peticiones get) y el directorio Recursos.
- **/ServerMet/Recursos/:** Dentro de este directorio se encuentran todos los archivos utilizados por nuestra página web


----

### 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerías, paquetes, etc, con sus números de versiones. ###

__librerías utilizadas:__
- **scokets:** Es utilizada para la creación de nuestro canal de comunicación
- **threading:** librería utilizada que permite la creación de hilos de procesamiento, que permite al servidor ser concurrente al crear un hilo por cada petición entrante

__IP:__ `54.145.202.4`

__Guia de uso:__ 

Posterior a la ejecución del archivo Server.py, lo único que necesita hacer el usuario es entrar a la ip `54.145.202.4`, donde acceder al index.html de la aplicación. Para navegar por los recursos disponibles dentro del servidor se debe realizar de la siguiente manera: __/Recursos/tipo_recurso/nombre_recurso.extension__

Tipos de recursos:
- **pdf:** `/Recursos/pdf/nombre_recurso.pdf`
- **documentos:** `/Recursos/documentos/nombre_recurso.html`
- **imagenes:** `/Recursos/imagenes/nombre_recurso.extension`
- **videos:** `/Recursos/videos/nombre_recurso.mp4`

----

### 5. Informacion relevante ###

__Nota importante:__
El código presentado toma como base el Proyecto #2 de telemática presentado en el semestre 2022-1, realizado por David Gomez Correa (mi persona) y Samuel Meneses Diaz (Compañero del curso), dicho código fue modificado para atender a los requerimientos de este laboratorio.

__Referencias:__

- https://github.com/smenesesd/TelematicaProyecto2

---

__versión README.md -> 1.0 (2022-agosto)__