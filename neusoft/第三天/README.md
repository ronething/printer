<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Day 3](#day-3)
  - [第 8 章 视图和索引](#%E7%AC%AC-8-%E7%AB%A0-%E8%A7%86%E5%9B%BE%E5%92%8C%E7%B4%A2%E5%BC%95)
  - [第 9 章 用户和权限管理](#%E7%AC%AC-9-%E7%AB%A0-%E7%94%A8%E6%88%B7%E5%92%8C%E6%9D%83%E9%99%90%E7%AE%A1%E7%90%86)
  - [第 10 章 表分区管理](#%E7%AC%AC-10-%E7%AB%A0-%E8%A1%A8%E5%88%86%E5%8C%BA%E7%AE%A1%E7%90%86)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Day 3

## 第 8 章 视图和索引

- 视图概述

```
视图是逻辑上来自一个或多个表的数据集合。
```

- 为什么使用视图

```
– 限制其它用户对数据库表的访问,因为视图可以有选择性的
显示数据库表的一部分;
– 容易实现复杂的查询;
– 对于相同的数据可以产生不同的视图;
```

- 视图分类

```
视图分为简单视图和复杂视图,最基本差别在DML操作上。
```

![](https://ws2.sinaimg.cn/large/006OWbT9gy1fsxk5qnen6j30j4076gmf.jpg
)

- 创建视图

```sql
CREATE [OR REPLACE] [ALGORITHM = {UNDEFINED | MERGE | TEMPTABLE}]
VIEW view_name [(column_list)]
AS select_statement
[WITH [CASCADED | LOCAL] CHECK OPTION]
```

```
OR REPLACE:如果所创建的视图已经存在,该选项表示修改原视图的定义;
view_name :视图的名称;
column_list :列名,列名的数量必须和视图所对应查询语句的列数量相等;
select_statement :一条完整的SELECT语句;
WITH CHECK OPTION:一个约束条件,通过视图所插入或修改的数据行必须满足视图所定义的查询;

ALGORITHM子句是可选的,它表示使用何种算法来处理视图。此外,它并不属于标准SQL的一部分,而是MySQL对标准SQL进行的功能扩展。ALGORITHM可以设置三个值:MERGE、TEMPTABLE或UNDEFINED。如果没有ALGORITHM子句,则默认值为
UNDEFINED(未定义的)。

• 对于MERGE,会将引用视图的语句的文本与视图定义合并起来,使得视图定义的某一部分取代语句的对应部分。
• 对于TEMPTABLE,视图的结果将被置于临时表中,然后使用它执行语句。
• 对于UNDEFINED,MySQL将选择所要使用的算法。如果可能,它倾向于MERGE而不是TEMPTABLE,这是因为MERGE通常更有效,而且如果使用了临时表,视图是不可更新的。
• [WITH [CASCADED | LOCAL] CHECK OPTION]是可选的。该选项中的CASCADED为默认值,LOCAL CHECK OPTION用于在可更新视图中防止插入或更新行,此选项一般不使用。
```

> 创建视图时,在子查询中使用列的别名

![](https://ws1.sinaimg.cn/large/006OWbT9gy1fsxs87euesj30jn05x3z0.jpg
)

> 创建复杂视图


```sql
-- 创建一个视图,通过该视图可以查询到工作在NEW YORK和CHICAGO的员工编号,姓名,部门编号,入职日期。

create view test as select e.empno,e.ename,e.deptno,e.hiradate from emp e,dept d where e.dpetno = d.deptno and d.loc='NEWYORK' or d.loc='CHICAGO';

-- 创建一个视图,通过该视图可以查询到每个部门的部门名称及最低工资。

create view test1 as select d.dname,min(e.sal) from emp e,dept d where e.deptno=d.deptno group by d.dname


-- 通过如上视图,查询每个部门工资最低的员工姓名及部门名称
```

- 索引简介

```
索引是一种特殊的数据库结构,可以用来快速查询数据库表中的特定记录。索引是提高数据库性能的重要方式。
MySQL中,所有的数据类型都可以被索引 。

– 索引的优点是可以提高检索数据的速度,这是创建索引的最主要的原因;对于有依赖关系的子表和父表之间的联合查询时,可以提高查询速度;使用分组和排序子句进行数据查询时,同样可以显著节省查询中分组和排序的时间。

– 索引的缺点是创建和维护索引需要耗费时间,耗费时间的数量随着数据量的增加而增加;索引需要占用物理空间,每一个索引要占一定的物理空间;增加、删除和修改数据时,要动态的维护索引,造成数据的维护速度降低了。
```

- 索引分类

```
普通索引
惟一性索引
全文索引
单列索引
多列索引
空间索引
```

- 创建索引

```
创建索引是指在某个表的一列或多列上建立一个索引,以便提高对表的访问速度。创建索引有三种方式,这三种方式分别是:
– 创建表的时候创建索引
– 在已经存在的表上创建索引
– 使用ALTER TABLE语句来创建索引
```

- 创建表的时候创建索引

```sql
CREATE TABLE 表名 ( 属性名 数据类型 [完整
性约束条件],
属性名 数据类型 [完整性约束条件],
...
属性名 数据类型
[UNIQUE | FULLTEXT | SPATIAL] INDEX | KEY
[别名](属性名1 [(长度)] [ASC | DESC])
);
```

- 全文索引

![](https://ws3.sinaimg.cn/large/006OWbT9gy1fsxot8elipj30js08zjsj.jpg
)

> 使用多列索引时一定要特别注意,只有使用了索引中的第一个字段时才会触发索引。如果没有使用索引中的第一个字段,那么这个多列索引就不会起作用。

- 用 ALTER TABLE 语句来创建索引

```sql
ALTER TABLE 表名 ADD [ UNIQUE |
FULLTEXT | SPATIAL ] INDEX
索引名(属性名 [ (长度) ] [ ASC | DESC]);
```

- 删除索引

```sql
DROP INDEX 索引名 ON 表名 ;
```

- 索引的设计原则

```
为了使索引的使用效率更高,在创建索引的时候
必须考虑在哪些字段上创建索引和创建什么类型
的索引。索引的设计原则如下:
选择惟一性索引
为经常需要排序、分组和联合操作的字段建立索引
为常作为查询条件的字段建立索引
限制索引的数目
尽量使用数据量少的索引
尽量使用前缀来索引
删除不再使用或者很少使用的索引
```

---

## 第 9 章 用户和权限管理

- 权限表

```
通过网络连接服务器的客户对MySQL数据库的访问由权限表内容来控制。这些表位于MySQL数据库中,并在第1次安装MySQL的过程中初始化。权限表共有6个表:user、db、host、tables_priv、columns_priv和procs_priv。

- `user` 表

user表是MySQL中最重要的一个权限表,记录允许连接到服务器的账号信息。user表列出可以连接服务器的用户及其口令,并且指定他们有哪种全局(超级用户)权限。在user表启用的任何权限均是全局权限,并适用于所有数据库。例如,如果用户启用了DELETE权限,则该用户可以从任何表中删除记录。

db表
中存储了用户对某个数据库的操作权限,决定用户能从哪个
主机存取哪个数据库。
– host表中存储了某个主机对数据库的操作权限,配合db权限
表对给定主机上数据库级操作权限做更细致的控制。

– tables_priv表用来对表设置操作权限
– columns_priv表用来对表的某一列设置权限
– procs_priv表可以对存储过程和存储函数设置操作权限
```

- `mysql` 访问控制分为两个阶段

    - 连接核实阶段
    - 请求核实阶段

- 工作原理

![](https://ws2.sinaimg.cn/large/006OWbT9gy1fsxmlucpq1j30ie0audgt.jpg
)

- 账户管理

- `create user`创建新用户

```sql
– 使用CREATE USER语句创建新用户。

• 执行CREATE USER或GRANT语句时,服务器会有相应的用户权限表,添加或修改用户及其权限。

• CREATE USER语句的基本语法格式如下。

CREATE USER user[IDENTIFIED BY [PASSWORD]'password'][,user[IDENTIFIED BY [PASSWORD]'password']][,...];
```

- `grant` 创建新用户

```sql
• GRANT语句不仅可创建新用户,还可以在创建的同时对用户授权。GRANT语句还可以指定用户的其他特点,如安全连接、限制使用服务器资源等。使用GRANT语句创建新用户时必须有GRANT权限。
• 其基本语法格式如下。

GRANT priv_type ON database.table TO user [IDENTIFIED BY [PASSWORD] 'password'][, user [IDENTIFIED BY [PASSWORD] 'password']]
[,...]
[WITH GRANT OPTION];
```

- 删除账户

```
DROP USER user_name[, user_name] [,...];

DROP USER 语句用于删除一个卓多个 mysql 账户。

要使用 DROP USER,必须拥有 MySQL 数据库的全局 CREATE USER 权限或 DELETE 权限
```

- 修改用户名

```sql
RENAME USER old_user TO new_user,[, old_user TO new_user] [,...];
```

- 修改密码

```sql
alter user username identified by 'password';

# set 修改（旧版本使用？）

set password [for user]=password("newpassword");

# 修改 root 密码

set password = password("123456");

# root 修改自己的密码(直接修改mysql.user表的数据 个人不是很建议)

update mysql.user set authentication_string=password('helloworld') where user='root'
```

- 授权

> 授权就是为某个用户授予权限。

- 权限的级别

    - 全局层级
    - 数据库层级
    - 子程序层级
    - 表层级
    - 列层级

> 在MySQL中,必须是拥有GRANT权限的用户才可以执行GRANT。

```sql
GRANT priv_type [(column_list)] [,priv_type
[(column_list)]] [,...n]
ON
{table_name|*|*.*|database_name.*|database_name.ta
ble_name}
TO user[IDENTIFIED BY [PASSWORD] 'password']
[,user[IDENTIFIED BY [PASSWORD] 'password']]
[,...n]
[WITH GRANT OPTION];
```

示例：

![](https://ws4.sinaimg.cn/large/006OWbT9gy1fsxo8hv7xbj30jt084ta4.jpg
)

```sql
mysql中只有with grant option，对A用户进行的授权，A可以授予给其他用户，当收回对A的授权时，A授予给其他用户的权限不会被级联收回。注意with grant option也可以被授予给其他用户。
```

- 授权列

```sql
-- 使用GRANT语句将mysqldb数据库中Departments表的DepId列的UPDATE权限授予用户grantUser。

mysql> grant update(DepId) on mysqldb.Departments to grantUser@localhost;
```

- 收回权限

```sql
# 收回所有权限。

REVOKE ALL PRIVILEGES,GRANT OPTION
FROM
'username'@'hostname'[,'username'@'hostname'][,...n
];

# 收回指定权限

REVOKE priv_type [(column_list)] [,priv_type
[(column_list)]] [,...n]
ON
{table_name|*|*.*|database_name.*|database_name.ta
ble_name}
FROM
'username'@'hostname'[,'username'@'hostname'][,...n
];

```

- 查看权限

```sql
SHOW GRANTS FOR 'username'@'hostname';
```

---

## 第 10 章 表分区管理

- 表分区

```
– 表分区通俗来讲就是允许把一个数据表根据一定的规则,跨文件系统划分成多个可以设置为任意大小的部分。
```

- 通过下面语句来查看本机 MySQL 是否支持分区:

```sql
show variables like '%partition%';
```

- 表为什么要分区

```
– 当表中的数据量不断增大,查询数据的速度就会变慢,应用程序的性能就会下降,这时就应该考虑对表进行分区。
– 表进行分区后,逻辑上表仍然是一张完整的表,只是将表中的数据在物理上存放到多个表空间(物理文件上),这样查询数据时,不至于每次都扫描整张表。
```

- 分区类型

```
– RANGE分区
– LIST分区
– COLUMNS分区
– HASH分区
– KEY分区
```

- RANGE 分区

```sql
– range 分区基于属于一个给定连续区间的列值进行分配
create table employees (
    id int not null,
    fname varchar(30),
    lname varchar(30),
    hired date not null default '1970-01-01',
    separated date not null default '9999-12-31',
    job_code int not null,
    store_id int not null
)
    partition by range (store_id) (
    partition p0 values less than (6),
    partition p1 values less than (11),
    partition p2 values less than (16),
    partition p3 values less than maxvalue
);
```

- LIST 分区

```sql
– list 分区类似range分区,它们的主要区别在于,list分区
中每个分区的定义和选择是基于某列的值从属于一个集合,
而range分区是从属于一个连续区间值的集合
create table employees (
    id int not null,
    fname varchar(30),
    lname varchar(30),
    hired date not null default '1970-01-01',
    separated date not null default '9999-12-31',
    job_code int,
    store_id int
)
    partition by list(store_id)
    partition pnorth values in (3,5,6,9,17),
    partition peast values in (1,2,10,11,19,20),
    partition pwest values in (4,12,13,14,18),
    partition pcentral values in (7,8,15,16)
);
```

- COLUMNS 分区

```
– columns分区是range分区或list分区的一种变体,支持非整形字段作为分区的键,也可以用多个字段组合起来作为分区的键
• columns分区可允许使用的分区键类型有:
– 所有的整形:tinyint, smallint, mediumint, int ,bigint (和range分区和list分区相同),不包括decimal和float这种数字类型的。
– date 和 datetime
– 字符型:chra, varchar, binary, varbinary,不包括text和blob型
```

- HASH 分区

```
HASH分区
– 要使用hash分区来分割一个表,要在create table 语句上添加一个“partition by hash (expr)”子句,其中“expr”是一个返回一个整数的表达式。它可以仅仅是字段类型为MySQL 整型的一列的名字。此外,需要在后面再添加一个“partitions num”子句,其中num 是一个非负的整数,它表示表将要被分割成分区的数量。
– 如果没有包括一PARTITIONS子句,那么分区的数量将默认
为1
– 如果在关键字“PARTITIONS”后面没有加上分区的数量,将
会出现语法错误。
```

示例：

```sql
create table employees (
    id int not null,
    fname varchar(30),
    lname varchar(30),
    hired date not null default '1970-01-01',
    separated date not null default '9999-12-31',
    job_code int,
    store_id int
)
    partition by hash(year(hired))
    partitions 4;
```

- KEY 分区

```sql
– key 分区按照key进行分区类似于按照hash分区,除了hash
分区使用的用户定义的表达式,而key分区的哈希函数是由
MySQL 服务器提供。
create table tk (
    col1 int not null,
    col2 char(5),
    col3 date
)
    partition by linear key (col1)
    partitions 3;
```

- 分区管理 -- range 分区和 list 分区

- 添加分区

```sql
• 添加分区
– 要增加一个新的RANGE或LIST分区到一个前面已经分区了的
表,使用“ALTER TABLE ... ADD PARTITION”语句。
• 例如有一个组织的全体成员数据的分区表,该表的定义如下:

create table members(
    id int,
    fname varchar(25),
    lname varchar(25),
    dob date
)
partition by range(year(dob))
(
    partition p0 values less than (1970),
    partition p1 values less than (1980),
    partition p2 values less than (1990)
);


• 添加分区
• 假设成员的最小年纪是16岁。随着日历接近2005年年底,要接纳1990年(以及以后年份)出生的成员。可以按照下面的方式,修改成员表来容纳出生在1990-1999年之间的成员:
alter table add partition (partition p3 values less than (2000));
• 对于通过RANGE分区的表,只可以使用ADD PARTITION添加新的分区到分区列表的高端。设法通过这种方式在现有分区的前面或之间增加一个新的分区,将会导致下面的一个错误:
alter table add partition (partition p3 values less
than (1960));
```

```sql
类似的可以增加新的分区到已经通过list分区的表。例如,假
定有如下定义的一个表:
create table tt(
    id int,
    data int
)
partition by list(data)
(
    partition p0 values in (5, 10, 15),
    partition p1 values in (6, 12, 18)
);


• 添加分区
• 可以通过下面的方法添加一个新的分区,用来保存拥有数据列值7,14和21的行:
alter table tt add partition (partition p2 values in (7, 14, 21));
• 注意:不能添加这样一个新的LIST分区,该分区包含有已经包含在现有分区值列表中的任意值。如果试图这样做,将会导致错误:
alter table tt add partition (partition np values in
(4, 8, 12));
```

- 修改分区

```sql
- 使用"reorganize partition"拆分或合并分区,没有数据丢失。在执行上面的语句中,MySQL 把保存在分区s0和s1中的所有数据都移到分区p0中。

- “reorganize partition”的基本语法是:
alter table tbl_name reorganize partition
partition_list into (partition_definitions);
```

```sql
-- 修改分区
alter table members reorganize partition p0 into(
partition s0 values less than (1960),
partition s1 values less than (1970)
);
• alter table members reorganize partition s0,s1 into(
partition p0 values less than (1970)
);
• alter table members reorganize partition p0,p1,p2,p3
into (
partition m0 values less than (1980),
partition m1 values less than (2000)
);
alter table tt reorganize partition p1,np into(
partition p1 values in (6, 18),
partition np values in (4, 8, 12)
);
```

> 修改`range`和`list`分区注意事项

![](https://ws2.sinaimg.cn/large/006OWbT9gy1fsxvrcc71lj30k107jabw.jpg)

![](https://ws1.sinaimg.cn/large/006OWbT9gy1fsxvrd7unvj30jm0a2ju5.jpg)

- 删除分区

```sql
– 从一个按照range或list分区的表中删除一个分区,可以使
用带一个drop partition子句的alter table命令来实现:
• 例如删除分区:
alter table tr drop partition p2;
```

---

- 分区管理 -- HASH 分区和 
KEY 分区

```sql
create table clients (
    id int,
    fname varchar(30),
    lname varchar(30),
    signed date
)
    partition by hash(month(signed)) 
    partitions 12;
```

```sql
不能使用与从按照range或list分区的表中删除分区相同的方式
来从hash或key分区的表中删除分区。但是,可以使用“alter
table ... coalesce partition”命令来合并hash或key分区。

oalesce不能用来增加分区的数量,要增加顾客表的分区数量从
12到18,使用“alter table ... add partition”,具体如下:
alter table clients add partition partitions 6;（相当于12+6）
•
要减少分区的数量从12到6,执行下面的ALTER TABLE命令:
alter table clients coalesce partition 6;（相当于12-6）
```

```
对于按照HASH,KEY,LINEAR HASH,或LINEAR KEY分区的表,COALESCE能起到同样的作用。
```

```sql
改变分区的方式
alter table tablename partition by hash(id) partitions 2;
重建分区
alter table t1 rebuild partition p0, p1;
优化分区:
alter table t1 optimize partition p0, p1;
分析分区
alter table t1 analyze partition p3;
修护分区:
alter table t1 repair partition p0,p1;
检查分区:
alter table t1 check partition p1;
```

- 分区的局限性

```sql
关于Partitioning Keys, Primary Keys, and Unique Keys的限制
– 在 mysql@5.1 中分区表对唯一约束有明确的规定,每一个唯一约束必须包含在分区表的分区键(也包括主键约束)。( 表中只能有一个有唯一标识的列)

• 例如:
create table t1(
    id int not null,
    uid int not null,
    primary key (id),
    unique key (uid)
)
partition by range (id)
(
    partition p0 values less than(5),
    partition p1 values less than(10)
);
• ERROR 1503 (HY000): A UNIQUE INDEX must include all
columns in the table's partitioning function
```

```sql
• 关于函数的限制
在建立分区表的语句中,只能包含例如ABS() 、CEILING()
、FLOOR() 、DAY() 、HOUR() 、MINUTE() 、MOD() 、
MONTH() 、QUARTER() 、SECOND() 、TO_DAYS() 、
YEAR()等返回整型的函数。
• 分区键必须是INT类型,或者通过表达式返回INT类型,可以为
NULL。唯一的例外是当分区类型为KEY分区的时候,可以使用其
他类型的列作为分区键( BLOB or TEXT 列除外)。
create table tkc (c1 char)
partition by key(c1)
partitions 4;
query ok, 0 rows affected (0.00 sec)
```

```
• 运算限制
– 支持加减乘等运算出现在分区表达式,但是运算后的结果必须是一个INT或者NULL。 |, &, ^, <<, >>, , ~ 等不允许出现在分区表达式。
• 最多支持1024个分区,包括子分区。
– 当你建立分区表包含很多分区但没有超过1024限制的时候,如果报错 Got error 24 from storage engine,那意味着你需要增大open_files_limit参数。
```

