# JavaScript 简介

- JavaScript 是脚本语言

- JavaScript 是一种轻量级的编程语言。

- JavaScript 是可插入 HTML 页面的编程代码。

- JavaScript 插入`HTML` 页面后，可由所有的现代浏览器执行。


---

- JavaScript：直接写入 HTML 输出流

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
	
<p>
JavaScript 能够直接写入 HTML 输出流中：
</p>
<script>
document.write("<h1>这是一个标题</h1>");
document.write("<p>这是一个段落。</p>");
</script>
<p>
您只能在 HTML 输出流中使用 <strong>document.write</strong>。
如果您在文档已加载后使用它（比如在函数中），会覆盖整个文档。
</p>
	
</body>
</html>
```

- JavaScript：对事件的反应

```html
<button type="button" onclick="alert('欢迎!')">点我!</button>
```

- JavaScript：改变 HTML 内容

```js
x=document.getElementById("demo")  //查找元素
x.innerHTML="Hello JavaScript";    //改变内容
```

- JavaScript：改变 HTML 图像

```html
<script>
function changeImage()
{
    element=document.getElementById('myimage')
    if (element.src.match("bulbon"))
    {
        element.src="/images/pic_bulboff.gif";
    }
    else
    {
        element.src="/images/pic_bulbon.gif";
    }
}
</script>
<img id="myimage" onclick="changeImage()" src="/images/pic_bulboff.gif" width="100" height="180">
```

- JavaScript：改变 HTML 样式

```js
x=document.getElementById("demo")  //找到元素 
x.style.color="#ff0000";           //改变样式
```

- JavaScript：验证输入

```js
function myFunction()
{
	var x=document.getElementById("demo").value;
	if(x==""||isNaN(x))
	{
		alert("不是数字");
	}
}
```

> 注：

```
JavaScript 与 Java 是两种完全不同的语言。

ECMA-262 是 JavaScript 标准的官方名称。

ECMAScript 6 也称为 ECMAScript 2015。

ECMAScript 7 也称为 ECMAScript 2016。
```