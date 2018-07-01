

- 什么是 RSS ？

```
RSS 指 Really Simple Syndication（真正简易联合）
RSS 使您有能力聚合（syndicate）网站的内容
RSS 定义了非常简单的方法来共享和查看标题和内容
RSS 文件可被自动更新
RSS 允许为不同的网站进行视图的个性化
RSS 使用 XML 编写
```

```
通过使用 RSS，您可以有选择地浏览您感兴趣的以及与您的工作相关的新闻。

通过使用 RSS，您可以把需要的信息从不需要的信息（兜售信息，垃圾邮件等）中分离出来。

通过使用 RSS，您可以创建自己的新闻频道，并将之发布到因特网。
```

---

- 实例

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">

<channel>
  <title>菜鸟教程首页</title>
  <link>http://www.runoob.com</link>
  <description>免费编程教程</description>
  <item>
    <title>RSS 教程</title>
    <link>http://www.runoob.com/rss</link>
    <description>菜鸟教程 Rss 教程</description>
  </item>
  <item>
    <title>XML 教程</title>
    <link>http://www.runoob.com/xml</link>
    <description>菜鸟教程 XML 教程</description>
  </item>
</channel>

</rss>
```

对上文实例的解释：

```xml
文档中的第一行：XML 声明 - 定义了文档中使用的 XML 版本和字符编码。此例子遵守 1.0 规范，并使用 UTF-8 字符集(可支持中文)。

下一行是标识此文档是一个 RSS 文档的 RSS 声明（此例是 RSS version 2.0）。

下一行含有 <channel> 元素。此元素用于描述 RSS feed。

<channel> 元素有三个必需的子元素：

<title> - 定义频道的标题。（比如 菜鸟教程首页）
<link> - 定义到达频道的超链接。（比如 www.runoob.com）
<description> - 描述此频道（比如 免费编程教程）
每个 <channel> 元素可拥有一个或多个 <item> 元素。

每个 <item> 元素可定义 RSS feed 中的一篇文章或 "story"。

<item> 元素拥有三个必需的子元素：

<title> - 定义项目的标题。（比如 RSS 教程）
<link> - 定义到达项目的超链接。（比如 http://www.runoob.com/rss）
<description> - 描述此项目（比如 菜鸟教程 Rss 教程）
最后，后面的两行关闭 <channel> 和 <rss> 元素。
```

- 注释

```xml
# 在 RSS 中书写注释的语法与 HTML 的语法类似：

<!-- 这是一个 RSS 注释 -->
```

```
RSS 使用 XML 来编写
因为 RSS 也是 XML，请记住：

所有的元素必许拥有关闭标签
元素对大小写敏感
元素必需被正确地嵌套
属性值必须带引号
```

- `<channel>` 元素

```xml
<channel> 元素可描述 RSS feed，而拥有三个必需的子元素：

<title> - 定义频道的标题。（比如 菜鸟教程首页）
<link> - 定义到达频道的超链接。（比如 http://www.runoob.com）
<description> - 描述此频道（比如 免费编程教程）
```

以下为 `<channel>`的子元素

- `<category>` 元素

```xml
<category> 子元素用于为 feed 规定种类。

<category> 子元素使 RSS 聚合器基于类别对网站进行分组成为可能。

上面的 RSS 文档的类别可能会是：

<category>Web 开发</category>
```

- `<copyright>` 元素

```xml
<copyright> 子元素会告知有关版本资料的信息。

上面的 RSS 文档的版本可能会是

<copyright>2006 Refsnes Data as. All rights reserved.</copyright>
```

- `<image>` 元素

```xml
<image> 子元素可在聚合器提供某个 feed 时显示一幅图像。

<image> 有三个必需的子元素：

<url> - 定义引用图像的 URL
<title> - 定义图像无法被显示时显示的文本
<link> - 定义到达提供此频道的网站的超链接

<image>
  <url>http://www.runoob.com/images/logo.png</url>
  <title>菜鸟教程</title>
  <link>http://www.runoob.com</link>
</image>
```

- `<language>` 元素

```xml
<language> 子元素用于规定用来编写文档的语言。

<language> 元素使 RSS 聚合器基于语言来对网站进行分组成为可能。

上面的 RSS 文档的语言可能是：

<language>zh-cn</language>
```

[了解更多元素请点击](http://www.runoob.com/rss/rss-channel.html)

- `<item>` 元素

```xml
每个 <item> 元素可定义 RSS feed 中的一篇文章或 "story"。
```

以下为 `<channel>`的子元素

- `<author>` 元素

```xml
author> 子元素用于规定一个项目的作者的电子邮件地址。

注释：为了防止垃圾邮件，一些开发者不会使用这个 <author> 元素。

上面的 RSS 文档中项目的作者可能是：

<author>admin@runoob.com</author>
```

- `<comments>` 元素

```xml
<comments> 子元素允许把一个项目连接到有关此项目的注释。

上面的 RSS 文档中项目的注释可能这样的：

<comments>http://www.runoob.com/comments</comments>
```

效果图：

![](https://ws1.sinaimg.cn/large/006OWbT9gy1fsuon2qz0jj30ni0gc75a.jpg)

- `<enclosure>` 元素

```xml
<enclosure> 子元素允许将一个媒体文件导入一个项中。

<enclosure> 元素有三个必需的属性：

url - 定义指向此媒体文件的 URL
length - 定义此媒体文件的长度（字节）
type - 定义媒体文件的类型
在上面的 RSS 文档中，被包含在项目中的媒体文件可能是这样的：

<enclosure url="http://www.runoob.com/rss/rss.mp3"
length="5000" type="audio/mpeg" />
```

[了解更多请点击](http://www.runoob.com/rss/rss-item.html)


- 发布 RssFeed

![](https://ws1.sinaimg.cn/large/006OWbT9gy1fsuoq0yfzej30ol0bkjsf.jpg)

- [Rss 阅读器](http://www.runoob.com/rss/rss-readers.html)

- [Rss 实例](http://www.runoob.com/rss/rss-examples.html)

- [Rss 参考手册](http://www.runoob.com/rss/rss-reference.html)