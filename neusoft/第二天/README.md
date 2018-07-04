# Day 2

## 第 5 章 常用函数

- mysql 函数概述

- 单行函数

```sql
-- 语法

函数名[(参数1,参数2,...)]
– 其中的参数可以是以下之一:
• 变量
• 列名
• 表达式

-- 特征

– 单行函数对单行操作
– 每行返回一个结果
– 有可能返回值与原参数数据类型不一致
– 单行函数可以写在SELECT、WHERE、ORDER BY子句中
– 有些函数没有参数,有些函数包括一个或多个参数
– 函数可以嵌套
```

- 常用函数分类

```
– 数学函数
– 字符串函数
– 日期和时间函数
– 流程控制函数
– 其他函数
```

- 数学函数

```sql
ABS(x):返回x的绝对值;
SQRT(x):返回非负数x的平方根;
PI():返回圆周率;
MOD(x,y)或%:返回x被y除的余数;
CEIL(x)、CEILING(x):返回大于或者等于x的最小整数值;
FLOOR(x):返回小于或者等于x的最大整数值;
ROUND(x,y):返回保留小数点后面y位,四舍五入的整数;
TRUNCATE(x,y):返回被舍弃的小数点后y位的数字x;
RAND():每次产生不同的随机数;
SIGN(x):返回参数的符号;
POW(x,y)和POWER(x,y): 返回x的y次乘方的结果值;
EXP(x):返回以e为底的x乘方后的值;
LOG(x):返回x的自然对数,x相对于基数e的对数;
LOG10(x):返回x的基数为10的对数;
RADIANS(x):将参数x由角度转化为弧度;
DEGREES(x):将参数x由弧度转化为度。
SIN(x):返回x正弦,其中x为弧度值;
ASIN(x)返回x的反正弦,即正弦为x的值;
COS(x):返回x的余弦;
ACOS(x):返回x反余弦
TAN(x):返回x的正切;
ATAN(x)返回x的反正切;
```

- 字符串函数

```sql
CHAR_LENGTH(str):返回字符串str的所包含字符个数;
LENGTH(str):返回字符串str的长度;
CONCAT(s1,s2,...): 字符串连接;
CONCAT_WS(x,s1,s2,...):字符串连接, x是其它参数的分隔符;
INSERT(s1,x,len,s2) :返回字符串s1,s1中插入字符串s2;
LOWER (str)|LCASE (str):将字符串全部转换成小写字母;
UPPER(str)|UCASE(str):将字符串全部转换成大写字母;
LEFT(s,n):返回最左边指定长度的字符;
RIGHT(s,n):返回最右边指定长度的字符;
LPAD(s1,len,s2)| RPAD(s1,len,s2) :填充字符串函数;
TRIM(s1 FROM s)|LTRIM(s)|RTRIM(s):删除空格函数;
REPEAT(s,n):重复生成字符串函数;
SPACE(n):返回一个由n个空格组成的字符串;
REPLACE(s,s1,s2):字符串替换函数;
STRCMP(s1,s2):比较字符串大小函数;
SUBSTRING(s,n,len):获取子串函数;
LOCATE(str1,str)|POSITION(str1 IN str)|INSTR(str, str1):
匹配子串开始位置函数;
REVERSE(s):将字符串s反转;
ELT(N,字符串1,字符串2,字符串3,...):返回指定位置函数;
```

- 日期和时间函数

```sql
CURDATE()和CURRENT_DATE() :获取当前日期函数;
NOW():返回服务器的当前日期和时间;
CURTIME():返回当前时间,只包含时分秒;
UTC_DATE():返回世界标准时间日期函数;
UTC_TIME():返回世界标准时间函数;
TIMEDIFF(expr1, expr2):返回两个日期相减相差的时间数;
DATEDIFF(expr1, expr2):返回两个日期相减相差的天数;
DATE_ADD(date,INTERVAL expr type):日期加上一个时间间隔值;
DATE_SUB(date,INTERVAL expr type):日期减去一个时间间隔值;
DATE(date)、TIME(date)、YEAR(date):选取日期时间的各个部分:
EXTRACT(unit FROM date):从日期中抽取出某个单独的部分或组合;
DAYOFWEEK(date) 、DAYOFMONTH(date) 、DAYOFYEAR(date):返回日期在一周、一月、一年中是第几天
DAYNAME、MONTHNAME:返回日期的星期和月份名称;
DATE_FORMAT(date,format):格式化日期;
TIME_FORMATE(time,formate):格式化时间;
```

