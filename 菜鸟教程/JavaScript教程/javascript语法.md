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