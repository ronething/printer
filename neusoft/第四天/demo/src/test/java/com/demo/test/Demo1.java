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
