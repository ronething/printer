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




