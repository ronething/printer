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