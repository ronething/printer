<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [第 2 章 新手必须掌握的 Linux 命令](#%E7%AC%AC-2-%E7%AB%A0-%E6%96%B0%E6%89%8B%E5%BF%85%E9%A1%BB%E6%8E%8C%E6%8F%A1%E7%9A%84-linux-%E5%91%BD%E4%BB%A4)
  - [常用系统工作命令](#%E5%B8%B8%E7%94%A8%E7%B3%BB%E7%BB%9F%E5%B7%A5%E4%BD%9C%E5%91%BD%E4%BB%A4)
  - [系统状态检测命令](#%E7%B3%BB%E7%BB%9F%E7%8A%B6%E6%80%81%E6%A3%80%E6%B5%8B%E5%91%BD%E4%BB%A4)
  - [工作目录切换命令](#%E5%B7%A5%E4%BD%9C%E7%9B%AE%E5%BD%95%E5%88%87%E6%8D%A2%E5%91%BD%E4%BB%A4)
  - [文本文件编辑命令](#%E6%96%87%E6%9C%AC%E6%96%87%E4%BB%B6%E7%BC%96%E8%BE%91%E5%91%BD%E4%BB%A4)
  - [文件目录管理命令](#%E6%96%87%E4%BB%B6%E7%9B%AE%E5%BD%95%E7%AE%A1%E7%90%86%E5%91%BD%E4%BB%A4)
  - [打包压缩与搜索命令](#%E6%89%93%E5%8C%85%E5%8E%8B%E7%BC%A9%E4%B8%8E%E6%90%9C%E7%B4%A2%E5%91%BD%E4%BB%A4)
  - [复习题](#%E5%A4%8D%E4%B9%A0%E9%A2%98)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# 第 2 章 新手必须掌握的 Linux 命令

- `man`命令中常用按键以及用途

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsrdrhrknyj20mj0ci400.jpg)

- `man`命令帮助信息的结构以及意义

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsrdsy4yb3j20mq0c4dh8.jpg)

举例：`man man`

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsrdvph3bzj20o20nu0uq.jpg)

## 常用系统工作命令

- `echo` 输出字符串或变量的值。

- `date` 用于显示及设置系统的时间或日期。`date [选项] [+指定的格式]` 其中`+`可以格式化。

参数列表：

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsre0ltqizj20mo08ewf1.jpg)

举例：`date "+%Y-%m-%d %H:%M:%S"`

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsrecwwaxyj20j6015a9w.jpg)

- `reboot` 重启系统

- `poweroff` 关闭系统

- `wget` 用于在终端中下载网络文件

参数列表：

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsree9lc79j20mw08l752.jpg)

举例：`wget https://www.linuxprobe.com/docs/LinuxProbe.pdf`

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsregm9q21j20o308fjrx.jpg)

- `ps` 用于查看系统中的进程状态

参数列表：

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsreqmcx37j20ml04z3z2.jpg)

在 Linux 系统中，有5中常见的进程状态，分别为运行，中断，不可中断，僵死与停止，其各自含义如下所示。

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsrevq6zk8j20lc09g40j.jpg)

进程状态各列的含义：

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsrewtf2ekj20n00c0mz4.jpg)

```
在Linux系统中的命令参数有长短格式之分，长格式和长格式之间不能合并，长格式和短格式之间也不能合并，但短格式和短格式之间是可以合并的，合并后仅保留一个-（减号）即可。另外ps命令可允许参数不加减号（-），因此可直接写成ps aux的样子。
```

- `top` 用于动态监视进程活动与系统负载等信息。

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsrf5bzkzij20vv05774r.jpg)

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsrf5qr8zcj20n70ax42f.jpg)

- `pidof` 用于查询某个指定服务进程的`PID`值。

举例：

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsrf85l4x6j20iz016dfn.jpg)

- `kill` 用于终止某个指定`PID`的服务进程。

