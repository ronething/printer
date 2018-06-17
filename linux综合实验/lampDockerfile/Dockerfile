FROM ubuntu:latest

MAINTAINER admin@ronething.cn

EXPOSE 80

RUN echo "deb http://mirrors.ustc.edu.cn/ubuntu/ bionic main restricted universe multiverse" > /etc/apt/sources.list \
	&& echo "deb-src http://mirrors.ustc.edu.cn/ubuntu/ bionic main restricted universe multiverse" >> /etc/apt/sources.list \
	&& echo "deb http://mirrors.ustc.edu.cn/ubuntu/ bionic-security main restricted universe multiverse" >> /etc/apt/sources.list \
	&& echo "deb-src http://mirrors.ustc.edu.cn/ubuntu/ bionic-security main restricted universe multiverse" >> /etc/apt/sources.list \
	&& echo "deb http://mirrors.ustc.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse" >> /etc/apt/sources.list \
	&& echo "deb-src http://mirrors.ustc.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse" >> /etc/apt/sources.list \
	&& echo "deb http://mirrors.ustc.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse" >> /etc/apt/sources.list \
	&& echo "deb-src http://mirrors.ustc.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse" >> /etc/apt/sources.list

RUN apt-get update \
	&& apt-get install apache2 -y \
	&& apt-get install php7.2 -y \
	&& apt-get install libapache2-mod-php7.2 \
	&& apt-get install mysql-server -y \
	&& apt-get install php7.2-mysql \
	&& apt-get install phpmyadmin -y \
	&& rm -rf /var/lib/apt/lists/* \
	&& ln -s /usr/share/phpmyadmin /var/www/html/phpmyadmin \

CMD ["/bin/bash"]
