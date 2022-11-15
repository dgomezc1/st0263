# ST0263 Tópicos Especiales en Telematica, 2022-2

__Estudiante:__

 David Gómez Correa, dgomezc10@eafit.edu.co  
 Pascual Gomez Londoño, pgomezl@eafit.edu.co
 Sebastian Granda Gallego, sgrandag@eafit.edu.co

__Profesor:__

 Edwin Nelson Montoya Munera, emontoya@eafit.edu.co

---

# Proyecto #2 Aplicacion monolitica
__Despliegue de aplicacion monolitica Moodle en nube__

- [Anvance 2](#proyecto-2-aplicacion-monolitica)
  - [Descripción de la actividad](#1-breve-descripción-de-la-actividad)
  - [información general](#2-información-general-de-diseño-de-alto-nivel-arquitectura-patrones-mejores-prácticas-utilizadas)
  - [Descripcion ambiente desarrollo y tecnico](#3-descripción-del-ambiente-de-desarrollo-y-técnico-lenguaje-de-programación-librerias-paquetes-etc-con-sus-numeros-de-versiones)
  - [Evidencias de desarrollo](#4-evidencias-de-desarrollo)
  - [Referencias](#5-referencias)

--- 

  
## 1. Breve descripción de la actividad  
  
### 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)  

Se realiza la creacion y despliege de un servidor de moodle monolitico escalable, el cual cumple con los siguientes requisitos:

- Certificado ssl de la direcion : __www.dgomezc10.tk__, para crear un canal de acceso a la aplicacion de manera segura
- Capa de loadbalancer, que se encarga de realizar el balanceo de las peticiones a las instancias de moodle existentes en el grupo de autoscaling de AWS.
- Se cuenta con un grupo de autoscaling para la capa de aplicacion, las instancias almacenan una instancia de moodle, la cual esta dockerizada. Estas instancias reciben las peticiones por el puerto 80 y las parsean al 8080. Igualmente, estas maquinas se encuentran conectadas a un servidor s3 y a una instancia de base de datos de mariadb que se encuentra en un sistema RDS de AWS
- Capa de contenidos, siendo esta un servidor de Efs, en el cual se realiza el alamacenamientod de los datos, y al cual se conectan cada uno de las instancias del grupo de autoscaling para acceder a los recursos del mooodle que se encuentran en dicho servidor
- Capa de datos, se cuenta con una aplicacion de mariadb para el almacenamiento de  los datos, esta instancia de mariadb se despliega haciendo uso del servicio de RDS de AWS, con el fin de tener una base de datos central para cada una de las instancias del grupo de autoscaling.
- El despliege realizado cumple con una alta disponibilidad y unos tiempos de respuesta rapidos (1-2 segundos).

---  
  
## 2. Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas 

* Diseño

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Proyecto2/Final/img/proyecto2.png)  

Se despliega una aplicacion moodle monolitica. Dicha aplicacion por capas, siendo estas un total de 4. En la primera capa se tiene un balanceador de cargas encargado de distribuir las cargas a las instancias de moodle, esta recibe peticiones por https y las parsea a http, esto incluyendo el algoritmo de roundrobin utilizado. Dicho loadbalancer cuenta igualmente con un certificado ssl para el dominio de __www.dgomezc10.tk__, lo cual permite un canal de comunicacion segura entre los clientes y los servicios que se ofrecen. Igualmente, cabe resalta que se establecen unas reglas de firewall, las cuales unicamente permiten el acceso a los contenidos por el puerto 443 limitando y bloqueando puntos de acceso incesarios al sistema.

Sumado a esto se cuenta con una capa de Aplicacion en la cual se encuentra un grupo de autoscaling de AWS, el cual instancia una maquina de Ubuntu que contiene precargada la instalacion y configuracion de un servicio de Moodle. Se hace uso del grupo de autoscaling con el fin de tener un sistema tolerante a fallos y tener un mejor manejo de cargas. Dicha tolerancia a fallos se logra gracias a que si una instancia se detiene por algun motivo, inmediatamente otra se despliega, al igual que el grupo de autoscaling permite aumentar la cantidad de instancias con relacion a las necesidades del sistema. De esta manera se logra tener una alta disponibilidad del sistema al igual que unos tiempos de respuesta rapidos.

Se tiene una capa de contenidos, con el servicio de EFS, el cual permite un mejor manejo de los contenidos ya que cada una de las instancias del grupo autoscaling se encuentra configuradas para conectarse a este. Por ultimo se tiene una capa de datos, con una base de datos de mariadb, la cual se encuentra corriendo en un servicio de RDS y a la cual cada una de las instancias se conectan.

---  
  
## 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones 

__NOTA:__ Por favor avisar cuando desee acceder al sitio, se necesita abrir las maquinas primero

__Link:__ https://www.dgomezc10.tk/

__Ip de maquinas:__

- **Load balancer:** elb-mywebapp-1066930966.us-east-1.elb.amazonaws.com
- **Moodle_Instance:** Asignada por el servicio de AWS Autoscaling
- **Moodle_Instance_Image:** 52.207.225.105
- **Servidor EFS:** fs-0216c6cd7fc6dd547.efs.us-east-1.amazonaws.com
- **Base de datos Mariadb:** moodle-database.cvcer3p6jxvc.us-east-1.rds.amazonaws.com

__Docker compose moodle :__

```bash
version: '2'
services:
  moodle:
    image: docker.io/bitnami/moodle:latest
    restart: always
    ports:
      - 80:8080
      - 443:8443
    environment:
      - MOODLE_DATABASE_HOST=moodle-database.cvcer3p6jxvc.us-east-1.rds.amazonaws.com
      - MOODLE_DATABASE_USER=admin
      - MOODLE_DATABASE_PASSWORD=adminmoodle
      - MOODLE_DATABASE_NAME=bitnami_moodle
      - BITNAMI_DEBUG=true
      - MOODLE_DATABASE_PORT_NUMBER=3306
    volumes:
      - /mnt/moodle/moodle:/bitnami/moodle
      - /mnt/moodle/moodledata:/bitnami/moodledata
```

__Directorios:__

- **/mnt/moodle:** Directorio donde se encuentra todos los archivos relacionados con la aplicacion del moodle, esta carpeta esta asociada al servidor EFS
- **/home/ubuntu:** Directorio donde es encuentra el docker compose del moodle
 
  
## 4. Evidencias de desarrollo  
 
* Configuracion Autoscaling 

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Proyecto2/Final/img/autoscaling.png)  

---

* LoadBalancer

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Proyecto2/Final/img/lb.png)  

* Configuracion DNS

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Proyecto2/Final/img/DNS.png)  

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Proyecto2/Final/img/consultaDNS.png) 

---

* Direcciones IP 

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Proyecto2/Final/img/direcciones.png)  

---

* Prueba funcionamiento 

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Proyecto2/Final/img/Funciona.png)  

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Proyecto2/Final/img/Funciona2.png) 
  
---

## 5. Referencias
- https://github.com/st0263eafit/st0263-2022-2/tree/main/docker-nginx-wordpress-ssl-letsencrypt
---
#### versión README.md -> 1.0 (2022-octubre)