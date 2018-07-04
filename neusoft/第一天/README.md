# Day 1

## 第 1 章 数据库基础

```sql
where 1=0; 这个条件始终为false，结果不会返回任何数据，只有表结构，可用于快速建表

SELECT * FROM strName WHERE 1 = 0; 该 select 语句主要用于读取表的结构而不考虑表中的数据，这样节省了内存，因为可以不用保存结果集。

create table newtable as select * from oldtable where 1=0; 
创建一个新表，而新表的结构与查询的表的结构是一样的。
```

---

- 数据库基础概述

```
– 数据库（DB）是一种专门存储信息和维护信息的容器，严格
地说数据库是“按照数据结构来组织、存储和管理信息的仓
库”。
– 数据库管理系统（Database Management System－DBMS）管
理数据库的软件。具有对数据存储、安全、一致性、并发操
作、恢复和访问等功能。
– 数据词典（系统目录），也是一种数据，只不过这些数据记
录的是数据库中存放的各种对象的定义信息和其他一些辅助
管理信息，包括名字、结构、位置、类型等。这些数据被称
为元数据（metadata）。
```

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsx2puftmlj20oc0gimzd.jpg)

- 数据管理主要经历过程

```
– 手工管理阶段：应用程序管理数据、数据不保存、不共享、
不具有独立性。
– 文件管理阶段：文件系统管理数据、数据可长期保存、但
共享性差、冗余度大、独立性差。
– 数据管理阶段：数据库系统管理数据、数据结构复杂、冗余
小、易扩充、较高的独立性、统一数据控制。
```

- 数据库类型

    - 按数据模型特点分：

        - 网状型数据库

        ![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsx2taie7fj20mn0c40t3.jpg)

        - 层次型数据库

        ![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsx2tkl9p3j20lq0bbt9a.jpg)

        - 关系型数据库

        ![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsx2ttzkvhj20mt08omyk.jpg)


- 关系型数据库管理系统（RDBMS）

---

- mysql 数据库操作

```sql
# 查看具体的表结构
desc user;

# 查看MySQL服务实例支持的存储引擎
show engines;
```

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsx2zghhq8j21cm094wfa.jpg)

- mysql 字符集

所有这些字符和编码对组成的集合就是字符集(Character Set)

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsx329cfn5j20m70co78w.jpg)

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsx32opylgj20m707omzs.jpg)

- 修改字符集操作

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsx36fg2srj20n803ojs1.jpg)

- 导入 sql 脚本

`source init.sql`

---

## 第 2 章 数据库和数据表管理

- 创建数据库

`create database [if not exists] 数据库名 [default charset utf8];`

- 显示创建的数据库的相关信息（包括MySQL版本ID号、默认字符集等信息）。

`show create database 数据库名;`

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsx3cvi6c8j20u204c74a.jpg)

- 删除数据库

`drop database 数据库名`

---

- 数据库表的设计

- er图

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsx3erjt9gj20mb0cuacy.jpg)

- 主键（primary key）

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsx3fir81gj20mf0at0w5.jpg)

- 实体间的关系与外键

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsx3i0og35j20o50cc785.jpg)

- 约束

当为某个表定义约束后，对该表做的所有SQL操作都必须满足约束的规则要求，否则操作将失败。

  - 约束类型

    ![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsx3iv78z3j20kr0aljte.jpg)

- mysql 表的字段的数据类型

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsx3k6tpokj20ls0ajmxy.jpg)

- 数值类型

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsx3ltr7lqj20n20cm77n.jpg)

- 日期和时间类型

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsx3l6042lj20mc0a8dh9.jpg)

- 字符串类型

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsx3mawf19j20m20d0n0b.jpg)

- 特殊字符

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsx3mxp645j20go0bqt9m.jpg)

- 创建表

```sql
create table 表名(
字段名1 数据类型[约束条件],
…
[其他约束条件],
[其他约束条件]
)其他选项（例如存储引擎、字符集等选项）

•PRIMARY KEY，指定字段为主键。
•AUTO_INCREMENT，指定字段为自动增加字段。
•INDEX，为字段创建索引。
•NOT NULL，字段值不允许为空。
•NULL，字段值可以为空。
•COMMENT，设置字段的注释信息。
•DEFAULT，设置字段的默认值。
```

