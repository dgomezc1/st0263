from redis import StrictRedis
import sys

r = StrictRedis(host="localhost",port=6379,password="TopicosTelematica",db=0)

def sorted_sets():
    print("ZADD visits 500 7wks 9 gog 9999 prag")
    print(f'{r.zadd("visits", {"7wks":500, "gog":9, "prag":9999})}')

    print("ZINCRBY visits 1 prag")
    print(f'{r.zincrby("visits", 1, "prag")}')

sorted_sets()