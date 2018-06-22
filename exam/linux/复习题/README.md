# linux模拟试题

- 选择题

2、dns域名系统主要负责主机名和____之间的解析。 (A)

A ip地址 B mac地址 C 网络地址 D 主机别名

4、系统中有用户user1和user2，同属于users组。在user1用户目录下有一文件file1，它拥有644的权限，如果user2用户想修改user1用户目录下的file1文件，应拥有_____权限。(B)     A   744    B   664      C   646     D  746s

（因为属于同一组 所以是664 r=4,w=2,x=1）

6、关于文件系统的安装和卸载，下面描述正确的是___。(A) 
A 如果光盘未经卸载，光驱是打不开的 

B 安装文件系统的安装点只能是/mnt下 

C 不管光驱中是否有光盘，系统都可以安装CD-ROM设备 

D mount /dev/fd0 /floppy 此命令中目录/floppy是自动生成的

10、文件标志b表示____ (C)

A  字符设备文件   B  目录文件  C  块设备文件  D  套接字

> d：目录文件
>
> l：链接文件
>
> p：管道文件
>
> s：Socker文件
>
> c：字符设备文件
>
> b：块设备文件

11、下面哪个文件定义了网络服务的端口？       （B）

A  /etc/netport       B  /etc/services  C  /etc/server        D  /etc/netconf

> /etc/services 该文件是网络服务名与端口号的映射文件

12、crontab文件由六个域组成，每个域之间用空格分割，其排列如下___。(B) 

A min hour day month year command 

B min hour day month dayofweek command 

C command hour day month dayofweek  

D command year month day hour min

> crontab  -e 编辑crontab
>
> crontab文件有固定的格式:
>
> f1 f2 f3 f4 f5 program
>
> min hour day month dayofweek command 
>
> f1为 \* 时表示每分钟、为a-b时表示从第a分钟到第b分钟都要执行。
>
> 为\*/n 时表示没n分钟执行一次。
>
> 为a,b,c...时表示第a,b,c...分钟要执行。
>
> 以上针对f1参数，其他以此类推。

17、Linux系统中不存在___基本文件类型。(B)

 A 普通文件   B 系统文件  C 目录文件  D 链接文件  E 特殊文件

18、在shell脚本中，用来读取文件内各个域的内容并将其赋值给shell变量的命令是____。 (D)

A fold     B join    C tr     D read

21、ftp的数据传送模式有___种。（B）

A  1   B  2   C  3   D  4

> 主动和被动。但是网上说还有另一种单端口。emm

22、使用at规划进程任务时，为了删除已经规划好的工作任务，我们可以使用______工具。  A  atq   B  atrm 　C  rm 　D  del

>at -d 或者 atrm

23、下列对shell变量FRUIT操作，正确的是：___。(C)

A 为变量赋值：\$FRUIT=apple  

B 显示变量的值：fruit=apple  

C 显示变量的值：echo \$FRUIT 

D 判断变量是否有值：[ -f “$FRUIT” ]

> -f file 如果文件是一个普通文件则结果为真
>
> -n string 如果字符串不为空则结果为真
>
> -z string 如果字符串为空则结果为真

24、内核引导信息在系统启动完成后，存放在： （C）
A  /var/log/syslog      B  /var/log/start 

 C  /var/log/messages    D  /var/log/statues

> /var/log/messages 包含整体系统信息，其中也包含系统启动期间的日志。此外，mail、cron、daemon、kern和auth等内容也记录在/var/log/messages 日志中。

27、通过修改文件______，可以设定开机时候自动安装的文件系统。  （C）

A  /etc/mtab  B  /etc/fastboot  C  /etc/fstab   D  /etc/inetd.conf

28、有如下的命令说明：mycommand \[-abcd][filename…],"…"表示______ (A)
A 只有一个参数      B 可以有一个以上的参数 

C 该参数可以省略    D 该参数位置可变

29、为了得到上一个后台执行的命令的PID，我们可以使用变量______ (D)

A  \$#    B  \$@    C  \$0   D  $!

> $$ 
> Shell本身的PID（ProcessID） 
> $! 
> Shell最后运行的后台Process的PID 
> $? 
> 最后运行的命令的结束代码（返回值） 
> $- 
> 使用Set命令设定的Flag一览 
> $* 
> 所有参数列表。如"\$*"用「"」括起来的情况、以"$1 $2 … $n"的形式输出所有参数。 
> $@ 
> 所有参数列表。如"\$@"用「"」括起来的情况、以"$1" "$2" … "$n" 的形式输出所有参数。 
> $# 
> 添加到Shell的参数个数 
> $0 
> Shell本身的文件名 
> \$1～$n 
> 添加到Shell的各参数值。$1是第1参数、$2是第2参数…。

---

- 简答题

1、linux系统的特点是什么？

```
开放性、多用户、多任务、良好的用户界面、设备独立性、丰富的网络功能、可靠的系统安全、良好的可移植性。
```

2、解释linux终端概念。

```
1)Linux终端也称为虚拟控制台 .一台计算机的输入输出设备就是一个物理的控制台 .
2)如果在一台计算机上用软件的方法实现了多个互不干扰独立工作的控制台界面，就是实现了多个虚拟控制台。 
3)Linux终端的工作方式是字符命令行方式，用户通过键盘输入命令进行操作，可以通过Linux终端对系统进行控制。 
```

3、说明VFS（虚拟文件系统）的作用，并使用图例表示。

