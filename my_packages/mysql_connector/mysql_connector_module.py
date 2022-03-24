import string
import mysql.connector
import hashlib

class MysqlConnectorModule:
    
    __cursor = None 
    __connection = None 

    ## Constructor
    def __init__(self , username , password , database , host = 'localhost' , port = 3306) ->None:
     
        self.__connection = mysql.connector.connect(
                user= username, 
                password= password,
                host= host,
                database=database,
                port= port
            )

        self.__cursor = self.__connection.cursor(dictionary=True , buffered=True)

    ## Execute single query (INSERT ,  DELETE , ...)
    def executeQuery(self , query):
        try:
            self.__cursor.execute(query)
            self.__connection.commit()
            return self.__cursor.rowcount
        except Exception as e:
            print(f"Error executing query {query} - {e}")
    
    # Cypher str (for password storage or delicate info)
    def encryptString(self,str = ''):
        cypher = hashlib.sha256()
        cypher.update(str.encode('utf8'))
        return cypher.hexdigest()

    ## Get data query (SELECT)
    def getResults(self , query , get_first = False):
        try:
            self.__cursor.execute(query)

            if get_first:
                return self.__cursor.fetchone()
            else:    
                return self.__cursor.fetchall()
            
        except Exception as e:
            print(f"Error executing query {query} - {e}")
    
    #Insert record 
    def insertRecord(self, table, data = dict):

        sql = f'INSERT INTO {table} VALUES ( null '
        
        dict_keys = data.keys()

        for key in dict_keys:
            sql += f',\'{data[key]}\''

        sql += ' )'

        self.executeQuery(sql)

        pass

    ## Close connection
    def closeConnection(self):
        self.__connection.close()