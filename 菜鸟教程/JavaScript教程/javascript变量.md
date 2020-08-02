<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [JavaScript 变量](#javascript-%E5%8F%98%E9%87%8F)
  - [变量是用于存储信息的"容器"。](#%E5%8F%98%E9%87%8F%E6%98%AF%E7%94%A8%E4%BA%8E%E5%AD%98%E5%82%A8%E4%BF%A1%E6%81%AF%E7%9A%84%E5%AE%B9%E5%99%A8)
  - [JavaScript 数据类型](#javascript-%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B)
  - [声明（创建） JavaScript 变量](#%E5%A3%B0%E6%98%8E%E5%88%9B%E5%BB%BA-javascript-%E5%8F%98%E9%87%8F)
  - [一条语句，多个变量](#%E4%B8%80%E6%9D%A1%E8%AF%AD%E5%8F%A5%E5%A4%9A%E4%B8%AA%E5%8F%98%E9%87%8F)
  - [Value = undefined](#value--undefined)
  - [重新声明 JavaScript 变量](#%E9%87%8D%E6%96%B0%E5%A3%B0%E6%98%8E-javascript-%E5%8F%98%E9%87%8F)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# JavaScript 变量

## 变量是用于存储信息的"容器"。

```js
var x=5;
var y=6;
var z=x+y;
```

## JavaScript 数据类型

## 声明（创建） JavaScript 变量

```js
var carname="Volvo";
document.getElementById("demo").innerHTML=carname;
```

## 一条语句，多个变量

```js
var lastname="Doe", age=30, job="carpenter";
声明也可横跨多行：

var lastname="Doe",
age=30,
job="carpenter";
一条语句中声明的多个不可以赋同一个值:

var x,y,z=1;
x,y 为 undefined， z 为 1。
```

## Value = undefined

`var carname;`

## 重新声明 JavaScript 变量

```js
如果重新声明 JavaScript 变量，该变量的值不会丢失：

在以下两条语句执行后，变量 carname 的值依然是 "Volvo"：

var carname="Volvo"; 
var carname;
```