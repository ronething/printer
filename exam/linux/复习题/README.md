# linux模拟试题

---

更新于 `2018/06/25 11:17`

今早考试

emm 发觉往年试题基本都要看，选择题考了很多，30道考了25左右。

简答题不出意料，考了往年的，下面整理了。今年考的是
stand-alone、xinetd、vfs(虚拟文件系统)、软链接和硬链接的区别、
X windows。

综合题就是makefile、还有往年试卷的看程序写每句话的意思(change函数)，看了往年试卷就知道了。最后一题是备份数据打包之类的。和往年试卷也大同小异。只能说简答题 40 分 4 道大题要背诵好。

以上。

溜了。

---

简答题知识点

卓乔贡献：

1、画出Linux操作系统的体系结构图，并说明每个模块的功能与联系。

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsm9e78b87j20lx0frwfd.jpg)

```
Linux操作系统的结构可以从两个层次上来划分。最上面的是用户（或应用程序空间），这是用户应用程序执行的地方。用户空间之下是内核空间，Linux内核正是位于这里。
1)	Linux 内核可以进一步划分成 3 层。
2)	最上面是系统调用接口，它实现了一些基本的功能，例如 read 和 write。
3)	系统调用接口之下是内核代码，可以更精确地定义为独立于体系结构的内核代码。这些代码是 Linux 所支持的所有处理器体系结构所通用的。
4)	在这些代码之下是依赖于体系结构的代码，构成了通常称为 BSP（Board Support Package）的部分。这些代码用作给定体系结构的处理器和特定于平台的代码。
```

2、画出VFS（虚拟文件系统）的结构图，并说明VFS的功能与作用。

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsmr709mfxj20dy09mq4p.jpg)

```
VFS功能：Linux系统可以支持多种文件系统，为此，必须使用一种统一的接口，这就是虚拟文件系统(VFS)。通过VFS将不同文件系统的实现细节隐藏起来，因而从外部看上去，所有的文件系统都是一样的。
```

3、说明软链接和硬链接的联系与区别。

```
联系：
1. 对软链接或硬链接的内容进行修改，会对原文件有效
2. 删除软链接或硬链接本身，不会对原文件有影响

区别：
1) 硬连接：给文件一个副本（别名），同时建立两者之间的连接关系，修改其中一个，与其连接的文件同时被修改，如果删除其中一个，其余的文件不受影响。磁盘上只有一份数据。创建硬链接会增加文件的链接数。当链接数变成0时，这个文件才会被真正删掉。
2) 软连接：只是一个快捷方式，是一个独立的文件，与原文件具有不同的inode节点。删除了原文件，这个连接文件就没用了。
```

4、画出X Window系统基本结构图，并说明每个组成部分的功能与作用。

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsmr8bd24tj20dy09075d.jpg)

```
整个X Window由三个部分组成：
1)X Server：是控制输出及输入设备并维护相关资源的程序，它接收输入设备的信息，并将其传给X Client，而将X Client传来的信息输出到屏幕上。
2)X Client：是应用程序的核心部分，它与硬件无关，每个应用程序就是一个X Client。X Client可以是终端仿真器（Xterm）或图形界面程序，它不直接对显示器绘制或者操作图形，而是与X Server通信，由X Server控制显示。
3)X protocol：X Client与X Server之间的通信协议。
```

5、以图解方式解释stand-alone工作模式和xinetd工作模式，并说明选择不同工作模式的原则。

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

