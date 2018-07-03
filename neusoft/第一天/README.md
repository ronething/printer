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

