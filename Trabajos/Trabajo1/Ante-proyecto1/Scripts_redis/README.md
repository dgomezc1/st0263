# ST0263 Tópicos Especiales en Telemática, 2022-2 

__Estudiantes:__ 

David Gómez Correa, dgomezc10@eafit.edu.co   
Samuel Meneses Diaz, smenesesd@eafit.edu.co 

__Profesor:__ 

Edwin Nelson Montoya Munera, emontoya@eafit.edu.co 

---
  
# Ante Proyecto 1 – REDIS
__Implementación de operaciones CRUD en Python__

## 1. Descripción de la actividad  

### 1.1 Requerimientos funcionales y no funcionales  

- Se despliega la aplicación Redis, la cual es una base de datos no SQL. 
- Se crean 8 scripts de Python que implementan diferentes operaciones de tipo CRUD y cumplen con las siguientes funciones: 
    - Conexión a la base de datos de manera “localhost” 
    - **Script1.py:** Se encarga de realizar las operaciones más básicas dE CRUD las cuales son: 
        - GET 
        - SET 
        - MSET 
        - INCR 
    - **Sets.py:** Se encarga de implementar las operaciones CRUD sobre los sets, las cuales son la siguientes: 
        - SADD 
        - SINTER 
        - SDIFF 
        - SUNION 
        - SUNIONSTORE 
    - **Hash.py:** Se encarga de implementar las operaciones CRUD sobre la estructura de datos hash, que son las siguientes: 
        - MSET 
        - HVALS 
        - HKEYS 
        - HGET 
    - **Listas.py:** Realiza las operaciones CRUD sobre la estructura de datos de listas. Las operaciones son las siguientes:  
        - RPUSH 
        - LRANGE 
        - LREM 
        - LPOP 
        - RPOPLPUSH 
    - **Multi.py:** Se encarga de ejecutar las transacciones dentro de la base de datos Redis 
    - **Expiry.py:** Se encarga de ejecutar las operaciones CRUD que expiran, las cuales son las siguientes: 
        - SET 
        - EXPIER 
        - EXISTS 
        - SETEX 
        - TTL 
        - PERSIST 
    - **Union.py:** Se encarga de ejecutar las operaciones de tipo unión dentro de la base de datos Redis, las cuales son las siguientes: 
        - ZADD 
        - ZUNIONSTORE 
        - ZRANGEBYSCORE 
    - **Sorted.py:** Realiza las operaciones CRUD de tipo sorted que son las siguientes: 
        - ZADD 
        - ZINCRBY 

---
## 2. Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas. 

Como propuesta de solucion se implementa 8 módulos de scripts de Python, cada uno de ellos enfocados en las operaciones CRUD de cada una de las estructuras de datos que utiliza la base de datos Redis. Esto con el fin de dividir las operaciones CRUD en subgrupos de operaciones. 

 
---
## 3. Descripción del ambiente de desarrollo y técnico: lenguajes de programación, librerías, paquetes, etc. con sus números de versiones. 

El laboratorio fue realizado utilizando el lenguaje de programación Python, para su ejecución es necesario tener instalado Python por defecto. La principal librería utilizada además de las que tiene Python por defecto es la librería redis la cual es utilizada para la comunicación con el servicio de Redis. Para su instalación lo único que debe de hacer es en la terminal de su editor de código fuente con el cual va a ejecutar el código ingrese el siguiente comando: 

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
 
Dentro del paquete Script_redis se encuentra 8 scripts de Python los cuales cumplen con las siguientes funciones: 
- **Script1.py:** Se encarga de realizar las operaciones más básicas dE CRUD las cuales son: 
    - GET 
    - SET 
    - MSET 
    - INCR 
- **Sets.py:** Se encarga de implementar las operaciones CRUD sobre los sets, las cuales son la siguientes: 
    - SADD 
    - SINTER 
    - SDIFF 
    - SUNION 
    - SUNIONSTORE 
- **Hash.py:** Se encarga de implementar las operaciones CRUD sobre la estructura de datos hash, que son las siguientes: 
    - MSET 
    - HVALS 
    - HKEYS 
    - HGET 
- **Listas.py:** Realiza las operaciones CRUD sobre la estructura de datos de listas. Las operaciones son las siguientes:  
    - RPUSH 
    - LRANGE 
    - LREM 
    - LPOP 
    - RPOPLPUSH 
- **Multi.py:** Se encarga de ejecutar las transacciones dentro de la base de datos Redis 
- **Expiry.py:** Se encarga de ejecutar las operaciones CRUD que expiran, las cuales son las siguientes: 
    - SET 
    - EXPIER 
    - EXISTS 
    - SETEX 
    - TTL 
    - PERSIST 
- **Union.py:** Se encarga de ejecutar las operaciones de tipo unión dentro de la base de datos Redis, las cuales son las siguientes: 
    - ZADD 
    - ZUNIONSTORE 
    - ZRANGEBYSCORE 
- **Sorted.py:** Realiza las operaciones CRUD de tipo sorted que son las siguientes: 
    - ZADD 
    - ZINCRBY 


Directorios: 

- **/Script_redis/script1.py**
- **/Script_redis/expiry.py** 
- **/Script_redis/hash.py** 
- **/Script_redis/listas.py** 
- **/Script_redis/multi.py** 
- **/Script_redis/sets.py** 
- **/Script_redis/sorted.py** 
- **/Script_redis/union.py** 

---
## 4. Descripción del ambiente de ejecución (en producción) lenguaje de programación, librerías, paquetes, etc. Con sus números de versiones. 

__Librerías utilizadas:__

redis: Librería utilizada para la comunicación con el servicio Redis 

__IP:__ **18.215.164.6** 

__Guia de uso:__

Para iniciar, es necesario inicializar máquina de AWS. Para iniciar correctamente el servicio Redis es necesario ejecutar el siguiente comando: 

```bash 
Redis-server 
```

Una vez iniciado el servidor, ingrensamos al directorio /Script_redis/ y ejecutamos cada uno de los scripts de la siguiente manera: 

`Sudo python3 script1.py `

`Sudo python3 expiry.py `

`Sudo python3 hash.py` 

`Sudo python3 listas.py `

`Sudo python3 multi.py` 

`Sudo python3 sets.py` 

`Sudo python3 sorted.py` 

`Sudo python3 union.py `


---
## 5.  Evidencia de ejecución. 

__Script1.py__

<img src="https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/Scripts_redis/img/script1.png" />

__Resultado:__ 

<img src="/img/resultados_ script1.png" />


__Lista.py:__ 

<img src="/img/listas.png" />

__Resultado:__ 

<img src="/img/resultados_listas.png" /> 


__Sorted.py:__ 

<img src="/img/sort.png" />

__Resultados:__ 

<img src="/img/resultados_sort.png" />


__Sets.py:__ 

<img src="/img/sets.png" /> 

__Resultados:__ 

<img src="/img/resultados_Sets.png" />

__Multi.py:__ 

<img src="/img/multi.png" /> 

__Resultados:__ 

<img src="/img/resultados_multi.png" />

__Hash.py:__ 

<img src="/img/hash.png" /> 

__Resultados:__ 

<img src="/img/resultados_hash.png" />

---
## Referencias: 

https://learning-oreilly-com.ezproxy.eafit.edu.co/library/view/seven-databases-in/9781680505962/f_0055.xhtml#d24e41269 

https://cosasdedevs.com/posts/como-utilizar-redis-con-python/ 

---
#### versión README.md -> 1.0 (2022-septiembre) 