```
Linux系统可以支持多种文件系统，为此，必须使用一种统一的接口，这就是虚拟文件系统(VFS)。通过VFS将不同文件系统的实现细节隐藏起来，因而从外部看上去，所有的文件系统都是一样的。
```

![](https://ws1.sinaimg.cn/large/bdc70b0agy1fs9lgt0pydj20a10baaa7.jpg)

4、以图解方式解释服务的xinetd工作模式和stand-alone工作模式，并说明选择不同工作模式的原则。

```
1）运行独立的守护进程工作方式称作：stand－alone。它是Unix传统的C/S模式的访问模式。服务器监听（Listen）在一个特点的端口上等待客户端的联机。如果客户端产生一个连接请求，守护进程就创建（Fork）一个子服务器响应这个连接，而主服务器继续监听。以保持多个子服务器池等待下一个客户端请求。
```

![stand-alone](https://ws1.sinaimg.cn/large/bdc70b0agy1fs9lw41uvej20bg058aa5.jpg)

```
2）从守护进程的概念可以看出，对于系统所要通过的每一种服务，都必须运行一个监听某个端口连接所发生的守护进程，这通常意味着资源浪费。
为了解决这个问题，Linux引进了“网络守护进程服务程序”的概念。Redhat Linux 9.0使用的网络守护进程是xinted（eXtended InterNET daemon）。和stand－alone模式相比xinted模式也称 Internet Super－Server（超级服务器）。
xinetd能够同时监听多个指定的端口，在接受用户请求时，他能够根据用户请求的端口不同，启动不同的网络服务进程来处理这些用户请求。
可以把xinetd看做一个管理启动服务的管理服务器，它决定把一个客户请求交给那个程序处理，然后启动相应的守护进程。 
```

![xinetd](https://ws1.sinaimg.cn/large/bdc70b0agy1fs9m0nnkivj20e4057wen.jpg)

---

- 综合应用题

```
1、编写一段bash shell程序，完成：根据从键盘输入的学生学号、成绩，通过计算成绩的等级后，把学生学号、成绩、成绩等级记录在mark.txt文件中。其中60分以下为“Failed！”，60-70分为“Passed！”，70-80分为“Medium！”，80-90分为“Good！”，90-100为“Excellent！”。

如果输入超过100的分数，则显示错误分数提示。
```

```shell
#!/bin/bash
if [ "$2" -lt 60 -a "$2" -ge 0 ]
then
    echo "$1,$2 Failed!" >> mark.txt
elif [ "$2" -ge 60 -a "$2" -lt 70 ]
then
    echo "$1,$2 Passed!" >> mark.txt
elif [ "$2" -ge 70 -a "$2" -lt 80 ]
then
    echo "$1,$2 Medium!" >> mark.txt
elif [ "$2" -ge 80 -a "$2" -lt 90 ]
then
    echo "$1,$2 Good!" >> mark.txt
elif [ "$2" -ge 90 -a "$2" -le 100 ]
then
    echo "$1,$2 Excellent!" >> mark.txt
else
    echo "error"
    exit 1
fi
exit 0
```

效果图：

![](https://ws1.sinaimg.cn/large/bdc70b0agy1fs9mqdm2juj20nq03iweo.jpg)

````
2、根据以下目标依赖关系图，写出makefile文件内容。
````

![](https://ws1.sinaimg.cn/large/bdc70b0agy1fs9jf33yn0j20ic09r40t.jpg)

```makefile
my_app: my_app.o greeting.o
	gcc my_app.o greeting.o -o my_app
my_app.o: my_app.c
	gcc -c my_app.c -o greeting.c -Ifunctions
greeting.o: functions/greeting.c
	gcc -c functions/greeting.c -o greeting.o -Ifunctions
```

```
3、某用户需要在每天晚上11点启动服务器的ftp服务，使得其他用户可以上传重要数据。而在每天凌晨3点就关闭ftp服务。在这个过程中要自动记录日志信息，每天是否成功启动ftp要体现在日志信息中，如果成功启动必须记录ftp的进程信息，如果没有启动，就记录错误信息。
约定如下：日志文件为/tmp/ftplog
请根据以上描述给出相应的crontab文件内容以及相关脚本。
```

```shell
# crontab 文件内容
0 23 * * * /root/startftp
0 3  * * * /root/stopftp
# 相关脚本

# startftp
#!/bin/bash
/usr/sbin/vsftpd start
# 注： ps -ef | grep vsftp | grep -v grep 为去掉带有grep的那一条进程
# grep --help 查看 -v 参数 
# -v, --invert-match        select non-matching lines
# awk '{print $2}' 打印第二列 即打印进程号pid
tmp=`ps -ef | grep vsftpd | grep -v grep | awk '{print $2}'`
# -n string 如果字符串不为空则为真
if [ -n $tmp ]
then
	echo `ps -ef | grep vsftp |grep -v grep`  >> /tmp/ftplog
else
	echo "FTP START FAILED" >> /tmp/ftplog

# stopftp
#!/bin/bash
/usr/sbin/vsftpd stop
# 注： ps -ef | grep vsftp | grep -v grep 为去掉带有grep的那一条进程
# grep --help 查看 -v 参数 
# -v, --invert-match        select non-matching lines
# awk '{print $2}' 打印第二列 即打印进程号pid
tmp=`ps -ef | grep vsftpd | grep -v grep | awk '{print $2}'`
# -z string 如果字符串为空则为真
if [ -z $tmp ]
then
	echo "FTP STOP SUCCESS"  >> /tmp/ftplog
else
	echo "FTP STOP FAILED" >> /tmp/ftplog
```

