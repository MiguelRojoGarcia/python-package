from my_packages.mysql_connector.mysql_connector_module import MysqlConnectorModule

db_connection = {
    'user':'root',
    'password':'root',
    'database':'my_python_database',
    'host':'localhost',
    'port':3304
}

mysql_connector = MysqlConnectorModule( 'root' , 'root' , 'my_python_database' , 'localhost' , 3304)