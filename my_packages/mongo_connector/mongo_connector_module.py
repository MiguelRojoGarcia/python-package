from pymongo import MongoClient

class MongoConnectorModule:
    
    __client = None    
    
    ## Constructor
    def __init__(self , url_connection ) ->None:
     
        try:

            self.__client = MongoClient(url_connection)   
            
        except Exception as e:
            print(f"Error connection to server {url_connection}: {e}")
    
    
    @property
    def client(self):
        return self.__client
