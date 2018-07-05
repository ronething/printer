package com.demo.dao;

import com.demo.po.Dept;

public interface IDeptDAO {
	
	Dept findById(int deptno);
	
	int insert(Dept dept);
	
	int update(Dept dept);
	
	int delete(int deptno);
}
