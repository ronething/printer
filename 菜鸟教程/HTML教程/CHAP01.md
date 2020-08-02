<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [这是一个标题](#%E8%BF%99%E6%98%AF%E4%B8%80%E4%B8%AA%E6%A0%87%E9%A2%98)
  - [这是一个标题](#%E8%BF%99%E6%98%AF%E4%B8%80%E4%B8%AA%E6%A0%87%E9%A2%98-1)
    - [这是一个标题](#%E8%BF%99%E6%98%AF%E4%B8%80%E4%B8%AA%E6%A0%87%E9%A2%98-2)
  - [这是一个标题](#%E8%BF%99%E6%98%AF%E4%B8%80%E4%B8%AA%E6%A0%87%E9%A2%98-3)
- [一个标题](#%E4%B8%80%E4%B8%AA%E6%A0%87%E9%A2%98)
  - [内联样式](#%E5%86%85%E8%81%94%E6%A0%B7%E5%BC%8F)
- [居中对齐的标题](#%E5%B1%85%E4%B8%AD%E5%AF%B9%E9%BD%90%E7%9A%84%E6%A0%87%E9%A2%98)
  - [内部样式表](#%E5%86%85%E9%83%A8%E6%A0%B7%E5%BC%8F%E8%A1%A8)
  - [外部样式表](#%E5%A4%96%E9%83%A8%E6%A0%B7%E5%BC%8F%E8%A1%A8)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->



- 中文乱码问题（头部声明为UTF-8）

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>页面标题</title>
</head>
<body>
 
<h1>我的第一个标题</h1>
 
<p>我的第一个段落。</p>
 
</body>
</html>
```

- 标题`<h1>-<h6>`

```html
<h1>这是一个标题</h1>
<h2>这是一个标题</h2>
<h3>这是一个标题</h3>
```
效果如下：

<h1>这是一个标题</h1>

<h2>这是一个标题</h2>

<h3>这是一个标题</h3>

- 段落

```html
<p>这是一个段落。</p>
<p>这是另外一个段落。</p>
```

> 浏览器会自动地在段落的前后添加空行。

- 链接

```html
<a href="http://www.runoob.com">这是一个链接</a>
```

- 图像

```html
在 HTML 中，图像由<img> 标签定义。

<img> 是空标签，意思是说，它只包含属性，并且没有闭合标签。

要在页面上显示图像，你需要使用源属性（src）。src 指 "source"。源属性的值是图像的 URL 地址。

# Alt属性
alt 属性用来为图像定义一串预备的可替换的文本。
在浏览器无法载入图像时，替换文本属性告诉读者她们失去的信息。此时，浏览器将显示这个替代性的文本而不是图像。为页面上的图像都加上替换文本属性是个好习惯，这样有助于更好的显示信息，并且对于那些使用纯文本浏览器的人来说是非常有用的。

# 设置图像的高度与宽度
height（高度） 与 width（宽度）属性用于设置图像的高度与宽度。

<img src="https://ws1.sinaimg.cn/large/006OWbT9gy1fstjdczairj31z41407ar.jpg" width="258" height="139" />
```

<img src="https://ws1.sinaimg.cn/large/006OWbT9gy1fstjdczairj31z41407ar.jpg" width="258" height="139" />

- 元素

![](https://ws1.sinaimg.cn/large/006OWbT9gy1fsulnimgixj30ot07e0sy.jpg)

![](https://ws1.sinaimg.cn/large/006OWbT9gy1fsuloyjpfuj30o905iaaf.jpg)

> 记得结束标签

- 空元素

```
没有内容的 HTML 元素被称为空元素。空元素是在开始标签中关闭的。
<br> 就是没有关闭标签的空元素（<br> 标签定义换行）。
在 XHTML、XML 以及未来版本的 HTML 中，所有元素都必须被关闭。
在开始标签中添加斜杠，比如 <br />，是关闭空元素的正确方法，HTML、XHTML 和 XML 都接受这种方式。
即使 <br> 在所有浏览器中都是有效的，但使用 <br /> 其实是更长远的保障。
```

> 使用小写标签。

> 严格来讲, 一个 HTML 元素包含了开始标签与结束标签。

- 属性

> 属性一般描述于开始标签。

> 在某些个别的情况下，比如属性值本身就含有双引号，那么您必须使用单引号，例如：name='John "ShotGun" Nelson'。

> 使用小写属性。

> 属性参考手册

![](https://ws1.sinaimg.cn/large/006OWbT9gy1fsultf3m5hj30os07p0t0.jpg)

- 水平线

```html
<hr> 标签在 HTML 页面中创建水平线。
```

- 注释

```html
<!-- 这是一个注释 -->
```

- 如何查看源代码（chrome）

```
ctrl+U or F12
```

- 折行

```html
如果您希望在不产生一个新段落的情况下进行换行（新行），请使用 <br /> 标签

<p>这个<br>段落<br>演示了分行的效果</p>
```

- 格式化标签

```html
HTML 使用标签 <b>("bold") 与 <i>("italic") 对输出的文本进行格式, 如：粗体 or 斜体

	通常标签 <strong> 替换加粗标签 <b> 来使用, <em> 替换 <i>标签使用。

然而，这些标签的含义是不同的：

<b> 与<i> 定义粗体或斜体文本。

<strong> 或者 <em>意味着你要呈现的文本是重要的，所以要突出显示。现今所有主要浏览器都能渲染各种效果的字体。不过，未来浏览器可能会支持更好的渲染效果。
```

![](https://ws1.sinaimg.cn/large/006OWbT9gy1fsum2zm9qcj30ot0etmxm.jpg)

![](https://ws1.sinaimg.cn/large/006OWbT9gy1fsum4g14yrj30ox091t8z.jpg)

![](https://ws1.sinaimg.cn/large/006OWbT9gy1fsum5gh7ioj30oq0bkglz.jpg)

其中,`<bdo>`标签用法：

```html
<p>该段落文字从左到右显示。</p>  
<p><bdo dir="rtl">该段落文字从右到左显示。</bdo></p>
```

- 链接

```html
<a href="url">链接文本</a>

# target 属性
下面的这行会在新窗口打开文档：
<a href="http://www.runoob.com/" target="_blank">访问菜鸟教程!</a>

```

`id 属性`

![](https://ws1.sinaimg.cn/large/006OWbT9gy1fsumhie5y3j30q50bjwfa.jpg)

```
基本的注意事项 - 有用的提示
注释： 请始终将正斜杠添加到子文件夹。假如这样书写链接：href="http://www.runoob.com/html"，就会向服务器产生两次 HTTP 请求。这是因为服务器会添加正斜杠到这个地址，然后创建一个新的请求，就像这样：href="http://www.runoob.com/html/"。
```

```
默认情况下，链接将以以下形式出现在浏览器中：

一个未访问过的链接显示为蓝色字体并带有下划线。
访问过的链接显示为紫色并带有下划线。
点击链接时，链接显示为红色并带有下划线。

注意：如果为这些超链接设置了 CSS 样式，展示样式会根据 CSS 的设定而显示。
```

- 头部

    - `<head>`元素

    ```html
    <head> 元素包含了所有的头部标签元素。在 <head>元素中你可以插入脚本（scripts）, 样式文件（CSS），及各种meta信息。

    可以添加在头部区域的元素标签为: <title>, <style>, <meta>, <link>, <script>, <noscript>, and <base>.
    ```

    - `<title>` 元素

    ```html
    <title> 标签定义了不同文档的标题。

    <title> 在 HTML/XHTML 文档中是必须的。

    <title> 元素:

    定义了浏览器工具栏的标题。
    当网页添加到收藏夹时，显示在收藏夹中的标题。
    显示在搜索引擎结果页面的标题。
    ```

    - `<base>` 元素

    `<base>` 标签描述了基本的链接地址/链接目标，该标签作为HTML文档中所有的链接标签的默认链接

    ```html
    <head><base href="http://www.runoob.com/images/" target="_blank"></head>
    ```

    - `<link>` 元素

    > `<link>` 标签定义了文档与外部资源之间的关系，通常用于链接到样式表。

    ```html
    <head><link rel="stylesheet" type="text/css" href="mystyle.css"></head>
    ```

    - `<style>` 元素

    > `<style>` 标签定义了HTML文档的样式文件引用地址.
    在 `<style>` 元素中你也可以直接添加样式来渲染 HTML 文档

    ```html
    <head><style type="text/css">
    body {background-color:yellow}
    p {color:blue}
    </style></head>
    ```

    - `<meta>` 元素

    ```html
    meta标签描述了一些基本的元数据。

    <meta> 标签提供了元数据.元数据也不显示在页面上，但会被浏览器解析。

    META 元素通常用于指定网页的描述，关键词，文件的最后修改时间，作者，和其他元数据。

    元数据可以使用于浏览器（如何显示内容或重新加载页面），搜索引擎（关键词），或其他Web服务。

    <meta> 一般放置于 <head> 区域
    ```

    ```html
    为搜索引擎定义关键词:

    <meta name="keywords" content="HTML, CSS, XML, XHTML, JavaScript">

    为网页定义描述内容:

    <meta name="description" content="免费 Web & 编程 教程">

    定义网页作者:

    <meta name="author" content="Runoob">

    每30秒钟刷新当前页面:

    <meta http-equiv="refresh" content="30">

    ```

    - `<script>` 元素
    
    ```html
    <script>标签用于加载脚本文件，如： JavaScript。
    ```

---

- 样式 CSS

![](https://ws1.sinaimg.cn/large/006OWbT9gy1fsumyzd890j30he07qwew.jpg)

## 内联样式

```html
当特殊的样式需要应用到个别元素时，就可以使用内联样式。 使用内联样式的方法是在相关的标签中使用样式属性。样式属性可以包含任何 CSS 属性。以下实例显示出如何改变段落的颜色和左外边距。

<p style="color:blue;margin-left:20px;">This is a paragraph.</p>

```

```html
# 背景颜色

<body style="background-color:yellow;">
<h2 style="background-color:red;">这是一个标题</h2>
<p style="background-color:green;">这是一个段落。</p>
</body>
```

背景颜色就不演示了。

<h2 style="background-color:red;">这是一个标题</h2>
<p style="background-color:green;">这是一个段落。</p>

```html
# 字体, 字体颜色 ，字体大小

使用font-family（字体），color（颜色），和font-size（字体大小）属性来定义字体的样式:

<h1 style="font-family:verdana;">一个标题</h1>
<p style="font-family:arial;color:red;font-size:10px;">一个段落。</p>
```

效果图：

<h1 style="font-family:verdana;">一个标题</h1>
<p style="font-family:arial;color:red;font-size:10px;">一个段落。</p>

```html
# 文本对齐方式
使用 text-align（文字对齐）属性指定文本的水平与垂直对齐方式

<h1 style="text-align:center;">居中对齐的标题</h1>
<p>这是一个段落。</p>
```

效果图：

<h1 style="text-align:center;">居中对齐的标题</h1>
<p>这是一个段落。</p>

## 内部样式表

```
当单个文件需要特别样式时，就可以使用内部样式表。你可以在<head> 部分通过 <style>标签定义内部样式表

<head>
<style type="text/css">
body {background-color:yellow;}
p {color:blue;}
</style>
</head>
```

## 外部样式表

```
当样式需要被应用到很多页面的时候，外部样式表将是理想的选择。使用外部样式表，你就可以通过更改一个文件来改变整个站点的外观。

<head>
<link rel="stylesheet" type="text/css" href="mystyle.css">
</head>
```

> 该注意的地方

![](https://ws1.sinaimg.cn/large/006OWbT9gy1fsun8ykdedj30ot0aeq3g.jpg)

- 表格

```html
表格由 <table> 标签来定义。每个表格均有若干行（由 <tr> 标签定义），每行被分割为若干单元格（由 <td> 标签定义）。字母 td 指表格数据（table data），即数据单元格的内容。数据单元格可以包含文本、图片、列表、段落、表单、水平线、表格等等。

<table>
    <tr>
        <td>row 1, cell 1</td>
        <td>row 1, cell 2</td>
    </tr>
    <tr>
        <td>row 2, cell 1</td>
        <td>row 2, cell 2</td>
    </tr>
</table>
```

> 注：`tr`行，`td`表格数据。

```html
# 表格和边框属性

如果不定义边框属性，表格将不显示边框。有时这很有用，但是大多数时候，我们希望显示边框。

使用边框属性来显示一个带有边框的表格：

<table border="1">
    <tr>
        <td>Row 1, cell 1</td>
        <td>Row 1, cell 2</td>
    </tr>
</table>
```

> 无边框：

<table >
    <tr>
        <td>Row 1, cell 1</td>
        <td>Row 1, cell 2</td>
    </tr>
</table>

> 有边框：

<table border="1">
    <tr>
        <td>Row 1, cell 1</td>
        <td>Row 1, cell 2</td>
    </tr>
</table>

```html
# 表格表头
表格的表头使用 <th> 标签进行定义。
大多数浏览器会把表头显示为粗体居中的文本：

<table border="1">
    <tr>
        <th>Header 1</th>
        <th>Header 2</th>
    </tr>
    <tr>
        <td>row 1, cell 1</td>
        <td>row 1, cell 2</td>
    </tr>
</table>
```

效果图：

<table border="1">
    <tr>
        <th>Header 1</th>
        <th>Header 2</th>
    </tr>
    <tr>
        <td>row 1, cell 1</td>
        <td>row 1, cell 2</td>
    </tr>
</table>

![](https://ws1.sinaimg.cn/large/006OWbT9gy1fsunhq5722j30ok0fy3z4.jpg)

(关于表格的更多知识](http://www.runoob.com/html/html-tables.html)

- 列表

```html
HTML 支持有序、无序和定义列表:

# 无序列表
# 无序列表使用 <ul> 标签
<ul>
<li>Coffee</li>
<li>Milk</li>
</ul>

# 有序列表
# 有序列表始于 <ol> 标签。每个列表项始于 <li> 标签。

<ol>
<li>Coffee</li>
<li>Milk</li>
</ol>

# 自定义列表
# 自定义列表不仅仅是一列项目，而是项目及其注释的组合。

自定义列表以 <dl> 标签开始。每个自定义列表项以 <dt> 开始。每个自定义列表项的定义以 <dd> 开始。

<dl>
<dt>Coffee</dt>
<dd>- black hot drink</dd>
<dt>Milk</dt>
<dd>- white cold drink</dd>
</dl>
```

无序：

<ul>
<li>Coffee</li>
<li>Milk</li>
</ul>

有序：

<ol>
<li>Coffee</li>
<li>Milk</li>
</ol>

自定义：

<dl>
<dt>Coffee</dt>
<dd>- black hot drink</dd>
<dt>Milk</dt>
<dd>- white cold drink</dd>
</dl>

> 提示: 列表项内部可以使用段落、换行符、图片、链接以及其他列表等等。

- 区块

