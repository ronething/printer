package com.demo.dao.impl;

import java.io.IOException;
import java.io.InputStream;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import com.demo.dao.IDeptDAO;
import com.demo.po.Dept;

public class DeptDAOImpl implements IDeptDAO {
	
	private SqlSessionFactory sqlSessionFactory = null;

	public DeptDAOImpl(){
		try {
			String resource = "SqlMapConfig.xml";
			InputStream inputStream = Resources.getResourceAsStream(resource);
			sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);
		} catch (IOException e) {
		}
	}
	
	
	public Dept findById(int deptno) {
		// TODO Auto-generated method stub
		
		SqlSession session = sqlSessionFactory.openSession();
		
		Dept dept = session.selectOne("selectById",deptno);
		
		return dept;
		
	}


	public int insert(Dept dept) {
		// TODO Auto-generated method stub
		
		SqlSession session = sqlSessionFactory.openSession();
		
		int num = session.insert("addDept", dept);
		
		session.commit();
		
		return num;
	}


	public int update(Dept dept) {
		// TODO Auto-generated method stub
		SqlSession session = sqlSessionFactory.openSession();
		
		int num = session.insert("updateDept", dept);
		
		session.commit();
		
		return num;
	}


	public int delete(int deptno) {
		// TODO Auto-generated method stub
		
		SqlSession session = sqlSessionFactory.openSession();
		
		int num = session.insert("removeDept", deptno);
		
		session.commit();
		
		return num;
	}

}
