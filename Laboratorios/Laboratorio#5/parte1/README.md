# ST0263 Tópicos Especiales en Telematica, 2022-2

__Estudiante:__

 David Gómez Correa, dgomezc10@eafit.edu.co  

__Profesor:__

 Edwin Nelson Montoya Munera, emontoya@eafit.edu.co

---

# Laboratorio #5 - BIG DATA 
__Cluster AWS EMR__

- [Laboratorio 4](#laboratorio-4---wordpress)
  - [Descripción de la actividad](#1-descripción-de-la-actividad)
  - [información general](#2-información-general-de-diseño-de-alto-nivel-arquitectura-patrones-mejores-prácticas-utilizadas)
  - [Descripcion ambiente desarrollo y tecnico](#3-descripción-del-ambiente-de-desarrollo-y-técnico-lenguajes-de-programación-librerías-paquetes-etc-con-sus-números-de-versiones)
  - [Descripcion ambiente en produccion](#4-descripción-del-ambiente-de-ejecución-en-producción-lenguaje-de-programación-librerías-paquetes-etc-con-sus-números-de-versiones)
  - [Evidencias de desarrollo](#5-evidencias-de-desarrollo)
  - [Referencias](#6-referencias)

--- 

  
## 1. Breve descripción de la actividad  
  
### 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)  

Se realiza la creacion y despliege de un cluster AWS EMR en Amazon, al igual que otras apliaciones adicionales como Hue, JupyterHub y Hive. Todo esto con el fin de simular el funcionamiento de de plataformas de trabajo de BIG DATA. Además, con esta actividad se busca desarrollar habilidades en el manejo de dichas herramientas.

Se despliegan las siguientes aplicaciones:
- EMR de AWS
- Hadoop, siendo este el software que permite el procesamiento distribuido de grandes conjuntos de datos, en modo cluster
- JupyterHub es un software que se ejecuta en nube que brinda un entorno de ciencia de datos
- Hive es una infraestructura de alamacenamiento de datos construida sobre hadoop, para realizar analisis de datos
- Zeppelin es un notebook que permite la data ingestion, la exploracion de datos y la visualizacion de los mismos.
- Hue editor SQL en nube
- Spark es un framework de computacion en cluster, usada para el BIG DATA

---  
  
## 2. Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas 
Se despliega una arquitectura de servicios de Amazon AWS, EMR, que consta de varias capas. La primera de ellas es la capa de alamacenamiento, en la que se hace uso del S3 para el alamcenamiento distribuido de los datos. Una capa de administracion de recursos, que es la responsable de la administracion de los recursos del cluster. La capa de procesamiento de los datos, que se encarga de procesar y analizar los datos, en este caso se ahce uso de apache Spark. Por utlimo la capa de aplicaciones y programas en la que se hace uso de Hive, Jupyter, entre otras.

---  
  
## 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones 
  
**Plataforma de nube usada:** AWS (Amazon Web Services)  
**Sistema operativo:**  Amazon Linux 2 AMI  
**Servicio web utilizado:** EMR (Elastic MapReduce) - version: 6.3.1

__Aplicaciones y versiones utilizadas:__

- Hadoop 3.2.1
- JupyterHub 1.2.0
- Hive 3.1.2
- Zeppelin 0.9.0
- Spark 3.1.1
- Hue 4.9.0

  
 
  
## 4. Evidencias de desarrollo  

#### **Configuracion de EMR**  
* Seleccion de las aplicaciones del EMR 
![image text](/img/1_part_1/conf.png)  
  
* Configuracion de las instancias de master y slave 
![image text](/img/1_part_1/conf_2.png)  
    
* Configuracion del nombre del cluster 
![image text](/img/1_part_1/conf_3.png)  
  
* Configuracion de claves de acceso
![image text](/img/1_part_1/conf_4.png)  
  
* Resultado de la configuracion del EMR 
![image text](/img/1_part_1/resultado.png)  
  
* Acceso a la terminal de EMR   
![image text](/img/1_part_1/terminal.png)  
  
---

#### **Configuracion de puertos y aplicaciones**  
  
* Configuracion de los puertos para acceso de las aplicaciones  
![image text](/img/1_part_2/conf_acceso_port.png)  
  
* Configuracion del S3 para la persistencia de los archivos  
![image text](/img/1_part_2/Creacion_s3.png)  

---

#### **Prueba de aplicaciones**  

* Se cambia el nombre del cluster y se dejan las demas opciones por defecto  
![image text](/img/1_part_2/huev.png)  
  
* Se realiza la asignación de la clave .pem  
![image text](/img/1_part_2/huev_inside.png)  
  
* Se crea el cluster y luego se debe esperar a que este se ejecute  
![image text](/img/1_part_2/gui_spark.png)  
  
* Se verifica que el cluster se inicio de manera correcta  
![image text](/img/1_part_2/spark_context.png)  
  
* Se configuran los puertos para el master  
![image text](/img/1_part_2/confirmacion_zepelin.png)  
  
---

## 5. Referencias
- https://github.com/st0263eafit/st0263-2022-2/tree/main/bigdata
- https://docs.aws.amazon.com/es_es/emr/latest/ManagementGuide/emr-what-is-emr.html
- https://docs.aws.amazon.com/es_es/emr/latest/ManagementGuide/emr-overview-arch.html#emr-arch-resource-management

---
#### versión README.md -> 1.0 (2022-octubre)
  