- 复制表

```sql
create table 新表名like 源表

or

create table 新表名select * from 源表 where 1=0;

create table 新表名select * from 源表 where 1=1;
```

- 删除表

`DROP TABLE 表名`

- 修改表

```sql
•可以使用 ALTER TABLE 语句修改表的结构，包括添加列、修改列属性和删除列等操作。

•ALTER TABLE 表名 ADD 列名数据类型和长度列属性
•ALTER TABLE 表名 MODIFY 列名新数据类型和长度新列属性
•ALTER TABLE 表名 DROP COLUMN 列名
```

- 修改约束条件

```sql
# 添加约束条件
alter table 表名 add constraint 约束名 约束类型(字段名)

# 删除约束条件
alter table 表名 drop primary key
alter table 表名 drop foreign key 约束名

```

- 修改表存储引擎

```sql
•alter table 表名 engine=新的存储引擎类型
•alter table 表名 default charset=新的字符集
•alter table 表名auto_increment=新的初始值
•alter table 表名 pack_keys=新的压缩类型
```

- 修改表名

```sql
rename table 旧表名 to 新表名

or

alter table 旧表名 rename 新表名
```

---

## 第 3 章 数据操作与事务控制

- 数据操作语言

```
–Data Manipulation Language ,简称DML，主要用来实现对数据库表中的数据进行操作。
–数据操作语言主要包括如下几种：
•增加行数据：使用INSERT语句实现
•修改行数据：使用UPDATE语句实现
•删除行数据：使用DELETE语句实现
```

- 插入数据

`INSERT INTO table [(column [, column...])]
VALUES (value [, value...]);`

> 采用这种语法一次只能追加一条记录。字符和日期型数据必须要用单引号括起来。

- 插入 NULL

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsx49psfa6j20m90cpt9z.jpg)

- 插入日期值

> sysdate(),now() 记录当前日期和时间。

> format: '1997-02-03'

- 批量插入数据

```sql
INSERT INTO 表名 [( 字段列表 )] VALUES
( 值列表 1),
( 值列表 2),
...
( 值列表 n);
```

- 通过子查询插入多行数据

```sql
INSERT INTO 表名 [( 列名 1[, 列名 2 , ... ,列名 n])] 子查询 ;

-- 不必书写values子句
-- INSERT子句和数据类型必须和子查询中列的数量和类型相匹配中列的数量
```

- 修改数据

```sql
-- 通过 update 实现修改

UPDATE table SET column = value [,column = value] [WHERE condition];
```

| 关系运算符和比较函数 | 功能函数 | 
| - | :-: | 
= |等于,例如a=1
<=> |与=相同,但如果操作符两边的操作数都是NULL,则表达式返回1,而不是NULL;而当只有一个操作数为NULL时,其所得值为0而不为NULL
!= | 不等于,例如a!=1
<> | 与!=相同,例如a<>1
<= | 小于或等于,例如a<=1
< | 小于,例如a<1
\>= | 大于或等于,例如a>=1
\> | 大于,例如a>1
IS NULL | 判断指定的值是否为NULL,例如a IS NULL
IS NOT NULL | 判断指定的值是否不为NULL,例如a IS NOT NULL
BETWEEN...AND | 判断操作数是否在指定的范围之间,例如a BETWEEN 1 AND 100
NOT BETWEEN...AND | 判断操作数是否不在指定的范围之间,例如a NOT BETWEEN 1 AND 100
COALESCE | 返回列表中第一个非NULL的值,如果没有非NULL值,则返回NULL。例如COALESCE(NULL,NULL, 1, 2)的结果为1
GREATEST | 当参数列表中有两个或多个值,则返回其中最大的值。例如,GREATEST(1,2,3)的结果为3
IN | 判断表达式是否为列表中的一个值,例如a IN (1,2,3,4),如果a为1,2,3或4,则表达式返回True,否则返回False
NOT IN | 判断表达式是否为列表中的一个值,例如a NOT IN (1,2,3,4),如果a为1,2,3或4,则表达式返回False,否则返回True
ISNULL(expr) | 判断指定的表达式是否为NULL
LEAST | 当参数列表中有两个或多个值,则返回其中最小的值。例如,LEAST (1,2,3)的结果为1

