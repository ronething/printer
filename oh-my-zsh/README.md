<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Ubuntu 18.04 LTS 安装oh-my-zsh](#ubuntu-1804-lts-%E5%AE%89%E8%A3%85oh-my-zsh)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Ubuntu 18.04 LTS 安装oh-my-zsh

项目链接:https://github.com/robbyrussell/oh-my-zsh

根据官方提示,安装步骤如下：

先安装`zsh`

```sh
sudo apt-get install zsh
```

确保`curl`或者`wget`有被安装在系统上。`ubuntu`默认有安装。

还要安装`git`

```sh
sudo apt-get install git
```

接下来就可以安装`oh-my-zsh`了

```sh
通过 `curl`
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
或者通过`wget`
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
```

安装完成后退出终端，然后重启终端，没问题的话可以看到终端界面变了。

如果不行就重启系统或者注销。

---

安装之后的一些配置：

插件或者主题 

这里只对主题[`agnoster`](https://github.com/robbyrussell/oh-my-zsh/blob/master/themes/agnoster.zsh-theme)进行简单介绍

```sh
vim .zshrc
```

找到`ZSH_THEME="robbyrussell"`

修改`robbyrussell`为`agnoster`

重启终端即可。

然后应该会发现一些字符乱码，所以需要更换字体。

`poewrline/fonts`项目链接：https://github.com/powerline/fonts

按照官方说：

```sh
sudo apt-get install fonts-powerline
```

但是我的电脑上即使这样安装了也没有用。（找不到对应的字体）

所以只好手动安装。

```sh
# clone
git clone https://github.com/powerline/fonts.git --depth=1
# install
cd fonts
./install.sh
# clean-up a bit
cd ..
rm -rf fonts
```

这样安装之后在终端修改字体。

修改为`ubuntu mono derivative powerline regular`

![fonts](./pic/1.png)

如果嫌终端提示符`user@hostname`太长的话要去掉，可以编辑`~/.oh-my-zsh/themes/agnoster.zsh-theme`, 在文件最后找到`prompt_context`字段注释即可。

![hostname](./pic/2.png)

---

最后晒一张配置完成的终端图嘻嘻。

![terminal](./pic/3.png)