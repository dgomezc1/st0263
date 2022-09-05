#!/usr/bin/python
from redis import StrictRedis
import sys

r = StrictRedis(host="localhost",port=6379,password="TopicosTelematica",db=0)

def hmset_hvals_hkeys_hget():
    print("MSET user:david name 'David' edad 20")
    r.hset("user-david",{"name": "David", "age": 20})
    print("HVALS user:david")
    value = r.hvals("user-david")
    i = 1
    for key in value:
        print(str(i)+".) "+key.decode('utf-8'))
        i+=1

    print("\nHKEYS user:david")
    value = r.hkeys("user-david")
    i = 1
    for key in value:
        print(str(i)+".) "+key.decode('utf-8'))
        i+=1

    print("\nHGET user:david name")
    value = r.hget("user-david","name")
    print(value.decode('utf-8'))

hmset_hvals_hkeys_hget()