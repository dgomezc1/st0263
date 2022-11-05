# ST0263 Tópicos Especiales en Telematica, 2022-2

__Estudiante:__

 David Gómez Correa, dgomezc10@eafit.edu.co  

__Profesor:__

 Edwin Nelson Montoya Munera, emontoya@eafit.edu.co

---

# Avance 2 - Amazon AWS
__Despliegue de aplicacion monolitica Moodle__

- [Laboratorio 5.1](#laboratorio-5---big-data)
  - [Descripción de la actividad](#1-breve-descripción-de-la-actividad)
  - [información general](#2-información-general-de-diseño-de-alto-nivel-arquitectura-patrones-mejores-prácticas-utilizadas)
  - [Descripcion ambiente desarrollo y tecnico](#3-descripción-del-ambiente-de-desarrollo-y-técnico-lenguaje-de-programación-librerias-paquetes-etc-con-sus-numeros-de-versiones)
  - [Evidencias de desarrollo](#4-evidencias-de-desarrollo)
  - [Referencias](#5-referencias)

--- 

  
## 1. Breve descripción de la actividad  
  
### 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)  

Se realiza la creacion y despliege de un servidor de moodle monolitico, el cual cumple con los siguientes requisitos:

- Certificado ssl de la direcion : __cloud.dgomezc10.tk__, para crear un canal de acceso a la aplicacion de manera segura
- Capa de loadbalancer, que se encarga de realizar el balanceo de las peticiones en las dos instancias de moodle existentes
- Se cuenta con dos capas de aplicacion, las cuales almacenan una instancia de moodle, la cual esta dockerizada. Estas instancias reciben las peticiones por el puerto 80 y las parsean al 8080. Igualmente, estas maquinas se encuentran conectadas a un servidor nfs y a una instancia de base de datos de mariadb
- Capa de contenidos, siendo esta un servidor de nfs, en el cual se realiza el alamacenamientod de los datos
- Capa de datos, se cuenta con una aplicacion de mariadb para el almacenamiento de  los datos

---  
  
## 2. Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas 
Se despliega una aplicacion moodle monolitica. Dicha aplicacion por capas, siendo estas un total de 4. En la primera capa se tiene un balanceador de cargas encargado de distribuir las cargas a las instancias de moodle, esta recibe peticiones por https y las parsea a http, esto incluyendo el algoritmo de roundrobin utilizado. Sumado a esto se cuenta con una capa de Aplicacion en la cual se encuentran dos instancias de moodle, esto con el fin de tener un sistema tolerante a fallos y tener un mejor manejo de cargas. Se tiene una capa de contenidos, con un nfs, el cual permite un mejor manejo de los contenidos y al estar compartido con ambas instancias de moodle permite tener ambos actualizados al tiempo. Por ultimo se tiene una capa de datos, con una base de datos de mariadb.

---  
  
## 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones 

__Ip de maquinas:__

- **Load balancer:** 34.237.100.216
- **Moodle_1:** 3.222.132.33
- **Moodle_2:** 3.224.154.71
- **Servidor NFS:** 18.208.2.129
- **Base de datos Mariadb:** 52.202.189.128

__Docker compose y archivos de maquinas:__

- **Load balancer:** 34.237.100.216
- **Moodle_1:** 3.222.132.33
- **Moodle_2:** 3.224.154.71
- **Servidor NFS:** 18.208.2.129
- **Base de datos Mariadb:** 52.202.189.128

__Directorios:__

- **/mnt/nfs_share:** Carpte dentro del servidor nfs donde se encuentran compartidos los archivos
- **/var/www/hmtl/moodle:** Directorio donde se encuentra todos los archivos relacionados con la aplicacion del moodle}
- **(moodle) /home/ubuntu/moodle:** Directorio donde es encuentra el docker compose del moodle
- **(loadbalancer) /home/ubuntu/moodle:** Directorio donde es encuentra el docker compose del load balancer, igualmente, el ngnix.conf y los certificados ssl
- **(mmariadb) /home/ubuntu/moodle:** Directorio donde es encuentra el docker compose de mariadb
 
  
## 4. Evidencias de desarrollo  
 
* Carga de archivos 

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%235/img/1_part_1/conf.png)  

* Comprobacion de moodle1

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%235/img/1_part_1/conf.png)  

* Comprobacion de moodle2 

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio%235/img/1_part_1/conf.png)  
   
  
---

## 5. Referencias
- https://github.com/st0263eafit/st0263-2022-2/tree/main/bigdata
- https://docs.aws.amazon.com/es_es/emr/latest/ManagementGuide/emr-what-is-emr.html
- https://docs.aws.amazon.com/es_es/emr/latest/ManagementGuide/emr-overview-arch.html#emr-arch-resource-management

---
#### versión README.md -> 1.0 (2022-octubre)