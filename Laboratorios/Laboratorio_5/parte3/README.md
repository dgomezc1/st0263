# ST0263 Tópicos Especiales en Telematica, 2022-2

__Estudiante:__

 David Gómez Correa, dgomezc10@eafit.edu.co  

__Profesor:__

 Edwin Nelson Montoya Munera, emontoya@eafit.edu.co

---

# Laboratorio #5 - BIG DATA 
__Analisis de datos con MAPREDUCE__

- [Laboratorio 5.1](#laboratorio-5---big-data)
  - [Descripción de la actividad](#1-breve-descripción-de-la-actividad)
  - [información general](#2-información-general-de-diseño-de-alto-nivel-arquitectura-patrones-mejores-prácticas-utilizadas)
  - [Descripcion ambiente desarrollo y tecnico](#3-descripción-del-ambiente-de-desarrollo-y-técnico-lenguaje-de-programación-librerias-paquetes-etc-con-sus-numeros-de-versiones)
  - [Evidencias de desarrollo](#4-evidencias-de-desarrollo)
  - [Referencias](#5-referencias)

--- 

  
## 1. Breve descripción de la actividad  
  
### 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)  

Se soluciona diferentes hipotesis haciendo uso de MapReduce y de un conjunto de datos de diferentes bases de datos, como lo son acerca de peliculas, registro de trabajadores y de acciones. Gracias a la libreria de mrjob se logra hacer un analisis de datos tipo MapReduce

---  
  
## 2. Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas 
Se realizan scrips en el leguaje de programacion de Python y haciendo uso de la libreria de mrjob. Cada script es una solucion para cada una de las hipotesis.

---  
  
## 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones 
  
__Librerias:__
- mrjob

__Link de scripts:__

- **1.1 :** [Salario Sector](https://github.com/dgomezc1/st0263/blob/main/Laboratorios/Laboratorio_5/parte3/p1/sal_sector.py)
- **1.2 :** [Salario Empleado](https://github.com/dgomezc1/st0263/blob/main/Laboratorios/Laboratorio_5/parte3/p1/sal_empleado.py)
- **1.3 :** [Numero sectores](https://github.com/dgomezc1/st0263/blob/main/Laboratorios/Laboratorio_5/parte3/p1/numero_se.py)
- **2.1 :** [Dia-menor-valor](https://github.com/dgomezc1/st0263/blob/main/Laboratorios/Laboratorio_5/parte3/p2/dia_accion.py)
- **2.2 :** [Acciones estables](https://github.com/dgomezc1/st0263/blob/main/Laboratorios/Laboratorio_5/parte3/p2/estables_accion.py)
- **3.1 :** [Vistas por usuario](https://github.com/dgomezc1/st0263/blob/main/Laboratorios/Laboratorio_5/parte3/p3/usuarios_peli.py)
- **3.2 :** [Mas peliculas](https://github.com/dgomezc1/st0263/blob/main/Laboratorios/Laboratorio_5/parte3/p3/fecha_mayor.py)
- **3.3 :** [Menos peliculas](https://github.com/dgomezc1/st0263/blob/main/Laboratorios/Laboratorio_5/parte3/p3/fecha_menor.py)
- **3.4 :** [Misma pelicula](https://github.com/dgomezc1/st0263/blob/main/Laboratorios/Laboratorio_5/parte3/p3/pelis_per_user.py)
- **3.5 :** [Peor evaluacion](https://github.com/dgomezc1/st0263/blob/main/Laboratorios/Laboratorio_5/parte3/p3/usuarios_peor.py)
- **3.6 :** [Mejor evaluacion](https://github.com/dgomezc1/st0263/blob/main/Laboratorios/Laboratorio_5/parte3/p3/usuarios_menor.py)
- **3.7 :** [Mejor y Peor](https://github.com/dgomezc1/st0263/blob/main/Laboratorios/Laboratorio_5/parte3/p3/mejor_peor.py)


---  

## 5. Referencias
- https://github.com/st0263eafit/st0263-2022-2/tree/main/bigdata
- https://docs.aws.amazon.com/es_es/emr/latest/ManagementGuide/emr-what-is-emr.html
- https://docs.aws.amazon.com/es_es/emr/latest/ManagementGuide/emr-overview-arch.html#emr-arch-resource-management

---
#### versión README.md -> 1.0 (2022-octubre)
  
