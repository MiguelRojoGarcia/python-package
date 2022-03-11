import pytest
from my_packages.mysql_connector.mysql_connector_module import MysqlConnectorModule

db_connection = {
    'user':'root',
    'password':'root',
    'database':'my_python_database',
    'host':'127.0.0.1',
    'port':3304
}

common_mysql_connector = MysqlConnectorModule( db_connection['user'], db_connection['password'] , db_connection['database'] , db_connection['host'] , int(db_connection['port']))

def test_basic_connection():
    MysqlConnectorModule( db_connection['user'], db_connection['password'] , db_connection['database'] , db_connection['host'] , int(db_connection['port']))
    assert True

def test_failed_execption():
    with pytest.raises(Exception):
        MysqlConnectorModule(1,2,3,4,5)

def test_execute_query():

    try:

        query = """DROP TABLE test_users"""
        common_mysql_connector.executeQuery(query)

        query = """CREATE TABLE IF NOT EXISTS test_users (
            id INTEGER PRIMARY KEY AUTO_INCREMENT, 
            name varchar(255) not null, 
            surname varchar(255) not null, 
            email varchar(255) not null
        )"""

        common_mysql_connector.executeQuery(query)

        query = """TRUNCATE TABLE test_users"""

        common_mysql_connector.executeQuery(query)

        users = [
            {'name':'Miguel','surname':'Rojo','email':'mrojo@gmail.es'},
            {'name':'Marco','surname':'Guerrero','email':'mguerrero@gmail.es'}
        ]

        for user in users:
            insertQuery = f"INSERT INTO test_users (name , surname , email) VALUES (\"{user['name']}\" , \"{user['surname']}\", \"{user['email']}\")"
            common_mysql_connector.executeQuery(insertQuery)

        assert True

    except:
        assert False

def test_get_unique_result():

    try:

       insertQuery = f"INSERT INTO test_users (name , surname , email) VALUES ('Marta' , 'Guerrero', 'mgerrero@test.es')"
       common_mysql_connector.executeQuery(insertQuery)

       result = common_mysql_connector.getResults("SELECT * FROM test_users WHERE email = 'mgerrero@test.es'" , True )
       
       assert type(result) == dict

    except:
        assert False

def test_get_results():

    try:

       result = common_mysql_connector.getResults("SELECT * FROM test_users")
       
       assert type(result) == list

    except:
        assert False