|关系运算符|功能描述|
|:-|:-|
NOT | 逻辑非。当操作数为0时结果为1;当操作数为1时结果为0 
! | 与NOT相同
AND | 逻辑与。例如a AND b,如果a和b都等于True时,则返回True,否则返回False
&& | 与AND相同
OR | 逻辑非。例如a OR b,如果a和b中有一个等于True时,返回True,否则返回False
\|\| | 与OR相同 
XOR | 逻辑异或。例如a XOR b 的计算等同于(a AND (NOT b)) OR ((NOT a) AND b)

- 删除数据

```sql
DELETE FROM table [WHERE condition];
```

- 截断表

```sql
TRUNCATE TABLE table;
```

- TRUNCATE 和 DELETE 区别

```
– TRUNCATE是DDL,只能删除表中所有记录,释放存储空间,
使用ROLLBACK不可以回滚。
– DELETE是DML,可以删除指定记录,不释放存储空间,使用
ROLLBACK可以回滚。
```

- 事务管理

```
– 事务:也称工作单元,是由一个或多个SQL语句所组成的操
作序列,这些SQL语句作为一个完整的工作单元,要么全部
执行成功,要么全部执行失败。在数据库中,通过事务来
保证数据的一致性。
– 事务处理语言:Transaction Process Language ,简称TPL,
主要用来对组成事务的DML语句的操作结果进行确认或取消。
确认也就是使DML操作生效,使用提交(COMMIT)命令实现;
取消也就是使DML操作失效,使用回滚(ROLLBACK)命令实现。
– 通过事务的使用,能防止数据库中出现数据不一致现象。
如两个银行账户进行转账,涉及到两条更新操作,这两条
更新操作只允许全部成功或失败,否则数据会出现不一致
的现象。
```

- 事务组成

```
在数据库中,事务由一组相关的DML或SELECT语句,加上一
个TPL语句(COMMIT、ROLLBACK)或一个DDL语句(CREATE、
ALTER、DROP、TRUNCATE等)或一个DCL(GRANT、REVOKE)
语句。
```

示例：

```sql
• INSERT....
• UPDATE....
• DELETE....
• SELECT....
• INSERT...
• COMMIT; -- 前6条语句,组成第1个事务
• UPDATE...
• DELETE....
• CREATE... ; --后3条语句,组成第2个事务
```

- 事务特征 ACID

    - 原子性(Atomicity)

    事务就像“原子”一样,不可被分割,组成事务的DML操作语句要么全成功,要么全失败,不可能出现部分成功部分失败的情况。

    - 一致性(Consistency)

    一旦事务完成,不管是成功的,还是失败的,整个系统处于数据一致的状态。

    - 隔离性(Isolation)

    一个事务的执行不会被另一个事务所干扰。比如两个人同时从一个账户从取钱,通过事务的隔离性确保账户余额的正确性。

    - 持久性(Durability)

    也称为永久性,指事务一旦提交,对数据的改变就是永久的,不可以再被回滚。

- MySQL的事务处理的两种方法

```sql
1.用begin,rollback,commit来实现
begin开始一个事务
rollback事务回滚
commit 事务提交
2.直接用set来改变MySQL的自动提交模式
MySQL默认是自动提交的,也就是你提交一个sql,就直接执行!可以通过
set autocommit = 0 禁止自动提交
set autocommit = 1 开启自动提交
来实现事务的处理。
• 但要注意当用set autocommit = 0 的时候,以后所有的sql都
将作为事务处理,直到用commit确认或 rollback结束,注意
当结束这个事务的同时也开启了新的事务!按第一种方法只将当前的做为一个事务!
```

- 隐式结束

```sql
– 隐式提交:当下列任意一种情况发生时,会发生隐式提交
• 执行一个DDL(CREATE、ALTER、DROP、TRUNCATE、RENAME)语句;
• 执行一个DCL(GRANT、REVOKE)语句;
– 隐式回滚:当下列任意一种情况发生时,会发生隐式回滚
• 客户端强行退出
• 客户端连接到服务器端异常中断
• 系统崩溃
```

