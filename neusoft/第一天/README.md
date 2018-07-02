# 第一章 数据库基础

```sql
where 1=0; 这个条件始终为false，结果不会返回任何数据，只有表结构，可用于快速建表

SELECT * FROM strName WHERE 1 = 0; 该 select 语句主要用于读取表的结构而不考虑表中的数据，这样节省了内存，因为可以不用保存结果集。

create table newtable as select * from oldtable where 1=0; 
创建一个新表，而新表的结构与查询的表的结构是一样的。
```


