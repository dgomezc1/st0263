from redis import StrictRedis
import sys

r = StrictRedis(host="localhost",port=6379,password="TopicosTelematica",db=0)


def list_example():
    print("RPUSH list:wishlist eafit intvir gog thm")
    r.rpush("list:wishlist", "eafit", "intvir", "gog", "thm")

    print("LRANGE list:wishlist 0 -1")
    value= r.lrange("list:wishlist", 0, -1)
    j = 0
    for i in value:
        print(str(j)+".)"+ "message = "+str(i.decode('utf-8')))
    
    print("\nLREM list:wishlist 0 gog")
    print(f'{r.lrem("list:wishlist", 0, "gog")}')
    
    print("\nLPOP list:wishlist")
    value = r.lpop("list:wishlist")
    print("Message:", value.decode('utf-8'))
    
    print("\nRPOPLPUSH list:wishlist list:visited")
    value = r.rpoplpush("list:wishlist", "list:visited")
    print("Message:", value.decode('utf-8'))

list_example()
