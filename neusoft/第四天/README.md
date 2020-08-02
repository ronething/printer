<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Day 4](#day-4)
  - [第 1 章 Mybatis框架入门](#%E7%AC%AC-1-%E7%AB%A0-mybatis%E6%A1%86%E6%9E%B6%E5%85%A5%E9%97%A8)
  - [第 2 章 MyBatis核心配置与DAO开发](#%E7%AC%AC-2-%E7%AB%A0-mybatis%E6%A0%B8%E5%BF%83%E9%85%8D%E7%BD%AE%E4%B8%8Edao%E5%BC%80%E5%8F%91)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Day 4

## 第 1 章 Mybatis框架入门

- 什么是 MyBatis

```
Mybatis 本是apache的一个开源项目iBatis, 2010年这个项目由apache software foundation 迁移到了google code，并且改名为Mybatis。2013年11月迁移到Github。
iBATIS一词来源于“internet”和“abatis”的组合，是一个基于Java的持久层框架。iBATIS提供的持久层框架包括SQL Maps和Data Access Objects（DAO）
Mybatis是一个数据持久层(ORM)框架。把实体类和SQL语句之间建立了映射关系，是一种半自动化的ORM实现。

下载地址：https://github.com/mybatis
```

- Mybatis 的优点

```
1.基于SQL语法，简单易学。
2.能了解底层组装过程。
3.SQL语句封装在配置文件中，便于统一管理与维护，降低了程序的耦合度。
4.程序调试方便。
所有sql语句，全部定义在xml（建议）中。也可以通过注解的方式在接口上实现。这些映射文件称之为mapper。
```

- Mybatis 框架功能架构

```
Mybatis框架功能架构分为三层：
API接口层：提供给外部使用的接口API，开发人员通过这些本地API来操纵数据库。接口层一接收到调用请求就会调用数据处理层来完成具体的数据处理。
数据处理层：负责具体的SQL查找、SQL解析、SQL执行和执行结果映射处理等。它主要的目的是根据调用的请求完成一次数据库操作。
基础支撑层：负责最基础的功能支撑，包括连接管理、事务管理、配置加载和缓存处理，这些都是共用的东西，将他们抽取出来作为最基础的组件。为上层的数据处理层提供最基础的支撑。
```

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsyaml0qjmj20jp0au0sy.jpg)

- Mybatis 工作流程

```
(1)加载配置并初始化
将SQL的配置信息加载成为一个个MappedStatement对象（包括了传入参数映射配置、执行的SQL语句、结果映射配置），存储在内存中。
(2)接收调用请求
传入参数：为SQL的ID和传入参数对象
(3)处理操作请求
处理过程：
(A)根据SQL的ID查找对应的MappedStatement对象。
(B)根据传入参数对象解析MappedStatement对象，得到最终要执行的SQL和执行传入参数。
(C)获取数据库连接，根据得到的最终SQL语句和执行传入参数到数据库执行，并得到执行结果。
(D)根据MappedStatement对象中的结果映射配置对得到的执行结果进行转换处理，并得到最终的处理结果。
(E)释放连接资源。
(4)返回处理结果
将最终的处理结果返回。
```

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsyanp686bj20fi08fwje.jpg)


---

- Mybatis框架项目开发流程(重点)

```
Mybatis项目创建流程
1、新建Maven项目
2、pom.xml配置，导入Mybatis的依赖jar包
3、创建SqlMapConfig.xml 全局配置文件，配置数据源、事务等Mybatis
运行环境
4、创建mapper.xml映射文件，配置增、删、改、查的SQL语句。
5、创建SqlSessionFactory，根据全局配置文件创建工厂
6、创建SqlSession，是一个接口，执行数据库操作
7、释放资源
```

- 新建 Maven 项目前的配置

上网站 http://maven.apache.org/download.cgi 下载 [Maven zip压缩包](http://mirrors.hust.edu.cn/apache/maven/maven-3/3.5.4/binaries/apache-maven-3.5.4-bin.zip)

下载完成后 修改 ./conf/settings.xml
在 146行左右 `<mirrors>` 里面添加阿里云镜像源

```xml
<mirror>
    <id>alimaven</id>
    <name>aliyun maven</name>
    <url>http://maven.aliyun.com/nexus/content/groups/public/</url>
    <mirrorOf>central</mirrorOf>
</mirror>
```

接着 在 `myeclipse`或`eclipse` 按如下操作：

![](https://ws1.sinaimg.cn/large/ecb0a9c3ly1fsyxqnczbyj204x06faa0.jpg)

- 设置 installations

![](https://ws1.sinaimg.cn/large/ecb0a9c3ly1fsyxs6gf2aj20ht0f4tac.jpg)

![](https://ws1.sinaimg.cn/large/ecb0a9c3ly1fsyxsd5bn0j20el0clwfb.jpg)

- 设置 user setting

![](https://ws1.sinaimg.cn/large/ecb0a9c3ly1fsyxu2htwbj20ht0f4jt1.jpg)

- 新建 Maven 项目

![](https://ws1.sinaimg.cn/large/ecb0a9c3ly1fsyxx8a90ij20l40hvwfz.jpg)

![](https://ws1.sinaimg.cn/large/ecb0a9c3ly1fsyxwnvuvlj20l70h10tw.jpg)

- 填写 GroupId、ArtifactId 后 点击 Finish

> GroupId: com.neusoft (相当于标识)

> ArtifactId: mybatis-demo1(相当于项目名称)

![](https://ws1.sinaimg.cn/large/ecb0a9c3ly1fsyxy9lexjj20l70h1myd.jpg)

- 配置 `pom.xml`

```xml
<!--添加依赖-->
<dependencies>
    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
        <version>5.1.25</version>
    </dependency>
<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis</artifactId>
    <version>3.4.6</version>
</dependency>
</dependencies>
```

- 在 src/main/resources 下新建 `SqlMapConfig.xml` 

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration
  PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
  "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
  <environments default="development">
    <environment id="development">
      <transactionManager type="JDBC"/>
      <dataSource type="POOLED">
        <property name="driver" value="com.mysql.jdbc.Driver"/>
        <property name="url" value="jdbc:mysql://localhost:3306/dongruan?useUnicode=true&amp;characterEncoding=utf8&amp;autoReconnect=true"/>
        <property name="username" value="username"/>
        <property name="password" value="password"/>
      </dataSource>
    </environment>
  </environments>
  <mappers>
    <mapper resource="./mapper/DeptMapper.xml"/>
  </mappers>
</configuration>
```

- 创建 mapper.xml 映射文件，配置增、删、改、查的 SQL 语句

```xml
<!--DeptMapper.xml-->

<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
  PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
  "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.demo.mybatis.po.Dept">
  <select id="selectDept" resultType="com.demo.mybatis.po.Dept">
    select * from dept where deptno = #{deptNo}
  </select>
  
  <insert id="addDept" parameterType="com.demo.mybatis.po.Dept">
  		insert into dept values (#{deptNo},#{dname},#{loc})
  </insert>
  
  <delete id="removeDept">
  		delete from dept where deptno=#{deptNo}
  </delete>
  
  <update id="updateDept" parameterType="com.demo.mybatis.po.Dept">
  		update dept set dname=#{dname},loc=#{loc} where deptno=#{deptNo}
  </update>
</mapper>
```

- 实体类

```java
// Dept.java

package com.demo.mybatis.po;

public class Dept {
	private int deptNo;
	private String dname;
	private String loc;
	public int getDeptNo() {
		return deptNo;
	}
	public void setDeptNo(int deptNo) {
		this.deptNo = deptNo;
	}
	public String getDname() {
		return dname;
	}
	public void setDname(String dname) {
		this.dname = dname;
	}
	public String getLoc() {
		return loc;
	}
	public void setLoc(String loc) {
		this.loc = loc;
	}
	
}

```

- 测试类（创建`SqlSessionFactory`,根据全局配置文件创建工厂 创建`SqlSession`是一个接口，执行数据库操作）

```java
package com.demo.test;

import java.io.IOException;
import java.io.InputStream;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import com.demo.mybatis.po.Dept;


public class Demo1 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		String resource = "./SqlMapConfig.xml";
		InputStream inputStream = Resources.getResourceAsStream(resource);
		SqlSessionFactory sqlSessionFactory =
		  new SqlSessionFactoryBuilder().build(inputStream);
		
		SqlSession session = sqlSessionFactory.openSession();
		
		//select test
		Dept dept = session.selectOne("selectDept", 60);
		System.out.println(dept.getLoc());
		
		//insert test
//		Dept dept = new Dept();
//		dept.setDeptNo(80);
//		dept.setDname("研发部");
//		dept.setLoc("深圳");
//		
//		int num = session.insert("addDept", dept);


		
		// delete test
		
		//int num = session.delete("removeDept", 66);
		
		// update test
//		Dept dept = new Dept();
//		dept.setDeptNo(60);
//		dept.setDname("hello");
//		dept.setLoc("guangzhou");
//		
//		int num = session.update("updateDept", dept); 
//		
//		session.commit();	
//		if (num>0){
//		System.out.println("success");
//		}
//		
		
		session.close();
	}

}

```

见 [demo](./demo)

---

## 第 2 章 MyBatis核心配置与DAO开发

- Mybatis 开发 dao 的方法

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fszcycz1qqj210o07rmyy.jpg)


- 原始 dao 开发方法

```
controller: 处理用户请求，业务控制逻辑
dao: 增删改查，数据操作，持久化操作
po: 实体类 关系表映射的类
service: 业务服务方法，算法
```

见 [mybatis-demo2](./mybatis-demo2)

- mapper 代理开发

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fszczh34z8j212n0ajgob.jpg)

见 [mybatis-demo3](./mybatis-demo3)
