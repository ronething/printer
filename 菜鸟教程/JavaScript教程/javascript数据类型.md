# JavaScript 数据类型

`字符串（String）、数字(Number)、布尔(Boolean)、数组(Array)、对象(Object)、空（Null）、未定义（Undefined）。`

## JavaScript 拥有动态类型

```js
JavaScript 拥有动态类型。这意味着相同的变量可用作不同的类型：

var x;               // x 为 undefined
var x = 5;           // 现在 x 为数字
var x = "John";      // 现在 x 为字符串
```

## JavaScript 字符串

```js
单引号双引号均可
var carname="Volvo XC60";
var carname='Volvo XC60';
```

```js
var answer="It's alright";
var answer="He is called 'Johnny'";
var answer='He is called "Johnny"';
```

## JavaScript 数字

```js
var x1=34.00;      //使用小数点来写
var x2=34;         //不使用小数点来写

var y=123e5;      // 12300000
var z=123e-5;     // 0.00123
```

## JavaScript 布尔

```js
var x=true;
var y=false;
```

## JavaScript 数组

```js
var cars=new Array();
cars[0]="Saab";
cars[1]="Volvo";
cars[2]="BMW";

var cars=new Array("Saab","Volvo","BMW");

var cars=["Saab","Volvo","BMW"];
```　

## JavaScript 对象

```js
对象由花括号分隔。在括号内部，对象的属性以名称和值对的形式 (name : value) 来定义。属性由逗号分隔：

var person={firstname:"John", lastname:"Doe", id:5566};

空格和折行无关紧要。声明可横跨多行：

var person={
firstname : "John",
lastname  : "Doe",
id        :  5566
};

Undefined 和 Null
Undefined 这个值表示变量不含有值。

可以通过将变量的值设置为 null 来清空变量。

在使用var声明变量但未对其加以初始化时，这个变量的值就是undefined。   null值则是表示空对象指针。

undefined是访问一个未初始化的变量时返回的值，而null是访问一个尚未存在的对象时所返回的值。因此，可以把undefined看作是空的变量，而null看作是空的对象。

cars=null;
person=null;
```

## 声明变量类型

```js
var carname=new String;
var x=      new Number;
var y=      new Boolean;
var cars=   new Array;
var person= new Object;
```

> JavaScript 变量均为对象。当您声明一个变量时，就创建了一个新的对象。