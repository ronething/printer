# JavaScript 输出

- JavaScript 显示数据

	使用 window.alert() 弹出警告框。
	使用 document.write() 方法将内容写到 HTML 文档中。
	使用 innerHTML 写入到 HTML 元素。
	使用 console.log() 写入到浏览器的控制台。

- 使用 window.alert() 

```html
//弹出警告框
<!DOCTYPE html>
<html>
<body>

<h1>我的第一个页面</h1>
<p>我的第一个段落。</p>

<script>
window.alert(5 + 6);
</script>

</body>
</html>
```

- 操作 HTML 元素

> document.getElementById(id) 方法。请使用 "id" 属性来标识 HTML 元素，并 innerHTML 来获取或插入元素内容。

```html
<!DOCTYPE html>
<html>
<body>

<h1>我的第一个 Web 页面</h1>

<p id="demo">我的第一个段落</p>

<script>
document.getElementById("demo").innerHTML = "段落已修改。";
</script>

</body>
</html>
```

- 写到 HTML 文档

```html
<script>
document.write(Date());
</script>
```

> 注: 请使用 document.write() 仅仅向文档输出写内容。如果在文档已完成加载后执行 document.write，整个 HTML 页面将被覆盖。


```html
<!DOCTYPE html>
<html>
<body>

<h1>我的第一个 Web 页面</h1>

<p>我的第一个段落。</p>

<button onclick="myFunction()">点我</button>

<script>
function myFunction() {
   	document.write(Date());
}
</script>

</body>
</html>
```

> 效果图：

![](https://ws1.sinaimg.cn/large/ecb0a9c3ly1ftcv8zmz87g20kp0dyjt7.gif)

- 写到控制台

`console.log()`

```html
<!DOCTYPE html>
<html>
<body>

<h1>我的第一个 Web 页面</h1>

<script>
a = 5;
b = 6;
c = a + b;
console.log(c);
</script>

</body>
</html>
```

