# ST0263 Tópicos Especiales en Telematica, 2022-2

__Estudiante:__

 David Gómez Correa, dgomezc10@eafit.edu.co  

__Profesor:__

 Edwin Nelson Montoya Munera, emontoya@eafit.edu.co

---

# Laboratorio #5.2 - BIG DATA 
__Cluster AWS EMR, carga de archivos__

- [Laboratorio 5.2](#laboratorio-5---big-data)
  - [Descripción de la actividad](#1-breve-descripción-de-la-actividad)
  - [información general](#2-información-general-de-diseño-de-alto-nivel-arquitectura-patrones-mejores-prácticas-utilizadas)
  - [Descripcion ambiente desarrollo y tecnico](#3-descripción-del-ambiente-de-desarrollo-y-técnico-lenguaje-de-programación-librerias-paquetes-etc-con-sus-numeros-de-versiones)
  - [Evidencias de desarrollo](#4-evidencias-de-desarrollo)
  - [Referencias](#5-referencias)

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

Adicional a esto, se realiza una conexion via SSH y via interfaz grafica para la comunicacion con el cluste. Con dicha conexion se realizan distintas tareas como lectura, copia y borrado de unos conjuntos de datos.

---  
  
## 2. Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas 
Se despliega una arquitectura de servicios de Amazon AWS, EMR, que consta de varias capas. La primera de ellas es la capa de alamacenamiento, en la que se hace uso del S3 para el alamcenamiento distribuido de los datos. Una capa de administracion de recursos, que es la responsable de la administracion de los recursos del cluster. La capa de procesamiento de los datos, que se encarga de procesar y analizar los datos, en este caso se ahce uso de apache Spark. Por utlimo la capa de aplicaciones y programas en la que se hace uso de Hive, Jupyter, entre otras.

Se establece un canal de conexion via ssh para la comunicacion con el EMR y para permitir la carga de archivos.

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

__Directorios utilizados:__

- **/user/hadoop/dataset:** En este directorio se puede encontrar todos los archivos cargados al EMR por medio de dhfs hfs
- **/datasets/:** En este directorio se puede encontrar todos los archivos cargados al EMR por medio de SSH
  
## 4. Evidencias de desarrollo  

#### **Carga de archvios por ssh**  
* Carga de archivos por medio de ssh 

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio_5/img/2_part_hdfs/carga_scp.png)  
  
* Verificacion de carga de archivos 

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio_5/img/2_part_hdfs/Captura%20de%20pantalla%202022-10-29%20105305.png)  

* Verificacion de dataset 

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio_5/img/2_part_hdfs/dataset_local.png) 
    

#### **Ejecucion de comandos**

* Cat

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio_5/img/2_part_hdfs/cat.png)  
  
* Chgrp

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio_5/img/2_part_hdfs/chgrp.png)  
  
* chmod

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio_5/img/2_part_hdfs/chmod.png)  
  
* put

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio_5/img/2_part_hdfs/copiado_manual.png)  
  
---

#### **Configuracion de puertos y aplicaciones**  
  
* Cp 

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio_5/img/2_part_hdfs/cp3.png)  
  
* Du

![image text](https://github.com/dgomezc1/st0263/blob/main/Laboratorios/Laboratorio_5/img/2_part_hdfs/du.png)  
 

* ls

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio_5/img/2_part_hdfs/listado_zip.png)  
  
* mv 

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio_5/img/2_part_hdfs/mv.png)  
  
* Ls

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio_5/img/2_part_hdfs/recursiva.png)  
  
* rm

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio_5/img/2_part_hdfs/rm.png)  
    

---

#### **Carga archivos s3** 
  
* Carga archivos s3 

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio_5/img/2_part_hdfs/carga_carpeta_s3.png)  

* Guardados S3 

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio_5/img/2_part_hdfs/guardados_s3.png)  

* Visualiazacion

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio_5/img/2_part_hdfs/contenido.png)  

* Creacion de directorio 

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio_5/img/2_part_hdfs/s3_Directorio.png)  


* De s3 a hdfs  

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio_5/img/2_part_hdfs/s3_a_hdfs.png)  

* Crecion de dataset 

![image text](https://raw.githubusercontent.com/dgomezc1/st0263/main/Laboratorios/Laboratorio_5/img/2_part_hdfs/Creacion_datasets.png)

---

## 5. Referencias
- https://github.com/st0263eafit/st0263-2022-2/tree/main/bigdata
- https://docs.aws.amazon.com/es_es/emr/latest/ManagementGuide/emr-what-is-emr.html
- https://docs.aws.amazon.com/es_es/emr/latest/ManagementGuide/emr-overview-arch.html#emr-arch-resource-management

---
#### versión README.md -> 1.0 (2022-octubre)
  
