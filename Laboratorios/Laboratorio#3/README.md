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

- Se implementa un servidor monolitico con las siguientes funciones:
  
    - Recibir peticiones HTTPS por el puerto 443 

    - Permitir la comunicación de manera segura entre el cliente y el servidor. Esto gracias al uso de un certificado ssl con Let's Encrypt:  
        - El certificado cuenta  con una validez de 3 meses
        - El certificado esta habilitado para el subdominio www.dgomezc10.tk

    - Correr el servicio en el dominio dgomezc10.tk, permitiendo de esta manera el uso de nombre canonicos para el acceso a los recursos del servidor 

    - Soportar una pagina web realizada con wordpress usando docker

    - Soportar la creacion y el uso de una base de datos y el servicio de docker de manera monolitica. 

-  Se implementa un servidor DNS con la herramienta Google Cloud que cumple con las siguientes funciones:

    -  Almacenar los diferentes registros del servidor web, para de esta manera permitir el acceso al mismo 

    -  Almacenar  el token de la herramienta Let's Encrypt para permitir la comunicacion de manera segura entre cliente y servidor por medio de mensajes cifrados

---
## 2.  Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas. 
Como propuesta de solución, se implementó un servidor monolitico, el cual tiene el servicio de wordpress y la base de datos dentro del mismo nodo. Esto se logra gracias al servicio de docker, el cual permite descoplar la infraestructura interna y agilizan la creacion y el despliegue de las mismas. Para la comunicacion con el cliente, se utiliza una aquitectura de C/S, donde nuestro cliente accede desde un browser a los recursos del servidor. Esto se hace por medio de peticiones de HTTP, las cuales con el certificado ssl viajan de manera segura por el medio.  Nuestro servidor es monolitico y aqui se almacena los recursos y servicios utilizados.

---
## 3. Descripción del ambiente de desarrollo y técnico: lenguajes de programación, librerías, paquetes, etc. con sus números de versiones. 
El laboratorio fue realizado utilizando Wordpress como CMS, esto con el fin de emolar las funciones de un servidor web de una manera minimalista. Igualmente se hizo uso de la herramienta docker para desplegar el CMS de una manera rapida y sencilla, esto al igual que las dependencias necesarias para el funcionamiento del wordpress. Para finalizar, como servidor web se utilizo la herramienta Nginx y de la mano de Let's Encrypt se realizo un canal seguro para la comunicacion. 

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

__IP:__ 35.174.100.150

__Url:__ https://www.dgomezc10.tk

__Clave:__ Enviada por teams, correo y buzon de entrega al docente

__Guía para acceder a la maquina:__
1. Es necesario decargar el archivo `wordpressDocker1.ppk` enviado al docente. 

2. Revisar los permisos sobre el archivo:

    1. En el caso de windows solo debe tener los permisos para el usuario actual y los administradores. No puede tener permisos para usuarios logeados

    2. En el caso de linux ejecutar el siguiente comando:
        ```bash 
            sudo chmod 400 wordpressDocker1.ppk
        ```

3. Una vez tenga los permisos requeridos ejecutar el siguiente comando (`Es necesario correrlo igual, ya que el usuario asociado a esa clave no puede cambiar`):
```bash 
    ssh -i "wordpressDocker1.ppk" dgomezc10@35.193.44.44
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

## 5. Envidencias de desarrollo del laboratorio

 __Creacion de maquina en GCP:__

 ![imagen del sudo update](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/creacionmaquina.png)
---

 __Creacion de clave ssh:__

  ![Imagen de install de redis](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/Creaciondeclave.png)
---

  __Creacion de usario-clave a GCP:__

  ![Imagen del estado de redis](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/anadirclave.png)
---

  __Conexion ssh de manera local:__

  ![Imagen turn off server-redis](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/conexionssh.png)
---

  __Creacion de dominio:__

  ![Imagen de Verificacion de conexion](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/Creaciondominio.png)
---

  __Configuracion de DNS:__

  ![Imagen de Verificacion de conexion](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/dns.png)
---

  __Instalacion de lets encrypt:__

  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/img/requirepass.png)
---

  __Instalacion de nginx:__

  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/intnginx.png)
---

  __Configuracion de nginx:__

  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/confngix.png)
---

  __Creacion de TXT:__

  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/creacionTXT.png)
---

  __Creacion de carpeta ssl wordpress:__

  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/creacionConfig.png)
---

  __Creacion de Dhpragram:__

  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/creacionDhpta.png)
---

  __Instalacion de Docker:__

  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/dockerins.png)
---

  __Instalacion de docker compose:__

  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/dckercompose.png)
---

  __Creacion de wordpress:__

  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/creaciondewordpress.png)
---

  __Resvision pagina web:__

  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/revisionpagweb.png)
---

  __Revision de clave ssl:__

  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%233/img/CERTIFICA.png)
---

## 6. Referencias
https://github.com/st0263eafit/st0263-2022-2/tree/main/docker-nginx-wordpress-ssl-letsencrypt

---
#### versión README.md -> 1.0 (2022-agosto)