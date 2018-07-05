package com.demo.test;

import java.io.IOException;
import java.io.InputStream;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import com.demo.dao.DeptMapper;

import com.demo.po.Dept;

public class mapperTest {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		String resource = "./SqlMapConfig.xml";
		InputStream inputStream = Resources.getResourceAsStream(resource);
		SqlSessionFactory sqlSessionFactory =
		  new SqlSessionFactoryBuilder().build(inputStream);
		
		SqlSession session = sqlSessionFactory.openSession();
		
		DeptMapper deptMapper = session.getMapper(DeptMapper.class); // ÷ÿµ„
		
		Dept dept = deptMapper.findById(10);
		
		System.out.println(dept.getDname());
	}
	
}
