# ST0263 Tópicos Especiales en Telematica, 2022-2

__Estudiante:__

 David Gómez Correa, dgomezc10@eafit.edu.co  

__Profesor:__

 Edwin Nelson Montoya Munera, emontoya@eafit.edu.co

---

# Laboratorio #3 - Wordpress 
__Despliegue de wordpress en docker usando GCP__

- [Laboratorio 3](#laboratorio-3---wordpress)
  - [Descripción de la actividad](#1-descripción-de-la-actividad)
  - [información general](#2-información-general-de-diseño-de-alto-nivel-arquitectura-patrones-mejores-prácticas-utilizadas)
  - [Descripcion ambiente desarrollo y tecnico](#3-descripción-del-ambiente-de-desarrollo-y-técnico-lenguajes-de-programación-librerías-paquetes-etc-con-sus-números-de-versiones)
  - [Descripcion ambiente en produccion](#4-descripción-del-ambiente-de-ejecución-en-producción-lenguaje-de-programación-librerías-paquetes-etc-con-sus-números-de-versiones)
  - [Evidencias de desarrollo](#5-envidencias-de-desarrollo-del-laboratorio)
  - [Referencias](#6-referencias)

--- 

## 1. Descripción de la actividad
### 1.1 Requerimientos funcionales y no funcionales

- Se implementa el depliege de una aplicacion monolitica con balanceo y datos distribuidos que cumple con los siguientes requisitos:
  
    - Despliegue de balanceador de cargas basado en nginx, utilizando la herramienta de docker para su despliege. Dicho balanceador de carga, redirecciona el trafico web https a multiples instancias

    - Despliege de dos instancias de procesamiento en las virtual machine de GCP, utilizando docker para su despliege

    - Una base de datos distribuida, concretamente una instancia de mysql sobre docker para la persistencia de los datos

    - Despliege de una instancia de NFS, para tener archivos distribuidos dentro de nuestra aplicacion, con el fin de ser compartidos por las instancias de wordpress

    - Permitir la comunicación de manera segura entre el cliente y el servidor. Esto gracias al uso de un certificado ssl con Let's Encrypt:  
        - El certificado cuenta  con una validez de 3 meses
        - El certificado esta habilitado para el subdominio lab4.dgomezc10.tk

    - Correr el servicio en el dominio dgomezc10.tk, permitiendo de esta manera el uso de nombre canonicos para el acceso a los recursos del servidor 

-  Se implementa un servidor DNS con la herramienta Google Cloud que cumple con las siguientes funciones:

    -  Almacenar los diferentes registros del servidor web, para de esta manera permitir el acceso al mismo 

    -  Almacenar  el token de la herramienta Let's Encrypt para permitir la comunicacion de manera segura entre cliente y servidor por medio de mensajes cifrados

---
## 2.  Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas. 

Como propuesta de solucion se realiza la implementacion de  un servidor monolitico de multiples capas. Cada capa representada por un nodo separado, con el fin de separar los componentes de la aplicacion. Gracias al servicio de docker se depliega en dos nodos de maquinas virtuales una imagen de wordpress. Dichas maquinas a su vez, apuntan a una base de datos distribuida, haciendo uso de docker y mysql, para la persistencia de los datos. Igualmente se cuenta con un servidor NFS con el fin de que ambas instancias compartan la misma referencia de los datos utilizados por wordpress. Para finalizar, se hace despliegue de un balanceador de cargas haciendo uso de las tecnologias de nginx.

---
## 3. Descripción del ambiente de desarrollo y técnico: lenguajes de programación, librerías, paquetes, etc. con sus números de versiones. 
El laboratorio fue realizado utilizando Wordpress como CMS, esto con el fin de emolar las funciones de un servidor web de una manera minimalista. Igualmente se hizo uso de la herramienta docker para desplegar el CMS de una manera rapida y sencilla, esto al igual que las dependencias necesarias para el funcionamiento del wordpress. Para la base de datos distribuida se hace uso de la herramienta docker para su despliegue. Por otro lado, se implementa un servidor NFS haciendo uso del software nfs-kernel-server. Para finalizar se despliega un servidor de nginx con la funcion de load balancer.

__Versiones de servicios utilizados:__
- **Nginx:** nginx/1.18.0 (Ubuntu)
- **docker:** 20.10.12-0ubuntu2~20.04.1
- **letsencrypt:** certbot 0.40.0
- **docer-compose:**  version 1.25.0
- **wordpress:** version 6.0.2


__Directorios:__
- **/etc/nginx/:** Directorio donde se encuentran los archivos de configuracion de nginx
- **/var/www/letsencrypt:** Directorio donde se encuentra los servicios de Let's encrypt
- **/home/dgomezc10/wordpress:** Directorio donde se encuentran los archivos de configuracion del wordpress
- **/var/www/html/:** Directorio donde se encuentrar los contenidos de wordpress

__Comandos para iniciar wordpress en docker:__
1. Detener el servicio de nginx en caso de que este corriendo:

```bash 
sudo systemctl disable nginx
sudo systemctl stop nginx 
```

2. Ir al directorio donde se encuentra los archivos de configuracion de wordpress

```bash 
cd /home/gcp-username/wordpress
```

3. Ejecutar el siguiente comando dentro del directorio (es necesario utilizar sudo)

```bash 
docker-compose up --build -d
```

---
## 4. Descripción del ambiente de ejecución (en producción) lenguaje de programación, librerías, paquetes, etc. Con sus números de versiones. 


__Sistema de VM utilizado:__ Google Cloud

__IP Wordpress 1:__ 35.192.220.120

__IP Wordpress 2:__ 34.123.163.221

__IP Servidor NFS:__ 34.134.57.191

__IP Load Balancer:__ 34.122.227.112

__IP Base de datos:__ 34.135.36.71

__Url:__ https://lab4.dgomezc10.tk

__Clave:__ Enviada por teams, correo y buzon de entrega al docente

__Guía para acceder a la maquina:__
1. Es necesario decargar el archivo `id_rsa` enviado al docente. 

2. Revisar los permisos sobre el archivo:

    1. En el caso de windows solo debe tener los permisos para el usuario actual y los administradores. No puede tener permisos para usuarios logeados

    2. En el caso de linux ejecutar el siguiente comando:
        ```bash 
            sudo chmod 400 id_rsa
        ```

3. Una vez tenga los permisos requeridos ejecutar el siguiente comando (`Es necesario correrlo igual, ya que el usuario asociado a esa clave no puede cambiar`):
```bash 
    ssh -i "id_rsa" dgomezc10@35.192.220.120
```

4. Ahora puede acceder a la consola de manera local

__Comandos para iniciar wordpress en docker:__
1. Detener el servicio de nginx en caso de que este corriendo:

```bash 
sudo systemctl disable nginx
sudo systemctl stop nginx 
```

2. Ir al directorio donde se encuentra los archivos de configuracion de wordpress

```bash 
cd /home/gcp-username/wordpress
```

3. Ejecutar el siguiente comando dentro del directorio (es necesario utilizar sudo)

```bash 
docker-compose up --build -d
```

---

__Archivos de configuracion docker compose Wordpress:__

```bash 
version: '3.7'
services:
  wordpress:
    container_name: wordpress
    image: wordpress:latest
    restart: always
    environment:
      WORDPRESS_DB_HOST: 10.128.0.4
      WORDPRESS_DB_USER: wdp
      WORDPRESS_DB_PASSWORD: lab4
      WORDPRESS_DB_NAME: dbwp
    volumes:
      - /var/www/html:/var/www/html
    ports:
      - 80:80
volumes:
  wordpress:
```

---

__Archivos de configuracion docker compose Mysql:__

```bash 
version: "3.7"
services:
  mysql:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: mysql
    restart: always
    ports:
      - 3306:3306
    environment:
      MYSQL_ROOT_PASSWORD: "lab4Telematica"
      MYSQL_DATABASE: "wordpress"
    volumes:
      - ./schemas:/var/lib/mysql:rw
volumes:
  schemas: {}
```

---

__Archivos de configuracion docker compose Load balancer:__

```bash 
version: "3.7"
services:
  nginx:
    container_name: nginx
    image: nginx
    restart: laways
    volumes:
    - ./nginx.conf:/etc/nginx/nginx.conf:ro
    - ./ssl:/etc/nginx/ssl
    - ./ssl.conf:/etc/nginx/ssl.conf
    ports:
    - 80:80
    - 443:443
```

---
## 5. Evidencias de desarrollo

 __Instalacion de nfs-kernel-server:__

 ![imagen del sudo update](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/creacionmaquina.png)
---

 __Archivo de configuracion NFS:__

 ![imagen del sudo update](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/creacionmaquina.png)
---

 __Configuracion de firewall nfs-server:__

 ![imagen del sudo update](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/creacionmaquina.png)
---

 __Configuracion de nfs-client:__

 ![imagen del sudo update](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/creacionmaquina.png)

  ![imagen del sudo update](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/creacionmaquina.png)
---

 __Depliegue de docker compose wordpress:__

 ![imagen del sudo update](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/creacionmaquina.png)
---

 __Depliegue mysql:__

 ![imagen del sudo update](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/creacionmaquina.png)
 ![imagen del sudo update](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/creacionmaquina.png)
 ![imagen del sudo update](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/creacionmaquina.png)
---

 __Resultado Final:__

 ![imagen del sudo update](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/creacionmaquina.png)
---