![](https://ws1.sinaimg.cn/large/bdc70b0agy1fs9m0nnkivj20e4057wen.jpg)

> 两种模式如何做出选择：

```
xinetd和stand-alone工作模式相比，系统不想要每一个网路服务进程都监听器服务端口，运行单个xinetd就可以同时监听所有服务端口，这样就降低了系统开销，保护了系统资源。但是对于访问量大、经常出现并发访问的情况，xinetd则要频繁启动响应的网络服务进程，反而会导致系统性能下降。所以访问量少、并发少的情况下选择xinetd工作模式，访问量大、并发多的情况下选择stand-alone工作模式
```

6、Linux系统的特点是什么？

```
开放性、多用户、多任务、良好的用户界面、设备独立性、提供了丰富的网络功能、可靠的系统安全、良好的可移植性。
```

7、解释linux终端概念。

```
1)Linux终端也称为虚拟控制台 .一台计算机的输入输出设备就是一个物理的控制台 .
2)如果在一台计算机上用软件的方法实现了多个互不干扰独立工作的控制台界面，就是实现了多个虚拟控制台。 
3)Linux终端的工作方式是字符命令行方式，用户通过键盘输入命令进行操作，可以通过Linux终端对系统进行控制。 
```

8、Linux文件类型,各类型说明。

```
普通文件：普通文件包括文本文件、二进制可执行文件、shell脚本文件以及各种类型的数据文件，如图像文件、声音文件等。
d:目录文件：目录文件是一种特殊的文件，它们包含文件名和子目录名，以及查找这些文件和子目录所必需的信息。
l:链接文件：普通的链接实际上不是文件，它们仅是指向同一索引节点的目录条目，是一个索引节点表。
设备文件：Linux系统把每一个输入/输出设备都看成一个文件，与普通文件一样处理，这样可以使文件与设备的操作尽可能统一。其中可以读写单个字符的是c:设备字符设备（如键盘）；不能访问单个字符，而必须整块读写的设备称作b:块设备（如磁盘）。
s:Socket文件
p:管道文件
```

9、Linux系统运行级别（课本P18）

```
0：关机级别
1：单用户
2：多用户，无NFS，字符模式，无网络功能
3：多用户，NFS，字符模式，有网络功能。
4：用户自定义级别
5：图形界面模式（redhat常用运行级别）
6：重启级别

更改系统运行级别的方法：
1、root用户 `init n `或者`telinit n`,n为级别号
2、在字符终端界面上执行命令`startx`启动图形化环境。
3、更改/etc/inittab可以更改默认级别。
```

---

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

> ASCII 和 Binary

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

26、系统 管理 常用的二进制文件，一般放置在 __A__ 目录下。

A  /sbin    B  /root   C  /usr/sbin   D  /boot

```
/sbin:
主要放置系统管理的必备程序，例如:
cfdisk、dhcpcd、dump、e2fsck、fdisk、halt、ifconfig、ifup、 ifdown、init、insmod、lilo、lsmod、mke2fs、modprobe、quotacheck、reboot、rmmod、 runlevel、shutdown等。

/usr/sbin:
主要放置网路管理的必备程序，例如:
dhcpd、httpd、imap、in.*d、inetd、lpd、named、netconfig、nmbd、samba、sendmail、squid、swap、tcpd、tcpdump等 
```

27、通过修改文件______，可以设定开机时候自动安装的文件系统。  （C）

A  /etc/mtab  B  /etc/fastboot  C  /etc/fstab   D  /etc/inetd.conf

28、有如下的命令说明：mycommand \[-abcd][filename…],"…"表示______ (B)

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

```sh
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
	gcc -c my_app.c -Ifunctions
greeting.o: functions/greeting.c
	gcc -c functions/greeting.c
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

---

2、一个文件名字为rr.Z，可以用来解压缩的命令是 __D__。 

A   tar    B   gzip   C  compress    D  uncompress

```
uncompress命令 用来解压缩由compress命令压缩后产生的“.Z”压缩包。
compress -d 也可以解压缩

语法
uncompress(选项)(参数)
选项
-f：不提示用户，强制覆盖掉目标文件；
-c：将结果送到标准输出，无文件被改变；
-r：递归的操作方式。
```

9、不是shell具有的功能和特点的是 __C__。 

A 管道   B 输入输出重定向   C 执行后台进程   D 处理程序命令 

> 执行后台进程是内核的功能。（课本P9）

14、下面   B   不属于Linux内核系统。

A 内存管理    B IO管理    C 进程管理    D 设备驱动程序

```
linux内核实际上仅仅是一个资源管理器，包含以下几个组件：
1、系统调用接口
2、进程管理
3、内存管理
4、虚拟文件系统
5、网络堆栈
6、设备驱动程序
7、依赖于体系结构的代码
```

19、内核自行启动(已经被载入内存，开始运行，并已初始化所有的设备驱动程序和数据结构等)之后，通过启动一个用户级程序 `init` 的方式，完成了自己的引导进程。在这个过程中 `init` 进程的进程号PID为 __B__。

A  0   B  1   C  2   D  100

> `init`总是第一个进程(进程号PID总是`1`)(课本P107)

用ftp进行文件传输时，有两种模式  C   。 

A Word和binary    B .txt和Word Document

C ASCII和binary   D ASCII和Rich Text Format

> [ftp数据传输方式和工作方式](https://blog.csdn.net/zhaoyangkl2000/article/details/78225709)

> 文件传输模式：ASCII和二进制

> 工作模式：主动和被动 还有一种不常用的单端口模式。


26、下列关于链接描述，错误的是 __B__。 

A 硬链接就是让链接文件的i节点号指向被链接文件的i节点 

B 硬链接和符号连接都是产生一个新的i节点 

C 链接分为硬链接和符号链接 

D 硬连接不能链接目录文件

```
D 选项书里说 ln -d 可以硬链接自己的目录
但是实测不行。
B 应该才是错的。
```

![](https://ws1.sinaimg.cn/large/ecb0a9c3ly1fsm7z5hfrkj20k40cagm9.jpg)

---

```
设计一个Shell程序，在/userdata目录下建立50个目录，即user1～user50，并设置每个目录的权限，其中其他用户的权限为：读；文件所有者的权限为：读、写、执行；文件所有者所在组的权限为：读、执行。
```

> test.sh
```sh
#!/bin/bash
flag=49
while [ "$flag" -ge 0 ]
do
    echo "创建目录:user$((50-$flag))"
    mkdir -m 754 /userdata/user$((50-$flag))
    flag=$(($flag-1))
done
exit 0
```

> 效果图：

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fslo2hz87uj20jj0ewgmc.jpg)

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fslo45dt00j20ni082mxm.jpg)


[shell脚本——判断文件的属性、内容](https://blog.csdn.net/dongxie_tk/article/details/77772460)

```sh
1、针对以下shell程序，写出每一句语句的意义，并写出整个程序的作用是什么？

#!/bin/bash 使用bash来运行程序
FILENAME= 定义一个变量
echo “Input file name：” 提示用户输入一个文件名
read FILENAME 将用户输入的内容赋值给变量
if [ -c “$FILENAME” ] 判断文件是否是字符设备文件
then 
cp $FILENAME /dev 复制此文件到/dev目录下
fi
```

```
描述linux操作系统的体系结构，并使用图例表示，说明各部份之间的作用与关系。（课本P9）
```

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsm9e78b87j20lx0frwfd.jpg)

```
3、说明VFS（虚拟文件系统）的作用，并使用图例表示。（课本P10）应该和P87的差不多
```
![](https://ws1.sinaimg.cn/large/bdc70b0agy1fs9lgt0pydj20a10baaa7.jpg)


```makefile
# 根据以下makefile文件内容，画出目标依赖关系图。

OBJS = greeting.o my_app.o thank.o
CC = gcc
CFLAGS = -Wall -O –g
my_app:${OBJS}
    ${CC} ${OBJS} -o my_app
thank.o:test\thank.c test\thank.h
${CC} ${CFLAGS} -c test\thank.c
greeting.o:functions\greeting.c functions\greeting.h
    ${CC} ${CFLAGS} -c functions\greeting.c
my_app.o:my_app.c functions\greeting.h
    ${CC} ${CFLAGS} -c my_app.c -Ifunctions
```

> emm… ~~题目程序应该写错了。~~ 题目没错。。是我错了。以为类似`${CC} ${CFLAGS} -c test\thank.c`是错的，实际上他只是没有指定.o的文件名而已。

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsmrmbyyo6j20cz08nabt.jpg)


```
3、系统需要定期做数据库的备份工作，采用如下规则执行：
（1）每星期五晚上21点30分开始以oracle用户执行/home/oracle/exportdata.sh程序导出数据库数据文件，数据文件以dmp为后缀，每次共有5个这样的文件生成，保存在/oracle/backup目录下；
（2）待以上工作执行完毕后（大约需要运行3小时45分钟才结束），必须把导出来的数据文件进行打包成datafile.tar文件；
（3）每个星期四晚上22点把/oracle/backup目录下的datafile.tar文件删除，以腾出空间。
请根据以上描述给出相应的crontab文件内容。
```

[Linux 下以其他用户身份运行程序—— su、sudo、runuser](https://www.cnblogs.com/bodhitree/p/6018369.html)

```sh
su命令 用于切换当前用户身份到其他用户身份，变更时须输入所要变更的用户帐号与密码。（课本P96）

语法
su(选项)(参数)
选项
-:表示在切换用户的同时也改变环境变量
-c<指令>或--command=<指令>：执行完指定的指令后，即恢复原来的身份；
-f或——fast：适用于csh与tsch，使shell不用去读取启动文件；
-l或——login：改变身份时，也同时变更工作目录，以及HOME,SHELL,USER,logname。此外，也会变更PATH变量；
-m,-p或--preserve-environment：变更身份时，不要变更环境变量；
-s<shell>或--shell=<shell>：指定要执行的shell；
--help：显示帮助；
--version；显示版本信息。

tar的用法

打包
tar -cvf Desktop.tar Desktop/
tar -zcvf Desktop.tar.gz Desktop/
解压
tar -xvf Desktop.tar
tar -zxvf Destkop.tar.gz
```

```sh
30 21 * * 5 su - oracle -c "/home/oracle/exportdata.sh"
# 加上大约3小时45分 应该是星期 六 的01:15
15 01 * * 6 su - oracle -c "tar -cvf /oracle/backup/datafile.tar /oracle/backup/*.dmp"
0 22 * * 4 su - oracle -c "rm -f /oracle/backup/datafile.tar"
```

---

18、下面      不属于Linux操作系统。(A)

A  elive    B  redflag    C  AIX    D  Caldera

20、在 bash 中, 在一条命令后加入 "1>&2" 意味着：__C__

A  标准错误输出重定向到标准输入

B  标准输入重定向到标准错误输出

C  标准输出重定向到标准错误输出

D  标准输出重定向到标准输入

> 0代表标准输入，1代表标准输出，2代表标准错误输出。

26、下列不是Linux系统进程类型的是 __D__

A 交互进程     B 批处理进程     C 守护进程     D 就绪进程

30、以下关于GTK+的说法错误的是 __B__。

A  GTK+有自己的事件和事件监听器系统，叫做信号和回调函数

B  “delete-event”是所有构件都继承的信号

C  连接回调函数没有任何限制，可以将多个信号连接到一个回调函数

D  所有窗口部件创建函数都返回一个GtkWidget类型

> C是对的。详情百度

28、以下关于shell的说法错误的是 __C__。（猜的）

A  不同的shell解释器使用不同的shell命令语法

B  shell程序解释执行，不生成可以执行的二进制文件

C  适合用来完成时间紧迫型和处理器忙碌型的任务

D  可以帮助用户完成特定的任务，提高使用、维护系统的效率

```
1、现有一C程序文件为hello.c，用gcc编译该文件，请根据上述要求写出各条编译指令。
（1）生成对应的预处理后的C源程序
gcc -E hello.c -o hello.i
（2）生成预处理后的汇编程序
gcc -S hello.c
（3）生成目标文件
gcc -c hello.c 
（4）生成带调试信息的可执行文件
gcc hello.c
（5）hello.c有一头文件hello1.h放在hello.c所在目录的子目录dir1下，另一头文件hello2.h放在hello.c所在目录的子目录dir2下，生成可执行文件
gcc hello.c -o hello -Idi1 -Idir2
```

```
3、使用bash编写一脚本，脚本中必须采用函数的形式计算1+2+3+4+…+N的值，N为该脚本的参数，若没有参数则提示错误，若运行过程有错，需把错误信息丢弃。
```

```sh
#!/bin/bash

demo(){
    if [ -z $1 ]
    then
	echo "error"
	exit 1
    else
	sum=
	n=$1
	while [ $n -ge 1 ]
	do
	    sum=$((sum+n))
	    n=$((n-1))
	done
    fi
    echo "$sum"
     
}
demo $1
```

```sh
# 2、解释以下脚本各行的内容，并说明整个函数的功能是什么
1. change(){ # 定义一个名为change的函数
2.    sure='y' # 声明并初始化变量sure的值为’y’
3.    while [ $sure = 'y' ] # 循环判断，当变量sure等于’y’时执行循环体
4.    do # while循环开始
5.        echo 'input direction name' # 输出提示信息
6.        read dirname  # 读取用户输入并赋值给变量dirname
7.        for d in $dirname/*.doc # 循环 遍历变量dirname目录下的所有以doc为后缀的文件
8.        do    # 循环开始
9.			 test -f $d # 判断循环变量d是否是一个文件
10.			 if [ $? -eq 0 ];then # 判断上一条命令的结果是否等于0
11.					mv $d "${d%doc}txt" # 如果上一条命令的结果等于0，把变量d所存储的文件的后缀由doc改为txt
12.			 fi # 分支判断结束
13.        done # 循环结束
14.        echo 'Do you want to continue?' # 输出提示信息，询问用户是否继续
15.        read sure # 获取用户输入，并赋值给sure变量
16.   done  # 循环结束
17.}    #函数结束
```

5、下列说法，不正确的是 __D__。

A 根用户具有对整个系统的控制权	

B 特殊用户的账号也可以登录

C 普通用户之间的私有资源是可以相互隔离的

D 普通用户只能访问自己的Home目录 

6、假设执行cat /etc/passwd命令后，发现以下记录信息：
 `games:x:12:100:games:/usr/games:/sbin/nologin`，下列说法错误的是 __A__。

A 该用户的用户ID为100(gid才是100) B 该用户的home目录为/usr/games

C 该用户是一个特殊用户      D 该用户不能登录shell

> 由此题可见，系统用户（UID100以下）也称为特殊用户？

14、下面关于less和more的说法错误的是 __B__。

A less和more都可以实现分页查看功能

B 打开大型文档时，more命令的速度要快一点

C less提供上下浏览的功能

D more会把整个文档读入到内存中

17、不能使vi显示行号的命令是 __B__。（课本P72）

A :nu		B :set num		C :set nu		D :set number

> :nu 可以取得光标所在行号

18、在利用gdb进行调试过程中，如果需要单步执行，且不进入函数内部，应该使用 __A__。（课本P160）

A next		B step		C run		D go

> next 单步执行，且不进入函数内部
setp 单步执行，且进入函数内部
run 执行当前被调试的程序

> gdb -g 选项编译源文件，使程序在编译时包含调试信息。（今年考到了。）

23、要删除已经设定的crontab内容，可以使用的命令是_____。

A crontab -e		B crontab -r		C crontab -l		D deltab

> A 编辑
B 删除
C 列出

4、下列命令中，不能导致vi工作模式切换的是 __A__。

A dd B I    C /   D O

> dd 剪切行
I 在当前行的开始处添加文本
/ 进入末行模式
O在当前行的上面新建一行

8、普通用户可执行的关机命令是 __D__。（猜的）

A shutdown		B halt		C init		D poweroff

10、为了获取shell脚本调用时传入的参数个数，需要在shell脚本中使用 __A__。

A $#		B $@		C $0		D $*

15、下列命令中，能把光标移动到行尾的是_____。

A $		B ^		C e		D b

> ^ 移到当前行的行首
b移到当前字的字首，如果已经是在字首，则移动到上个字的字首
e移到当前字的字尾，如果已经是在字尾，则移动到下个字的字尾
