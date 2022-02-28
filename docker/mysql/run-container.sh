docker build --no-cache -t python-mysql .

docker stop python_mysql

rm -rf ${PWD}/data

docker run --name python_mysql -i -t \
-v ${PWD}/data:/data/db \
-p 3304:3306 \
-e MYSQL_ROOT_PASSWORD=root \
-e MYSQL_DATABASE=my_python_database \
python-mysql
