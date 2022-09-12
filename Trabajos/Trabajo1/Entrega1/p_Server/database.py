import os,json 

class Databases: 

    def __init__(self , location=".\\db"): 
        self.location = os.path.expanduser(location) 
        self.loaddb(self.location) 

    def loaddb(self, key): 
        self.db = json.load(open(self.location, "r")) if os.path.exists(self.location) else {} 
        return True 

    def savedb(self): 
        try: 
            json.dump(self.db , open(self.location, "w+")) 
            return True 
        except: 
            return False 

    def save(self, key, value): 
        try: 
            self.db[str(key)] = value 
            self.savedb() 
            return "Base de datos actualizada".encode("utf-8")   
        except Exception as e: 
            print("[X] Error Saving Values to Database : " + str(e)) 
        return "No se ha podido actualizar la base de datos".encode("utf-8")   

    def get(self , key): 
        try: 
            return self.db[key].encode("utf-8")   
        except KeyError:  
            return "400 Elemento no encontrado".encode("utf-8")  

    def delete(self , key): 
        if not key in self.db: 
            return "400 Elemento no encontrado".encode("utf-8") 
        del self.db[key] 
        self.savedb() 
        return "200 OK Elemento eliminado con exito".encode("utf-8")  

    def resetdb(self): 
        self.db={} 
        self.savedb() 
        return True 