- `killall` 用于终止某个指定名称的服务所对应的 __全部__ 进程。

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsrfc2sgcuj20mt06zmzj.jpg)

## 系统状态检测命令

- `ifconfig` 用于获取网卡配置与网络状态等信息。

主要用处：

```
使用ifconfig命令来查看本机当前的网卡配置与网络状态等信息时，其实主要查看的就是网卡名称、inet参数后面的IP地址、ether参数后面的网卡物理地址（又称为MAC地址），以及RX、TX的接收数据包与发送数据包的个数及累计流量
```

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsrfinisn8j20iv09z0tc.jpg)

- `uname` 用于查看系统内核与系统版本等信息。

```
在使用uname命令时，一般会固定搭配上-a参数来完整地查看当前系统的内核名称、主机名、内核发行版本、节点名、系统时间、硬件名称、硬件平台、处理器类型以及操作系统名称等信息。
```

举例：

```sh
uname -a
cat /etc/redhat-release
```

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsrfl5wifrj20mp06a758.jpg)

- `uptime` 用于查看系统的负载信息。

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsrfmrouj5j20nt01ta9x.jpg)

跟`top`第一行应该是一样的。

- `free` 用于显示当前系统中内存的使用量信息。

举例：`free -h` `-h`人性化显示（GB，MB之类的）

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsrfqfx2xdj20ml07w3z5.jpg)

- `who` 用于查看当前登入主机的用户终端信息。

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsrfsblu51j20nh061weu.jpg)

- `last` 用于查看所有系统的登录记录。

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsrfww3blsj20n9088abz.jpg)

- `history` 用于显示历史执行过的命令。

```
执行history命令能显示出当前用户在本地计算机中执行过的最近1000条命令记录。如果觉得1000不够用，还可以自定义/etc/profile文件中的HISTSIZE变量值。在使用history命令时，如果使用-c参数则会清空所有的命令历史记录。还可以使用“!编码数字”的方式来重复执行某一次的命令。
```

- `sosreport` 用于收集系统配置及架构信息并输出诊断文件。

```
当Linux系统出现故障需要联系技术支持人员时，大多数时候都要先使用这个命令来简单收集系统的运行状态和服务配置信息，以便让技术支持人员能够远程解决一些小问题，亦或让他们能提前了解某些复杂问题。
```

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsrg11lcbhj20m409igmm.jpg)

## 工作目录切换命令

- `pwd` 用于显示用户当前所处的工作目录。

- `cd` 用于切换工作路径。

`cd -` 返回上一次所处的目录。

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fss8bbvulgj20ld045mxc.jpg)

```
使用“cd ..”命令进入上级目录，以及使用“cd ~”命令切换到当前用户的家目录，亦或使用“cd ~username”切换到其他用户的家目录。
```

- `ls` 用于显示目录中的文件信息。

```
使用ls命令的“-a”参数看到全部文件（包括隐藏文件），使用“-l”参数可以查看文件的属性、大小等详细信息。将这两个参数整合之后，再执行ls命令即可查看当前目录中的所有文件并输出这些文件的属性信息。
如果想要查看目录属性信息，则需要额外添加一个-d参数。
```

## 文本文件编辑命令

- Linux "一切皆文件"

- `cat` 用于查看纯文本文件（内容较少的）。

`cat -n` 显示行号。

- `more` 用于查看纯文本文件。

`空格或回车` 翻页。

- `head` 用于查看纯文本文档的前 N 行。

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fss8lkq1gdj20ox09l40b.jpg)

- `tail` 用于查看纯文本文档的后 N 行或 __持续刷新内容__。

`持续刷新内容举例 tail -f test`:

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fss8psx4maj20ck03f0sp.jpg)

- `tr` 用于替换文本文件中的字符，`tr 「原始字符」 「目标字符」`

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fss8tg697pj20p60bggms.jpg)

- `wc` 用于统计指定文本的行数，字数，字节数。