- 流程控制函数

```sql
-- 常见的控制流程函数如下:

– CASE
– IF
– IFNULL
– NULLIF


• CASE value WHEN [compare-value] THEN result [WHEN
[compare-value] THEN result ...] [ELSE result] END
• CASE WHEN [condition] THEN result [WHEN [condition] THEN
result ...] [ELSE result] END
• 在第一个方案的返回结果中, value=compare-value。
• 而第二个方案的返回结果是第一种情况的真实结果。如果没有匹配
的结果值,则返回结果为ELSE后的结果,如果没有ELSE 部分,则
返回值为 NULL。
•
SELECT CASE 11 WHEN 1 THEN 'one'
WHEN 2 THEN 'two' ELSE 'more' END; （相当于赋值11进去判断）
• SELECT CASE WHEN 1>0 THEN 'true' ELSE 'false' END;（直接在when判断(1>0)）

-- IF

• IF(expr1,expr2,expr3)
– 如果 expr1 是TRUE (expr1 <> 0 and expr1 <> NULL),
则 IF()的返回值为expr2; 否则返回值则为 expr3。
– IF() 的返回值为数字值或字符串值,具体情况视其所在语
境而定。
•
• SELECT IF(1>2,2,3);
SELECT IF(1<2,'yes ','no');

-- IFNULL

IFNULL(expr1,expr2)|NULLIF(expr1,expr2)
– 假如expr1 不为NULL ,则IFNULL() 的返回值为expr1 ; 否则
其返回值为expr2。
– IFNULL() 的返回值是数字或是字符串,具体情况取决于其所使
用的语境

```

- 其他函数

```
Database():返回使用utf8 字符集的默认( 当前) 数据库名
Version():返回指示MySQL 服务器版本的字符串
User():返回当前MySQL 用户名和机主名
Inet_aton(ip):给出一个作为字符串的网络地址的点地址表示,
返回一个代表该地址数值的整数
Inet_ntoa(num):给定一个数字网络地址, 返回作为字符串的该地址的点地址表示。
Password(str):从原文密码str 计算并返回密码字符串,当参数为NULL 时返回NULL。
Md5():为字符串算出一个MD5 128 比特检查和。
```

---

## 第 6 章 多表连接查询

> 连接:连接是在多个表之间通过一定的连接条件,使表
之间发生关联,进而能从多个表之间获取数据。

```sql
SELECT table1.column, table2.column FROM table1, table2 WHERE table1.column1 = table2.column2;
```

```
– 如果在多个表中出现相同的列名,则需要使用表名作为来自该表的列名的前缀。
– N个表相连时,至少需要N-1个连接条件。
```

- 连接类型

![](https://ws2.sinaimg.cn/large/006OWbT9gy1fsxx3q9f06j30fw0ad0tf.jpg
)

- 笛卡尔积

```sql
SELECT emp.empno,
emp.ename, emp.deptno,
dept.deptno, dept.loc FROM emp, dept;

-- 为了避免笛卡尔积的产生,通常需要在WHERE子句中包含一个有效的连接条件。
```

- 等值连接

```sql
SELECT emp.empno,
emp.ename, emp.deptno,
dept.deptno, dept.loc FROM emp, dept WHERE emp.deptno=dept.deptno;
```

- 非等值连接（就是查询的数据的匹配条件不是等于的，而是一个范围之类的）

示例：

![](https://ws4.sinaimg.cn/large/006OWbT9gy1fsy4htyjzyj30ip0b0jsc.jpg
)

- 多表连接的写法

```sql
1.分析要查询的列都来自于哪些表,构成FROM子句;
2.分析这些表之间的关联关系,如果表之间没有直接关联
关系,而是通过另一个中间表关联,则也要在FROM子句中
补充中间关联表;
3.接下来在 WHERE 子句中补充表之间的关联关系,通常 N 个
表,至少要有 N-1 个关联关系;
4.分析是否还有其它限制条件,补充到WHERE子句的表关联
关系之后,作为限制条件;
5.根据用户想要显示的信息,补充 SELECT 子句。
6.分析是否有排序要求,如果排序要求中还涉及到其它表
,则也要进行第2步补充排序字段所在的表,并且添加表之
间的关联关系;
```

- 自身连接

> 自身连接,也叫自连接,是一个表通过某种条件和本身进行连接的一种方式,就如同多个表连接一样。

