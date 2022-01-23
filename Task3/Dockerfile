FROM python
RUN apt-get update
RUN apt-get install apache2 -y && apt-get clean
RUN sed -i 's/80/8081/g' /etc/apache2/ports.conf
RUN sed -i 's/*:80/*:8081/g' /etc/apache2/sites-available/000-default.conf
EXPOSE 8081
CMD apachectl -D FOREGROUND
