# JavaScript 语句

## JavaScript 语句

```js
document.getElementById("demo").innerHTML = "你好 Dolly";
```

## 分号 ;

```js
分号用于分隔 JavaScript 语句。

通常我们在每条可执行的语句结尾添加分号。

使用分号的另一用处是在一行中编写多条语句。

实例:

a = 5;
b = 6;
c = a + b;
以上实例也可以这么写:

a = 5; b = 6; c = a + b;
```

## JavaScript 代码块

```js
代码块以左花括号开始，以右花括号结束。

代码块的作用是一并地执行语句序列。

function myFunction()
{
    document.getElementById("demo").innerHTML="你好Dolly";
    document.getElementById("myDIV").innerHTML="你最近怎么样?";
}
```

## JavaScript 语句标识符

语句	|描述
:-|:-
break|用于跳出循环。
catch|语句块，在 try 语句块执行出错时执行 catch 语句块。
continue|跳过循环中的一个迭代。
do ... while|执行一个语句块，在条件语句为 true 时继续执行该语句块。
for|在条件语句为true 时，可以将代码块执行指定的次数。
for ... in|用于遍历数组或者对象的属性（对数组或者对象的属性进行循环操作）。
function|定义一个函数
if ... else|用于基于不同的条件来执行不同的动作。
return|退出函数
switch|用于基于不同的条件来执行不同的动作。
throw|抛出（生成）错误 。
try|实现错误处理，与 catch 一同使用。
var|声明一个变量。
while|当条件语句为 true 时，执行语句块。

## 空格

```js
var person="Hege";
var person = "Hege";
```

## 对代码行进行折行

> 您可以在文本字符串中使用反斜杠对代码行进行换行。