- ANSI SQL:1999标准的连接语法

> Oracle除了上述自己的连接语法外,同时支持美国国家
标准协会(ANSI)的SQL:1999标准的连接语法。

- 交叉连接

> 交叉连接会产生连个表的交叉乘积,和两个表之间的笛卡尔积是
一样的;使用 `CROSS JOIN` 子句完成。

- 自然连接

```sql
– 自然连接是对两个表之间相同名字和数据类型的列进行的等值连接;
– 如果两个表之间相同名称的列的数据类型不同,则会产生错误;
– 使用 NATURAL JOIN 子句来完成。
```

- USING 子句

> 自然连接是使用所有名称和数据类型相匹配的列作为连接条件,而USING子句可以指定用某个或某几个相同名字和数据类型的列作为连接条件。

示例：

![](https://ws2.sinaimg.cn/large/006OWbT9gy1fsy4qajmrzj30jc0a2mxs.jpg
)

`USING` 子句注意事项：

```
使用USING子句创建连接时,应注意以下几点:
– 如果有若干个列名称相同但数据类型不同,自然连接子句可以用USING子句来替换,以指定产生等值连接的列。
– 如果有多于一个列都匹配的情况,使用USING子句只能指定其中的一列。
– USING子句中的用到的列不能使用表名和别名作为前缀。
– NATURAL JOIN子句和USING子句是相互排斥的,不能同时使用。
```

- ON 子句

```
– 自然连接条件基本上是具有相同列名的表之间的等值连接;
– 如果要指定任意连接条件,或指定要连接的列,则可以使用ON子句;
– 用ON将连接条件和其它检索条件分隔开,其它检索条件写在WHERE子句;
– ON子句可以提高代码的可读性
```

示例：

![](https://ws2.sinaimg.cn/large/006OWbT9gy1fsy4uyg89xj30i10c0q3w.jpg
)

- 外部连接

```
•
在多表连接时,可以使用外部连接来查看哪些行,按照连接条件没有被匹配上。
• 左外连接以FROM子句中的左边表为基表,该表所有行
数据按照连接条件无论是否与右边表能匹配上,都会被显示出来。
• 右外连接以FROM子句中的右边表为基表,该表所有行数据按照连接条件无论是否与左边表能匹配上,都会被显示出来。
```

- 左外连接

![](https://ws1.sinaimg.cn/large/006OWbT9gy1fsy4yfev84j30jk0c6wfx.jpg
)

- 右外连接

![](https://ws3.sinaimg.cn/large/006OWbT9gy1fsy4yxfcpgj30j00c3dh7.jpg
)

---

## 第 7 章 高级查询

- 分组函数

```
分组函数是对表中一组记录进行操作,每组只返回一个结果,即首先要对表记录进行分组,然后再进行操作汇总,每组返回一个结果,分组时可能是整个表分为一组,也可能根据条件分成多组。
```

- 分组函数常用的五个函数

```
MIN
MAX
SUM
AVG
COUNT
```

- 使用分组函数

```sql
SELECT [column,] group_function(column) FROM table [WHERE condition] [GROUP BY column] [HAVING group_function(column)expression] [ORDER BY column| group_function(column)expression];
```

- MIN函数和MAX函数

```sql
– MIN和MAX函数主要是返回每组的最小值和最大值。
• MIN([DISTINCT|ALL] column|expression)
• MAX([DISTINCT|ALL] column|expression)
– MIN和MAX可以用于任何数据类型

-- 查询入职日期最早和最晚的日期

select min(hiredate),max(hiredate) from emp;
```

- SUM函数和AVG函数

```sql
– SUM和AVG函数分别返回每组的总和及平均值。
• SUM([DISTINCT|ALL] column|expression)
• AVG([DISTINCT|ALL] column|expression)
– SUM和AVG函数都是只能够对数值类型的列或表达式操作。

-- 查询职位以SALES开头的所有员工平均工资、最低工资、最高工资、工资和。

select avg(sal),min(sal),max(sal),sum(sal) from emp where job like 'SALES%';
```

- COUNT 函数

```sql
– COUNT( [DISTINCT|ALL] column|expression):返回满足条件的非空(NULL)行的数量

-- 查询部门30有多少个员工领取奖金。

select count(comm) from emp where deptno=30;
```

- 组函数中DISTINCT

> DISTINCT会消除重复记录后再使用组函数。

```sql
-- 查询有员工的部门数量

select count(distinct deptno) from emp; 
```

