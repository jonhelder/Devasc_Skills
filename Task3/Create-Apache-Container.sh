#!/bin/basc
#docker stop apache-container
#docker rm apache-container
#docker rmi apache-image
echo "FROM python" > Dockerfile
echo "RUN apt-get update" >> Dockerfile
echo "RUN apt-get install apache2 -y && apt-get clean" >> Dockerfile
echo "RUN sed -i 's/80/8081/g' /etc/apache2/ports.conf" >> Dockerfile
echo "RUN sed -i 's/*:80/*:8081/g' /etc/apache2/sites-available/000-default.conf" >> Dockerfile
echo "EXPOSE 8081"  >> Dockerfile
# echo "RUN service apache2 start" >> Dockerfile # deze werkt niet
echo "CMD apachectl -D FOREGROUND" >> Dockerfile
docker build -t apache-image .
docker run -t -d -p 8081:8081 --name apache-container apache-image
