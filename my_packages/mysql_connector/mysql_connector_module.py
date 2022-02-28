import mysql.connector

class MysqlConnectorModule:
    
    __db_user = None
    __db_pass = None
    __db_name = None
    __db_host = None

    __cursor = None 
    __connection = None 

    ## Constructor
    def __init__(self , db_user , db_pass , db_name , db_host = 'localhost' , port = 3306) ->None:
     
        try:
            self.__connection = mysql.connector.connect(
                user= db_user, 
                password= db_pass,
                host= db_host,
                database=db_name,
                port= port
            )

            self.__cursor = self.__connection.cursor(dictionary=True , buffered=True)

        except Exception as e:
            print(f"Error connection to server {db_host}:{port} - {db_name} {e}")

    ## Execute single query (INSERT ,  DELETE , ...)
    def executeQuery(self , query):
        try:
            self.__cursor.execute(query)
            self.__connection.commit()
            return self.__cursor.rowcount
        except Exception as e:
            print(f"Error executing query {query} - {e}")
    
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
    
    ## Close connection
    def closeConnection(self):
        self.__connection.close()