- 分组函数中空值处理

> 除了COUNT(*)之外,其它所有分组函数都会忽略列中的空值,然后再进行计算。

- 在分组函数中使用 IFNULL 函数

> IFNULL 函数可以使分组函数强制包含含有空值的记录

```sql
select avg(ifnull(comm,0)) from emp;
```

---

- 创建数据组

- 用 GROUP BY 子句创建数据组

```sql
SELECT column, group_function(column) FROM table [WHERE condition] [GROUP BY group_by_expression] [ORDER BY column];

-- 其中GROUP BY子句指定要分组的列

-- 查询每个部门的编号,平均工资

select deptno,avg(sal) from emp group by deptno;

!!! 在SELECT列表中除了分组函数那些项,所有列都必须包含在 GROUP BY 子句中。

-- GROUP BY 所指定的列并不是必须出现在 SELECT 列表中、

select avg(sal) from emp group by deptno;
```

- 使用组函数的非法的查询

> 不能在 WHERE子句中限制组

> 可以通过 HAVING 子句限制组

![](https://ws3.sinaimg.cn/large/006OWbT9gy1fsy5ljzvkqj30ij079t9o.jpg
)


- 用 HAVING 子句排除组结果

```sql
-- 使用 HAVING 子句限制组
-- 记录已经分组.
-- 使用过组函数.
-- 与 HAVING 子句匹配的结果才输出

SELECT column, group_function(column) FROM table [WHERE condition] [GROUP BY group_by_expression] [HAVING group_confition] [ORDER BY column];

-- 查询每个部门最高工资大于2900的部门编号,最高工资

select deptno,max(sal) from emp group by deptno having max(sal)>2900;
```

- SELECT语句执行过程

```
1.通过FROM子句中找到需要查询的表;
2.通过WHERE子句进行非分组函数筛选判断;
3.通过GROUP BY子句完成分组操作;
4.通过HAVING子句完成组函数筛选判断;
5.通过SELECT子句选择显示的列或表达式及组函数;
6.通过ORDER BY子句进行排序操作。
```

- 子查询

![](https://ws2.sinaimg.cn/large/006OWbT9gy1fsy5tmaofdj30in09r3zs.jpg
)

- 子查询使用指导

```
子查询要用括号括起来
将子查询放在比较运算符的右边
对于单行子查询要使用单行运算符
对于多行子查询要使用多行运算符
```

- 单行子查询

> 子查询只返回一行一列
> 使用单行运算符

运算符 | 含义
|:-|:-|
= | 等于
\> | 大于
\>= | 大于等于
< | 小于
<= | 小于等于
<> | 不等于

- 多行子查询

```sql
– 子查询返回记录的条数 可以是一条或多条。
– 和多行子查询进行比较时,需要使用多行操作符,多行操作符包括:
• IN
• ANY
• ALL
– IN操作符和以前介绍的功能一致,判断是否与子查询的任意一个返回值相同。
```

- IN 的使用

- ANY 的使用

```sql
– ANY:表示和子查询的任意一行结果进行比较,有一个满足条件即可。
• < ANY:表示小于子查询结果集中的任意一个,即小于最大值就可以。
• > ANY:表示大于子查询结果集中的任意一个,即大于最小值就可以。
• = ANY:表示等于子查询结果中的任意一个,即等于谁都
可以,相当于IN。
```

- ALL 的使用

```sql
– ALL:表示和子查询的所有行结果进行比较,每一行必须都满足条件。
• < ALL:表示小于子查询结果集中的所有行,即小于最小值。
• > ALL:表示大于子查询结果集中的所有行,即大于最大值。
• = ALL :表示等于子查询结果集中的所有行,即等于所有值,通常无意义。
```

---

- 子查询的空值（重要）

```sql
-- 查询不是经理的员工姓名
SELECT * FROM p_emp e WHERE e.empno NOT IN (SELECT mgr FROM p_emp)

-- 输出结果为空，没有返回值

-- 解决方法 `可以在子查询里用is not null或函数过滤null值`

-- 具体见：https://www.cnblogs.com/sutao/p/7380220.html

SELECT * FROM p_emp e WHERE e.empno NOT IN (SELECT mgr FROM p_emp WHERE mgr IS NOT NULL)
```

- 在 FROM 子句中使用子查询

![](https://ws4.sinaimg.cn/large/006OWbT9gy1fsy6a3k7bkj30jh0cemys.jpg
)


