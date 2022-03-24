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
            email varchar(255) not null,
            password varchar(255) not null
        )"""

        common_mysql_connector.executeQuery(query)

        query = """TRUNCATE TABLE test_users"""

        common_mysql_connector.executeQuery(query)

        assert True

    except:
        assert False

def test_get_unique_result():

    try:

       common_mysql_connector.insertRecord('test_users',{
           'name':'marta',
           'surname':'Guerrero',
           'email':'mgerrero@test.es',
           'password':common_mysql_connector.encryptString('M4rt4!')
        })
 
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

def test_insert_record():

    try:

        users = [
            {'name':'Miguel','surname':'Rojo','email':'mrojo@gmail.es','password': common_mysql_connector.encryptString('M1gu3l!')},
            {'name':'Marco','surname':'Guerrero','email':'mguerrero@gmail.es','password': common_mysql_connector.encryptString('M4rc0!')}
        ]

        for user in users:
            common_mysql_connector.insertRecord('test_users',user)
    
        assert True

    except:
        assert False

   