> 如果在一个事务内,想要回滚到指
定位置,不是回滚到事务的起始点,可以通过保存点(SAVEPOINT)来实现。

```sql
– SAVEPOINT savepointname ;--定义一个保存点语句;
– ROLLBACK TO savepointname ;--回滚到指定保存点
– 注意:如上两条语句不结束事务的执行。
```

示例：

![](https://ws4.sinaimg.cn/large/006OWbT9gy1fsxr2iyontj30kg0a040x.jpg
)

---

## 第 4 章 简单查询

- 结构化查询语言

```
结构化查询语言(Structured Query Language)简称SQL,
是操作和检索关系型数据库的标准语言,20世纪70年代由
IBM公司开发,目前应用于各种关系型数据库。
```

- 结构化查询语言分类

```
- 数据查询语言(DQL:Data Query Language):语句主要包括SELECT,用于从表中检索数据。
- 数据操作语言(DML:Data Manipulation Language):语句主要包括INSERT,UPDATE和DELETE,用于添加,修改和删除表中的行数据。
- 事务处理语言(TPL:Transaction Process Language): 语句主要包括COMMIT和ROLLBACK,用于提交和回滚。
- 数据控制语言(DCL:Data Control Language):语句主要包括GRANT和REVOKE,用于进行授权和收回权限。
- 数据定义语言(DDL:Data Definition Language):语句主要包括CREATE、DROP、ALTER,用于定义、销毁、修改数据库对象。
```

- 基本 SELECT 语句

```sql
SELECT [DISTINCT]{*|column|expression [alias],...} FROM table;
```

- SQL 语句相关概念

```sql
– 关键字(Keyword):SQL语言保留的字符串,例如,SELECT和FROM都是关键字。
– 语句(statement):一条完整的SQL命令。例如,SELECT * FROM dept 是一条语句。
– 子句(clause):部分的SQL语句,通常是由关键字加上其它语法元素构成,例如,SELECT * 是一个子句,FROM table也是一个子句。
```

- 算数运算符

> 可以在SELECT语句中使用算术运算符,改变输出结果。

|运算符|描述|
|:-|:-|
+|加
-|减
*|乘
/|除

- 空值 NULL

> 空值是指一种无效的、未赋值、未知的或不可用的值。空值不同于零或者空格。

> 任何包含空值的算术表达式运算后的结果都为空值 NULL。

- 列别名

```
• 列别名
– 用来重新命名列的显示标题
– 如果SELECT语句中包含计算列,通常使用列别名来重新定义列标题。
• 使用列别名的方法
– 方式1:列名 列别名
– 方式2:列名 AS 列别名
• 以下三种情况列别名两侧需要添加双引号
– 列别名中包含有空格
– 列别名中要求区分大小写
– 列别名中包含有特殊字符
```

- 消除重复行

> 在SELECT字句中使用关键字DISTINCT可消除重复行。

- 显示表的结构

> 可以使用 DESCRIBE or DESC 命令来查看表结构。

|操作符|含义|
|:-|:-|
= | 等于
\> | 大于
\>= | 大于或等于
< | 小于
<= | 小于或等于
<> | 不等于

- 特殊比较运算符

![](https://ws2.sinaimg.cn/large/006OWbT9gy1fsxro8azmdj30id098dgu.jpg
)

- 逻辑运算符

![](https://ws2.sinaimg.cn/large/006OWbT9gy1fsxrr8f4p6j30j50720tg.jpg
)

- ORDER BY 子句

```sql
SELECT [DISTINCT] { * | 列名 | 表达式 [ 别名 ][,...]}
FROM 表名 [WHERE 条件 ]
 [ORDER BY { 列名 | 表达式 | 列别名 | 列序号 } [ASC|DESC],...];
```

> ASC: 升序,默认值 DESC: 降序

> ORDER BY 子句必须写在SELECT语句的最后

- 排序规则

![](https://ws1.sinaimg.cn/large/006OWbT9gy1fsxrtp8smnj30it071wfo.jpg
)

- 限制记录的行数 `limit`

```sql
select 字段列表 from 数据源 limit [start,]length;
```

> 1.limit接受一个或两个整数参数。start表示从第几行记录开始输
出,length表示输出的记录行数。

> 2.表中第一行记录的start值为0(不是 1) 。

