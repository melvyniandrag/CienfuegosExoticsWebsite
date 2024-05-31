FROM debian:bookworm

COPY requirements.txt .

RUN apt -y update && apt  -y upgrade

run apt -y install python3-dev python3-pip apache2 libapache2-mod-wsgi-py3

RUN apt -y install python3-django python3-djangorestframework python3-djangorestframework-simplejwt

COPY cienfuegosexotics.conf /etc/apache2/sites-available

COPY cienfuegosexotics /var/www/cienfuegosexotics

WORKDIR /var/www/cienfuegosexotics

RUN a2enmod wsgi

RUN a2dissite 000-default.conf

EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND"]
