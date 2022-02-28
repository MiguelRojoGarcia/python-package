rm -rf ${PWD}/mongo/data

docker run --name python_mongodb -i -t \
-v ${PWD}/mongo/data:/data/db \
-v ${PWD}/mongo/init.js:/docker-entrypoint-initdb.d/init.js \
-p 27017 \
-e MONGO_INITDB_ROOT_USERNAME=admin \
-e MONGO_INITDB_ROOT_PASSWORD=root \
-e MONGO_INITDB_DATABASE=python_course \
mongo