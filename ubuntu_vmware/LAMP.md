<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Ubuntu 18.04 LTS 搭建 LAMP 环境](#ubuntu-1804-lts-%E6%90%AD%E5%BB%BA-lamp-%E7%8E%AF%E5%A2%83)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Ubuntu 18.04 LTS 搭建 LAMP 环境

这次我们来了解一下ubuntu如何搭建lamp环境。

上次我们刚安装了虚拟机。

所以首先我们要更改一下软件源。（官方源实在是太慢了。）

[ubuntu配置源](https://mirrors.ustc.edu.cn/repogen/)

上这个网址。

下载自己需要的源。

我这里还是先下载`openssh-server` 然后`ssh`登录操作吧。电脑太卡了。

![](https://ws1.sinaimg.cn/large/bdc70b0agy1fs9d4m33wkj20o90f5dgw.jpg)

连接进去后我们首先更改一下镜像源。

`sources.list` 放在`/etc/apt/`目录下

```
deb https://mirrors.ustc.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb-src https://mirrors.ustc.edu.cn/ubuntu/ bionic main restricted universe multiverse

deb https://mirrors.ustc.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
deb-src https://mirrors.ustc.edu.cn/ubuntu/ bionic-security main restricted universe multiverse

deb https://mirrors.ustc.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb-src https://mirrors.ustc.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse

deb https://mirrors.ustc.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
deb-src https://mirrors.ustc.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
```

然后`sudo apt-get update` update 一下

---

接下来我们搭建lamp环境

首先要安装`apache2`

```
sudo apt-get install apache2 -y
```

安装完成后访问虚拟机ip可以看到如下界面：

![](https://ws1.sinaimg.cn/large/bdc70b0agy1fs9dqpuhmij21fm0rhmzx.jpg)

然后安装`php`

```
sudo apt-get install php7.2 -y
```

安装`php`相关组件

```
sudo apt-get install libapache2-mod-php7.2
```

安装`mysql`服务

```
sudo apt-get install mysql-server -y
```

安装`php-mysql`相关组件

```
sudo apt-get install php7.2-mysql
```

到这里 lamp 环境其实已经搭建完毕。下面为可选项。

---

安装 `phpmyadmin`（可选）

>  phpMyAdmin 是一个以PHP为基础，以Web-Base方式架构在网站主机上的MySQL的数据库管理工具。

```
sudo apt-get install phpmyadmin -y
```

![](https://ws1.sinaimg.cn/large/bdc70b0agy1fs9dn84jsoj20om0q2t94.jpg)

这里选择`apache2`

```
sudo ln -s /usr/share/phpmyadmin /var/www/html/phpmyadmin
```

访问虚拟机ip/phpmyadmin 可以看到如下界面

![](https://ws1.sinaimg.cn/large/bdc70b0agy1fs9ds3kjz3j21fm0rhgm9.jpg)

重启`mysql`、`apache2`服务 

```
sudo service mysql restart
```

```
sudo service apache2 restart
```

