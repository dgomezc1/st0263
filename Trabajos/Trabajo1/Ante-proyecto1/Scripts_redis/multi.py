#!/usr/bin/python
from redis import StrictRedis
import sys

r = StrictRedis(host="localhost",port=6379,password="TopicosTelematica",db=0)

def multi_exec():
    print("\n********Displaying transaction...*******")
    print("Query: SET pakc:prag http://pragprog.com")
    p = r.pipeline()
    print(f"Status: {p.set('pakc:prag', 'http://pragprog.com')}")
    print("Query: INCR count")
    print(f"Status: {p.incr('count')}")
    print(f"Status: {p.execute()}")
    p.mget({'pack:prag','count'})   
    value = p.execute()
    print("message = "+str(value))
    
multi_exec()