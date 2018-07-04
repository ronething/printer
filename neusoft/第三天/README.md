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

