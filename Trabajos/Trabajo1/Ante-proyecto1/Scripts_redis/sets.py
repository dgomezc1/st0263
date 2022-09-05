#!/usr/bin/python
from redis import StrictRedis
import sys

r = StrictRedis(host="localhost",port=6379,password="TopicosTelematica",db=0)

def setsExample():
    print("Query: SADD news nytimes.com pragprog.com picso.com.co ")
    r.sadd("news", "nytimes.com", "pragprog.com", "picso.com.co")

    print("Query: SMEMBERS news\nMessage: ")
    value = r.smembers("news")
    i = 1
    for key in value:
        print(str(i)+".) "+key.decode('utf-8'))
        i+=1
    
    print("\nQuery: SADD tech bbc.com pragprog.com epic.com.co ")
    r.sadd("tech", "bbc.com", "pragprog.com", "epic.com.co")

    print("\nQuery: SMEMBERS news")
    value = r.smembers("tech")
    i = 1
    for key in value:
        print(str(i)+".) "+key.decode('utf-8'))
        i+=1

    print("\nQuery: SINTER news tech ")
    value = r.sinter("news", "tech")
    i = 1
    for key in value:
        print(str(i)+".) "+key.decode('utf-8'))
        i+=1

    print("\nQuery: SDIFF news tech ")
    value = r.sdiff("news", "tech")
    i = 1
    for key in value:
        print(str(i)+".) "+key.decode('utf-8'))
        i+=1

    print("\nQuery: SUNION news tech ")
    value = r.sunion("news", "tech")
    i = 1
    for key in value:
        print(str(i)+".) "+key.decode('utf-8'))
        i+=1   

    print("\nQuery: SUNIONSTORE websites news tech ")
    print(f'{r.sunionstore("websites", "news", "tech")}')

setsExample()