#!/usr/bin/python
from redis import StrictRedis
import sys

r = StrictRedis(host="localhost",port=6379,password="TopicosTelematica",db=0)

def getPackt(key):
    #GET value stored in packt:welcome
    print("Query:", key)
    value = r.get(key)
    print("message = " + str(value.decode('utf-8')))

def setPackt(key, value):
    #SET new value packt:welcome
    print("\n********Displaying get...*******")
    print(f"Query: SET {key} {value} \nStatus: {r.set(key,value)}")

def setMultiSet(dicc):
    print("\n********Displaying multiples message...*******")
    print("Query: MSET ", end="")
    for clave in dicc:
        print(clave,dicc[clave], end=" ")
    print(f"\nStatus: {r.mset(dicc)}")

def getMultiSet():  
    value = r.mget({'pack:ytb','pack:outlo'})
    for i in value:
        print("message = "+str(i.decode('utf-8')))

def incr_action():
    r.incr('count')
    value = r.get('count')
    print("\n********Displaying incr...*******")
    print("Valor = "+str(value.decode('utf-8')))
    print(f"Query: {r.incr('count')}")
    value = r.get('count')
    print("Valor incrementado = "+str(value.decode('utf-8')))


setPackt('pack:aws','https://awsacademy.instructure.com/')
getPackt('pack:aws')
setMultiSet({'pack:outlo':'https://outlook.office365.com/', 'pack:ytb': 'https://www.youtube.com/'})
getMultiSet()
incr_action()
