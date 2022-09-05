# ST0263 Tópicos Especiales en Telemática, 2022-2 

__Estudiantes:__ 

David Gómez Correa, dgomezc10@eafit.edu.co   
Samuel Meneses Diaz, smenesesd@eafit.edu.co 

__Profesor:__ 

Edwin Nelson Montoya Munera, emontoya@eafit.edu.co 

---
  
# Ante Proyecto 1 – REDIS
__Implementación de Redis como cluster__

-[Ante-Proyecto 1](#ante-proyecto-1---REDIS)
 - [Descripción de la actividad](#1-descripción-de-la-actividad)
 - [información general](#2-información-general-de-diseño-de-alto-nivel-arquitectura-patrones-mejores-prácticas-utilizadas)
 - [Descripcion ambiente desarrollo y tecnico](#3-descripción-del-ambiente-de-desarrollo-y-técnico-lenguajes-de-programación-librerías-paquetes-etc-con-sus-números-de-versiones)
 - [Descripcion ambiente en produccion](#4-descripción-del-ambiente-de-ejecución-en-producción-lenguaje-de-programación-librerías-paquetes-etc-con-sus-números-de-versiones)
 - [Evidencia](#5-evidencia-de-ejecucion)

## 1. Descripción de la actividad  

### 1.1 Requerimientos funcionales y no funcionales  

Se implementa el servicio de base de datos de Redis en modo Cluster, el cual nos permite escalar el sistema, tener una mayor potencia de cómputo y una alta disponibilidad ante posibles fallos en uno de los nodos. Dicha implementación cumple con los siguientes requisitos:
- Se implementa el servicio de Cluster en un único nodo con múltiples puertos
- Se crea un sistema distribuido, que permite el acceso al servicio por múltiples puertos
- Se implementa un sistema con alta disponibilidad, esto ya que cada nodo tiene un Slave que le permite la replicación asincrónica de los datos
- Se implementa un servicio con hash para la distribución de los datos

---
## 2. Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas. 

Como propuesta de solucion se implementa 6 nodos de servicios de Redis dentro de una única máquina de AWS. En total son 3 nodos master, cada uno de ellos cuenta con un slave como modo de respaldo, esto con el fin de tener una alta disponibilidad. A su vez, se crea un sistema de distributed hash table, esto para hacer el direccionamiento de las transacciones a la partición correspondiente. Por último, se crean 3 slots en los cuales se almacenarán cada uno de los recursos.
 
---
## 3. Descripción del ambiente de desarrollo y técnico: lenguajes de programación, librerías, paquetes, etc. con sus números de versiones. 

Para utilizar el servicio de base de datos de Redis en modo cluster se realizó la respectiva configuración siguiendo los pasos que suministra la documentación de dicho servicio como se muestra a continuación.

__Creacion del archivo de configuracion redis.conf__

Para este apartado se crea el archivo de configuración de cada uno de los nodos que se desean utilizar dentro del cluster. En este archivo se especifica que va a funcionar como un cluster, se define el archivo de configuración de los nodos y el timeout.

![Imagen de conf](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/Cluster/img/creacionconf.png)

![Imagen de conf](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/Cluster/img/archivoconf.png)

![Imagen de conf](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/Cluster/img/replicacion.png)

---
__Corremos los servicios con le archivo de configuracion__

Una vez terminamos de configurar cada uno de los nodos, se procede a correr los servicios con la siguiente linea de codigo. 

```bash 
redis-server ./redis.conf
```

![Imagen de conf](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/Cluster/img/correrservicios.png)

De esta manera se inicializara cada uno de los nodos con su respectivo archivo de configuraición. Igualmente en la parte de abajo de puede observar que en background estan corriendo cada uno de los servicios, eso corriendo el siguiente comando:

```bash 
ps
```

---
__Creacion del cluster__

Para conectar cada uno de los nodos en el modo cluster es necesario correr le siguiente codigo. 

![Imagen de conf](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/Cluster/img/slots.png)

Una vez que se realiza la operacion se pueden observar aspectos relevantes como lo son:
- **Configuracion de masters:** Para este caso se puede ver como se crean 3 masters, el puerto 7000, 7001 y 7002
- **Configuracion de slaves:** Para este caso se puede ver como se crean 3 slaves, los cuales son los nodos de los puertos 7003, 7004, 70005
- **Configuracion de slots:** Se puede observar como se generan 3 slots para los tres masters que se tiene.

---
## 4. Descripción del ambiente de ejecución (en producción) lenguaje de programación, librerías, paquetes, etc. Con sus números de versiones. 

Para la correcta ejecucion del cluester, es necesario inicializar la maquina de AWS **AvPro-redisCluster**

__IP:__ **18.211.121.120** 

__Guia de uso:__


Una vez iniciado el servidor, ingrensamos a cada uno de los nodos con el siguiente comando: 

```bash 
redis-cli -p 7000 -c
```

```bash 
redis-cli -p 7001 -c
```

```bash 
redis-cli -p 7002 -c
```

---
## 5.  Evidencia de ejecución. 

__Pruebas PING__

![Imagen de conf](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/Cluster/img/ping.png)
---
__Cluster slots__

![Imagen de conf](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/Cluster/img/clusterinfo.png)
---
__Operacion basicas__

![Imagen de conf](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/Cluster/img/slotsinfo.png)
---
__Operacion MSET__

![Imagen de conf](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/Cluster/img/mset.png)
---
__Operacion MULTI__

![Imagen de conf](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/Cluster/img/multi.png)
---
__Operaciones de listas__

![Imagen de conf](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/Cluster/img/l1.png)

![Imagen de conf](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/Cluster/img/l2.png)
---

## Referencias: 

https://redis.io/docs/reference/cluster-spec/

https://www.youtube.com/watch?v=N8BkmdZzxDg
#### versión README.md -> 1.0 (2022-septiembre) 
