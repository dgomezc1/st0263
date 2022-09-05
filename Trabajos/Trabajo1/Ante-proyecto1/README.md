
# ST0263 Tópicos Especiales en Telemática, 2022-2
#
# Estudiantes:
David Gómez Correa, dgomezc10@eafit.edu.co  
Samuel Meneses Diaz, smenesesd@eafit.edu.co
#
# Profesor:
Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#
 # Proyecto 1 – 1. Activación de la infraestructura TI y 2. Uso de la base de datos mediante operaciones en la versión single-node:
   
# 1. Descripción de la actividad 

## 1.1 Requerimientos funcionales y no funcionales 
-	Se creo una instancia en AWS para instalar redis de manera local (sinlge-node)
-	Se estableció el grupo de seguridad, específicamente en las reglas de entrada, una regla de TCP por el puerto 22 y otra también TCP pero por el puerto 6379 
-	Se instalo localmente el servicio de redis 
-	Se hizo una verificación de conexión escribiendo Redis-CLI y copiando un PING para dar como respuesta un PONG
-	Se le aumento la seguridad a redis poniéndole una contraseña usando un requirepass.
-	Al momento de crear o manipular una key o lo que este adentro del redis nos pedirá una AUTH con la contraseña antes puesta por el usuario 
-	Para la parte de persistencia se escogió el append only file (AOF) ya que no hay problemas de corrupción y es mucho más duradero. 
-	Se crearon unas key value con el comando set para ver que redis las está almacenando correctamente
-	Después de haber creado las key value se mira a ver si se puede acceder a la dicha clave usando el comando get y el nombre dado a la key

## 1.2 Requerimientos funcionales y no funcionales que no se cumplieron
-	En este caso ya que era seguir los pasos del libro de Seven databases in seven weeks, no hubo requerimientos funcionales o no funcionales que no se cumplieron

# 2. Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
Como propuesta de implementación en esta primera parte, se instaló y se implementó una base de datos durable, llamado redis. Esto con el fin de simular como se implementa un cluster multi-node o de manera local un single-node. Y en la segunda parte se amplió el conocimiento del CRUD y los datatypes gracias al libro recomendado llamado Seven databases in seven weeks, usando comandos en el redis como: SET, GET, MSET, MGET, INCR entre otras que fueron de gran ayuda. 

# 3. Descripción del ambiente de desarrollo y técnico: lenguajes de programación, librerías, paquetes, etc. con sus números de versiones.
Este punto 1 y 2 del avance del proyecto se hizo todo en una instancia Ubuntu de AWS, en si no se necesita nada para ejecutar ya que fue un ambiente de pruebas y primer contacto con lo que es Redis. La versión usada e instalada de redis server fue la V = 6.0.16. Y la versión de redis – CLI fue la 6.0.16. Para su instalación lo único que debe de hacer es al momento de ingresar a la instancia creada en AWS, ingresar los siguientes comandos en la terminal:
```bash
Sudo apt-get update
Sudo apt-get install redis
```

# 4. Descripción del ambiente de ejecución (en producción) lenguaje de programación, librerías, paquetes, etc. Con sus números de versiones.
En este caso del punto 1 y 2 no fue necesario usar directorios ni librerías ya que al momento de instalar redis de la manera anteriormente dicha, es todo lo que se necesita para llevar a cabo estos puntos. Por parte de la IP, no se necesitó ya que todo lo estaba corriendo en la IP local de la máquina. 
Guia de uso: 
Mas que una guía de uso, esta parte será de cómo se puede empezar a usar redis de una forma resumida.
Para iniciar, es necesario inicializar la máquina de AWS. Ya hablado de la instalación de redis en dicha máquina, podemos empezar conectándonos al redis usando el comando:
```bash
Redis-cli
```
Después de conectarse, podemos hacer un PING para verificar conexión y si la conexión es establecida recibiremos un PONG por parte de redis. En base a lo que dice el libro después de hacer esta conexión podemos empezar a establecer key values en nuestro servidor de redis, usando el comando 
```bash
SET
```
Esto seguido del nombre que le queramos dar y junto a una URL, como este tipo de comandos hay varios como lo son GET para devolver el valor de esta key, para reducir tráfico podemos usar MSET para poner múltiples valores y MGET para retornar varios valores. 

# 5. Evidencia.
 
 __SudoUpdate:__
 ![imagen del sudo update](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/img/update.png)

 __InstallRedis:__
  ![Imagen de install de redis](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/img/install_redis.png)

  __EstadoRedis:__
  ![Imagen del estado de redis](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/img/status.png)

  __TurnOff:__
  ![Imagen turn off server-redis](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/img/apague.png)

  __conexion:__
  ![Imagen de Verificacion de conexion](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/img/cli.png)

  __noContraseña:__
  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/img/requirepass.png)

  __siContraseña:__
  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/img/requirepass2.png)

  __AUTH:__
  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/img/noauth.png)

  __AUTHOK:__
  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/img/authok.png)

  __Persistencia:__
  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/img/config.png)

  __help:__
  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/img/help.png)

  __KeyValues:__
  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/img/setget.png)
  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/img/mset.png)
  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/img/incr.png)
  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/img/multi.png)
  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/img/mget.png)
  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/img/mgetuser.png)
  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/img/hmset.png)
  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/img/hgetpassword.png)
  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/img/rpush.png)
  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/img/lrem.png)

  __BrpopLpush:__
  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/img/brpop.png)

  __ValuesNorepetidos:__
  ![Imagen de contraseña no establecida](https://raw.githubusercontent.com/dgomezc1/st0263/main/Trabajos/Trabajo1/Ante-proyecto1/img/sadd.png)








 

  
Cliente servidor, BRPOP para el cliente y LPUSH para enviar
 
Set de valores no repetidos
 
SINTER: Intercepto de dos sets
 
Diferencia lo que esta en news y no en tech
 
Union y guardar unión 
 
 
 
 

# Referencias:
Perkins, L. (208d. C.). Seven Databases in Seven Weeks, 2nd Edition (2.a ed.). Pragmatic Bookshelf.## sitio1-url 
Install Redis on Windows. (2022). Redis. https://redis.io/docs/getting-started/installation/install-redis-on-windows/

Redis persistence. (2022). Redis. https://redis.io/docs/manual/persistence/

#### versión README.md -> 1.0 (2022- Septiembre)