参数列表：

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fss8ux1t2oj20j30410sv.jpg)

`wc -l /var/log/messages`

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fss8vcvzuqj20ci01cmx0.jpg)

- `stat` 用于查看文件的具体存储信息和时间等信息。

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fss8yt45lgj20jb07pjss.jpg)

- `cut` 用于按`列`提取文本字符。`-d`设置间隔符号，`-f`设置需要查看的列数，`-c`指定提取内容的字符串个数。

`head -10 /etc/shadow | cut -d: -f1`

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fss914jg97j20h70643yk.jpg)

`head -10 /etc/passwd | cut -c2-4`

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fss94hobe8j20en05o748.jpg)

- `diff` 用于比较多个文本文件的差异。

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fss9h6n8quj20fc0k6wgd.jpg)

## 文件目录管理命令

- `touch` 用于创建空白文件或设置文件的时间。

```
对touch命令来讲，有难度的操作主要是体现在设置文件内容的修改时间（mtime）、文件权限或属性的更改时间（ctime）与文件的读取时间（atime）
```

参数列表：

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsscr44ridj20jg049aae.jpg)

举例：

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fssd1zhp41j20hd05s74p.jpg)

- `mkdir` 用于创建空白的目录。

- `cp` 用于复制文件或目录。

参数列表：

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fssd3cvk3rj20kb090q55.jpg)

- `mv` 用于剪切文件或将文件重命名。

- `rm` 用于删除文件或目录。

- `dd` 用于按照指定大小和个数的数据块来复制文件或转换文件。

参数列表：

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fssd8sakwvj20ki04rdg8.jpg)

```
Linux系统中有一个名为/dev/zero的设备文件，这个文件不会占用系统存储空间，但却可以提供无穷无尽的数据，因此可以使用它作为dd命令的输入文件，来生成一个指定大小的文件。
```

例子：

`dd if=/dev/zero of=hh count=2 bs=20M` 总文件大小"2\*20M = 40M"

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fssdd0i6lij20ho045dg3.jpg)

- `file` 用于查看文件的类型。

举例：

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fssdfyt6luj20gc02jq2z.jpg)

## 打包压缩与搜索命令

- `tar` 用于对文件进行打包压缩或解压。

参数列表：

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fssdhvipz3j20k108ydgv.jpg)

```
首先，-c参数用于创建压缩文件，-x参数用于解压文件，因此这两个参数不能同时使用。其次，-z参数指定使用Gzip格式来压缩或解压文件，-j参数指定使用bzip2格式来压缩或解压文件。用户使用时则是根据文件的后缀来决定应使用何种格式参数进行解压。在执行某些压缩或解压操作时，可能需要花费数个小时，如果屏幕一直没有输出，您一方面不好判断打包的进度情况，另一方面也会怀疑电脑死机了，因此非常推荐使用-v参数向用户不断显示压缩或解压的过程。-C参数用于指定要解压到哪个指定的目录。

！！！（重要）
-f参数特别重要，它必须放到参数的最后一位，代表要压缩或解压的软件包名称。
```

- `grep` 用于在文本中执行关键词搜索，并显示匹配的结果。

参数列表：

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fssdmwsvbfj20j904gwev.jpg)

举例：

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fssdprmr4vj20nu0lo782.jpg)

- `find` 用于按照指定条件来查找文件。

参数列表：

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fssds70s8mj20j00fin00.jpg)

例子：

`find / -type f -name "*.conf" -exec stat -c "%s %n" {} \; | sort -nr | head -10`

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsseerskifj20ou0610tb.jpg)

```
其中的{}表示搜索出的每一个文件。
stat -c "%s %n" filename.
```

## 复习题

```
使用uptime命令查看系统负载时，对应的负载数值如果是0.91、0.56、0.32，那么最近15分钟内负载压力最大的是哪个时间段？
答：通过负载数值可以看出，最近1分钟内的负载压力是最大的。
```