# 1 起步

## 1.1 起步 - 关于版本控制

- 版本控制

版本控制是一种记录一个或若干文件内容变化，以便将来查阅特定版本修订情况的系统。

使用版本控制系统通常还意味着，就算你乱来一气把整个项目中的文件改的改删的删，你也照样可以轻松恢复到原先的样子。 但额外增加的工作量却微乎其微。

- 本地版本控制系统

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1ft1apcx30oj20m80izab7.jpg)

- 集中化的版本控制系统

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1ft1apoaxkij20m80fg0u3.jpg)

- 分布式版本控制系统

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1ft1arfr9r6j20ik0m8dhk.jpg)

---

## 1.2 起步 - Git 简史

- [Git简史](https://git-scm.com/book/zh/v2/%E8%B5%B7%E6%AD%A5-Git-%E7%AE%80%E5%8F%B2)

---

## 1.3 起步 - Git 基础

- Git 基础

- 直接记录快照，而非差异比较

    - 非`git`的大部分版本控制系统

    ![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1ft1az1wl6ej20m808m758.jpg)

    > 这类系统（CVS、Subversion、Perforce、Bazaar 等等）将它们保存的信息看作是一组基本文件和每个文件随时间逐步累积的差异。

    - `git`版本控制系统

    ![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1ft1b0cu9cwj20m808h3zt.jpg)

    > 如果文件没有修改，Git 不再重新存储该文件，而是只保留一个链接指向之前存储的文件。 Git 对待数据更像是一个 快照流。

- 近乎所有操作都是本地执行

> 在 Git 中的绝大多数操作都只需要访问本地文件和资源，一般不需要来自网络上其它计算机的信息。

- Git 保证完整性

> Git 用以计算校验和的机制叫做 SHA-1 散列（hash，哈希）。

> 实际上，Git 数据库中保存的信息都是以文件内容的哈希值来索引，而不是文件名。

- Git 一般只添加数据

- 三种状态

> 已提交（committed）、已修改（modified）和已暂存（staged）

> Git 仓库、工作目录以及暂存区域。

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1ft1c5i62mij20m80c90tr.jpg)

```
Git 仓库目录是 Git 用来保存项目的元数据和对象数据库的地方。 这是 Git 中最重要的部分，从其它计算机克隆仓库时，拷贝的就是这里的数据。

工作目录是对项目的某个版本独立提取出来的内容。 这些从 Git 仓库的压缩数据库中提取出来的文件，放在磁盘上供你使用或修改。

暂存区域是一个文件，保存了下次将提交的文件列表信息，一般在 Git 仓库目录中。 有时候也被称作`‘索引’'，不过一般说法还是叫暂存区域。
```

- 基本的 Git 工作流程

1. 在工作目录中修改文件
2. 暂存文件，将文件的快照放入暂存区域。
3. 提交更新，找到暂存区域的文件，将快照永久性存储到 Git 仓库目录。

> 注：如果 Git 目录中保存着的特定版本文件，就属于已提交状态。 如果作了修改并已放入暂存区域，就属于已暂存状态。 如果自上次取出后，作了修改但还没有放到暂存区域，就是已修改状态。

---

## 1.4 起步 - 命令行

- [命令行](https://git-scm.com/book/zh/v2/%E8%B5%B7%E6%AD%A5-%E5%91%BD%E4%BB%A4%E8%A1%8C)

---

## 1.5 起步 - 安装 Git

- 向后兼容

```
向后兼容（Backward Compatibility），又称作向下兼容（Downward Compatibility）。在计算机中指在一个程序或者类库更新到较新的版本后，用旧的版本程序创建的文档或系统仍能被正常操作或使用，或在旧版本的类库的基础上开发的程序仍能正常编译运行的情况。
```

- 在 Linux 上安装

    - 如果以 Fedora 上为例，你可以使用 yum：
    
    ```sh
    $ sudo yum install git
    ```

    - 如果你在基于 Debian 的发行版上，请尝试用 apt-get：

    ```sh
    $ sudo apt install git
    ```

    [dowanload](http://git-scm.com/download/linux)

- 在 Mac 上安装

    - [download](http://git-scm.com/download/mac)

    - [download2](http://mac.github.com/)

- 在 Windows 上安装

    - [download](http://git-scm.com/download/win)

    - [download2](http://windows.github.com/)

- 从源代码安装

```
如果你想从源码安装 Git，需要安装 Git 依赖的库：curl、zlib、openssl、expat，还有libiconv。 如果你的系统上有 yum （如 Fedora）或者 apt-get（如基于 Debian 的系统）
```

```sh
$ sudo yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel
$ sudo apt-get install libcurl4-gnutls-dev libexpat1-dev gettext libz-dev libssl-dev

# 为了能够添加更多格式的文档（如 doc, html, info），你需要安装以下的依赖包：

$ sudo yum install asciidoc xmlto docbook2x
$ sudo apt-get install asciidoc xmlto docbook2x

```

[download](https://www.kernel.org/pub/software/scm/git)

[download2](https://github.com/git/git/releases)

```sh
$ tar -zxf git-2.0.0.tar.gz
$ cd git-2.0.0
$ make configure
$ ./configure --prefix=/usr
$ make all doc info
$ sudo make install install-doc install-html install-info
```

---

## 1.6 起步 - 初次运行 Git 前的配置

- 初次运行 Git 前的配置

```
Git 自带一个 git config 的工具来帮助设置控制 Git 外观和行为的配置变量。 这些变量存储在三个不同的位置：

/etc/gitconfig 文件: 包含系统上每一个用户及他们仓库的通用配置。 如果使用带有 --system 选项的 git config 时，它会从此文件读写配置变量。

~/.gitconfig 或 ~/.config/git/config 文件：只针对当前用户。 可以传递 --global 选项让 Git 读写此文件。

当前使用仓库的 Git 目录中的 config 文件（就是 .git/config）：针对该仓库。

每一个级别覆盖上一级别的配置，所以 .git/config 的配置变量会覆盖 /etc/gitconfig 中的配置变量。
```

- 用户信息(重要)

> 当安装完 Git 应该做的第一件事就是设置你的用户名称与邮件地址。

```
git config --global user.name "username"

git config --global user.email "username@example.com" 
```

- 文本编辑器

```sh
# Git 会使用操作系统默认的文本编辑器，通常是 Vim。 如果你想使用不同的文本编辑器，例如 Emacs，可以这样做：

$ git config --global core.editor emacs
```

- 检查配置信息

`git config --list`

`git config user.name`

---

## 1.7 起步 - 获取帮助

- 获取帮助

```sh
$ git help <verb>
$ git <verb> --help
$ man git-<verb>
```

举例：

`git help config`

---

## 1.8 起步 - 总结

> 现在，在你的个人系统中应该也有了一份能够工作的 Git 版本。是时候开始学习有关 Git 的基础知识了。
