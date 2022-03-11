docker build --no-cache -t image-python-mysql .

rm -rf ${PWD}/data

docker kill python_mysql
docker rm python_mysql

docker run --name python_mysql -i -t -d \
-v ${PWD}/data:/data/db \
-p 3304:3306 \
-e MYSQL_ROOT_PASSWORD=root \
-e MYSQL_DATABASE=my_python_database \
image-python-mysql
