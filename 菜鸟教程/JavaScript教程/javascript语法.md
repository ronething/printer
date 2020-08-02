<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [JavaScript 语法](#javascript-%E8%AF%AD%E6%B3%95)
  - [JavaScript 字面量](#javascript-%E5%AD%97%E9%9D%A2%E9%87%8F)
  - [JavaScript 变量](#javascript-%E5%8F%98%E9%87%8F)
  - [JavaScript 关键字](#javascript-%E5%85%B3%E9%94%AE%E5%AD%97)
  - [JavaScript 注释](#javascript-%E6%B3%A8%E9%87%8A)
  - [JavaScript 数据类型](#javascript-%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B)
  - [JavaScript 函数](#javascript-%E5%87%BD%E6%95%B0)
  - [JavaScript 字母大小写](#javascript-%E5%AD%97%E6%AF%8D%E5%A4%A7%E5%B0%8F%E5%86%99)
  - [JavaScript 字符集](#javascript-%E5%AD%97%E7%AC%A6%E9%9B%86)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# JavaScript 语法

## JavaScript 字面量

```js
数字（Number）字面量 可以是整数或者是小数，或者是科学计数(e)。
3.14

1001

123e5
```

```js
字符串（String）字面量 可以使用单引号或双引号:

"John Doe"

'John Doe'
```

```js
表达式字面量 用于计算：

5 + 6

5 * 10
```

```js
数组（Array）字面量 定义一个数组：

[40, 100, 1, 5, 25, 10]
对象（Object）字面量 定义一个对象：

{firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"}
函数（Function）字面量 定义一个函数：

function myFunction(a, b) { return a * b;}
```

## JavaScript 变量

```js
JavaScript 使用关键字 var 来定义变量， 使用等号来为变量赋值：

var x, length

x = 5

length = 6
```

## JavaScript 关键字

```js
var 关键字告诉浏览器创建一个新的变量：
var x = 5 + 6;
var y = x * 10;
```

## JavaScript 注释

`//这是注释`

## JavaScript 数据类型

```js
JavaScript 有多种数据类型：数字，字符串，数组，对象等等：

var length = 16;                                  // Number 通过数字字面量赋值 
var points = x * 10;                              // Number 通过表达式字面量赋值
var lastName = "Johnson";                         // String 通过字符串字面量赋值
var cars = ["Saab", "Volvo", "BMW"];              // Array  通过数组字面量赋值
var person = {firstName:"John", lastName:"Doe"};  // Object 通过对象字面量赋值
```

## JavaScript 函数

```js
function myFunction(a, b) {
   	return a * b;                                // 返回 a 乘以 b 的结果
}
```

## JavaScript 字母大小写

```js
JavaScript 对大小写是敏感的。

当编写 JavaScript 语句时，请留意是否关闭大小写切换键。

函数 getElementById 与 getElementbyID 是不同的。

同样，变量 myVariable 与 MyVariable 也是不同的。
```

## JavaScript 字符集

```js
JavaScript 使用 Unicode 字符集。

Unicode 覆盖了所有的字符，包含标点等字符。
```