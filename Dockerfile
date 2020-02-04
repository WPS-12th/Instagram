FROM        python:3.7-slim

RUN         apt -y update && apt -y dist-upgrade && apt -y autoremove
RUN         apt -y install nginx

# poetry export로 생성된 requirements.txt를 적절히 복사
COPY        ./requirements.txt /tmp/
RUN         pip install -r /tmp/requirements.txt

# 소스코드 복사
COPY        . /srv/instagram
WORKDIR     /srv/instagram/app

# Nginx설정파일을 복사
RUN         cp /srv/instagram/.config/instagram.nginx /etc/nginx/sites-enabled/
