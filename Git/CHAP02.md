# Git 基础

## 2.1 Git 基础 - 获取 Git 仓库

- 两种方法

- 获取 Git 仓库

    - 两种方法
        - 在现有项目或目录下导入所有文件到 Git 中

        - 从一个服务器克隆一个现有的 Git 仓库

    - 在现有目录中初始化仓库

    如果你打算使用 Git 来对现有的项目进行管理，你只需要进入该项目目录并输入：

    ```sh
    $ git init
    ```

    该命令将创建一个名为 .git 的子目录，这个子目录含有你初始化的 Git 仓库中所有的必须文件，这些文件是 Git 仓库的骨干。不过我们仅仅是做了一个初始化的操作，你的项目里的文件还没有被跟踪。你可通过 `git add` 命令来实现对指定文件的跟踪，然后执行 `git commit` 提交：

    ```sh
    $ git add *.c
    $ git add LICENSE
    $ git commit -m 'initial project version'
    ```

    - 克隆现有的仓库

    克隆仓库的命令格式是 `git clone [url]`

    ```sh
    # use ssh
    git clone git@github.com:ronething/notes.git
    # use https
    git clone https://github.com/ronething/notes.git
    ```

    如果你想在克隆远程仓库的时候，自定义本地仓库的名字，你可以使用如下命令：

    ```sh
    # use ssh
    git clone git@github.com:ronething/notes.git myproject
    # use https
    git clone https://github.com/ronething/notes.git myproject
    ```

---

## 2.2 Git 基础 - 记录每次更新到仓库

- 记录每次更新到仓库

> 文件都不外乎这两种状态：已跟踪或未跟踪。

> 初次克隆某个仓库的时候，工作目录中的所有文件都属于已跟踪文件，并处于未修改状态。

- 使用 Git 时文件的生命周期如下：

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1ft1jqs3rjlj20m8096q3n.jpg)

- 检查当前文件状态

    ```sh
    $ git status
    ```

    ```sh
    # 如果在克隆仓库后立即使用此命令，会看到类似这样的输出：
    
    $ git status On branch master nothing to commit, working directory clean

    # 现在，分支名是 “master”,这是默认的分支名。
    ```

    未跟踪的文件出现在 `Untracked files` 下面。

- 跟踪新文件

    ```sh
    $ git add README
    ```

    此时再运行 `git status` 命令，会看到 README 文件已被跟踪，并处于暂存状态

    只要在 `Changes to be committed` 这行下面的，就说明是已暂存状态。

    `git add` 命令使用文件或目录的路径作为参数；如果参数是目录的路径，该命令将递归地跟踪该目录下的所有文件。

- 暂存已修改文件

    出现在 `Changes not staged for commit` 这行下面，说明已跟踪文件的内容发生了变化，但还没有放到暂存区。

    将`git add`这个命令理解为"添加内容到下一次提交中"而不是"将一个文件添加到项目中"要更加合适。

    运行了`git add`之后又作了修订的文件，需要重新运行`git add`把最新版本重新暂存起来。(不然提交上去的文件就是最后一次运行`git add`命令是的那个版本)

- 状态简览

    `git status -s` or `git status --short`

    ```sh
    $ git status -s
    M README
    MM Rakefile
    A  lib/git.rb
    M  lib/simplegit.rb
    ?? LICENSE.txt
    ```

    ```
    新添加的未跟踪文件前面有 ?? 标记，新添加到暂存区中的文件前面有 A 标记，修改过的文件前面有 M 标记。 你可能注意到了 M 有两个可以出现的位置，出现在右边的 M 表示该文件被修改了但是还没放入暂存区，出现在靠左边的 M 表示该文件被修改了并放入了暂存区。 
    ```

    ```
    例如，上面的状态报告显示： README 文件在工作区被修改了但是还没有将修改后的文件放入暂存区,lib/simplegit.rb 文件被修改了并将修改后的文件放入了暂存区。 而 Rakefile 在工作区被修改并提交到暂存区后又在工作区中被修改了，所以在暂存区和工作区都有该文件被修改了的记录。
    ```

- 忽略文件（重要）

    创建`.gitignore`文件

    ```
    *.[oa]
    *~
    ```

    一行告诉 Git 忽略所有以 .o 或 .a 结尾的文件。一般这类对象文件和存档文件都是编译过程中出现的。 第二行告诉 Git 忽略所有以波浪符（~）结尾的文件。

    文件 .gitignore 的格式规范如下：

    - 所有空行或者以 ＃ 开头的行都会被 Git 忽略。

    - 可以使用标准的 glob 模式匹配。

    - 匹配模式可以以（/）开头防止递归。

    - 匹配模式可以以（/）结尾指定目录。

    - 要忽略指定模式以外的文件或目录，可以在模式前加上惊叹号（!）取反。

    ```
    所谓的 glob 模式是指 shell 所使用的简化了的正则表达式。 星号（*）匹配零个或多个任意字符；[abc] 匹配任何一个列在方括号中的字符（这个例子要么匹配一个 a，要么匹配一个 b，要么匹配一个 c）；问号（?）只匹配一个任意字符；如果在方括号中使用短划线分隔两个字符，表示所有在这两个字符范围内的都可以匹配（比如 [0-9] 表示匹配所有 0 到 9 的数字）。 使用两个星号（*) 表示匹配任意中间目录，比如`a/**/z` 可以匹配 a/z, a/b/z 或 `a/b/c/z`等。
    ```

    ```sh
    # no .a files
    *.a

    # but do track lib.a, even though you're ignoring .a files above
    !lib.a

    # only ignore the TODO file in the current directory, not subdir/TODO
    /TODO

    # ignore all files in the build/ directory
    build/

    # ignore doc/notes.txt, but not doc/server/arch.txt
    doc/*.txt

    # ignore all .pdf files in the doc/ directory
    doc/**/*.pdf
    ```

    GitHub 有一个十分详细的针对数十种项目及语言的 `.gitignore` 文件列表 [链接](https://github.com/github/gitignore )

- 查看已暂存和未暂存的修改

    如果想知道具体修改了什么地方，可以用`git diff`命令。

    要查看尚未暂存的文件更新了哪些部分，不加参数直接输入 `git diff`

    此命令比较的是工作目录中当前文件和暂存区域快照之间的差异， 也就是修改之后还没有暂存起来的变化内容。

    若要查看已暂存的将要添加到下次提交里的内容，可以用 `git diff --cached` 命令。Git 1.6.1 及更高版本还允许使用 `git diff --staged`。

    也可以用`git difftool`命令等输出`diff`分析结果，更加直观。

- 提交更新

    `$ git commit`

    这种方式会启动文本编辑器以便输入本次提交的说明。 (默认会启用 shell 的环境变量 $EDITOR 所指定的软件，一般都是 vim 或 emacs。也可使用 `git config --global core.editor` 命令设定默认编辑器。)

    添加 -m 选项，将提交信息与命令放在同一行,即`git commit -m "commit messages"`

- 跳过使用暂存区域

    只要在提交的时候，给 `git commit` 加上 `-a` 选项，Git 就会自动把所有已经跟踪过的文件暂存起来一并提交，从而跳过 `git add` 步骤

- 移除文件

    删除本地文件和暂存区域中的记录

    - 第一种方法
    ```sh
    touch test
    git add test
    rm test
    git rm test
    ```
    - 第二种方法(亲测可行)
    ```sh
    touch test
    git add test
    rm test
    git add .
    ```

    不删除本地文件和但是删除文件在暂存区域中的记录(加上`cached`选项)

    ```sh
    $ git rm --cached README
    ```

    例子：

    ```sh
    # 因为 Git 有它自己的文件模式扩展匹配方式，所以我们不用 shell 来帮忙展开。 (-f为force强制删除选项)

    $ git rm -f log/\*.log

    $ git rm -f \*~
    ```

- 移动文件

    `$ git mv file_from file_to`

    相当于

    ```sh
    $ mv README.md README
    $ git rm README.md
    $ git add README
    ```

---

## 2.3 Git 基础 - 查看提交历史

`git log`

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1ft28hfs312j20ma08gjrp.jpg)

> `-p`，用来显示每次提交的内容差异

> `-n`,显示最近n次提交，例如`-2`表示显示最近两次提交

> `--stat`，显示每次提交的简略的统计信息

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1ft28osg2hqj20m806bglq.jpg)

> `--pretty`，可以指定使用不同于默认格式的方式展示提交历史。比如用 `oneline` 将每个提交放在一行显示，查看的提交数很大时非常有用。 另外还有 `short`，`full` 和 `fuller` 可以用，展示的信息或多或少有些不同。`format`，可以定制要显示的记录格式。

- `git log --pretty=format` 常用的选项

选项|说明
:-|:-
%H|提交对象（commit）的完整哈希字串
%h|提交对象的简短哈希字串
%T|树对象（tree）的完整哈希字串
%t|树对象的简短哈希字串
%P|父对象（parent）的完整哈希字串
%p|父对象的简短哈希字串
%an|作者（author）的名字
%ae|作者的电子邮件地址
%ad|作者修订日期（可以用 --date= 选项定制格式）
%ar|作者修订日期，按多久以前的方式显示
%cn|提交者（committer）的名字
%ce|提交者的电子邮件地址
%cd|提交日期
%cr|提交日期，按多久以前的方式显示
%s|提交说明

例如: `$ git log --pretty=format:"%h - %an, %ar : %s" -1`

```sh
$ git log --pretty=format:"%h - %an, %ar : %s" -1
e277a2a - ronething, 12 hours ago : update
```

- 作者(author)和提交者(committer)之间的区别:

> 其实作者指的是实际作出修改的人，提交者指的是最后将此工作成果提交到仓库的人。 所以，当你为某个项目发布补丁，然后某个核心成员将你的补丁并入项目时，你就是作者，而那个核心成员就是提交者。

> 当 `oneline` 或 `format` 与另一个 log 选项 `--graph` 结合使用时尤其有用。 这个选项添加了一些ASCII字符串来形象地展示你的分支、合并历史：

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1ft291kw82pj20lh08mweu.jpg)

- `git log` 的常用选项

选项|说明
:-|:-
-p|按补丁格式显示每个更新之间的差异。
--stat|显示每次更新的文件修改统计信息。
--shortstat|只显示 --stat 中最后的行数修改添加移除统计。
--name-only|仅在提交信息后显示已修改的文件清单。
--name-status|显示新增、修改、删除的文件清单。
--abbrev-commit|仅显示 SHA-1 的前几个字符，而非所有的 40 个字符。
--relative-date|使用较短的相对时间显示（比如，“2 weeks ago”）。
--graph|显示 ASCII 图形表示的分支合并历史。
--pretty|使用其他格式显示历史提交信息。可用的选项包括 oneline，short，full，fuller 和 format（后跟指定格式）。

- 限制输出长度

> 限制输出长度的选项，也就是只输出部分提交信息

> 按照时间作限制的选项， `--since` 和 `--until`

- 列出所有最近两周内的提交：

`$ git log --since=2.weeks`

> 该命令也可以这样用。比如说具体的某一天 "2008-01-15"，或者是相对地多久以前 "2 years 1 day 3 minutes ago"

> 用 `--author` 选项显示指定作者的提交，用 `--grep` 选项搜索提交说明中的关键字。 （请注意，如果要得到同时满足这两个选项搜索条件的提交，就必须用 `--all-match` 选项。否则，满足任意一个条件的提交都会被匹配出来）

> `-S`，可以列出那些添加或移除了某些字符串的提交。 比如说，你想找出添加或移除了某一个特定函数的引用的提交，你可以这样使用：`$ git log -Sfunction_name`

> 如果只关心某些文件或者目录的历史提交，可以在 git log 选项的最后指定它们的路径。 因为是放在最后位置上的选项，所以用两个短划线（--）隔开之前的选项和后面限定的路径名(其实不要也可以。。亲测可行)

![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1ft29hns50bj20k10a074q.jpg)

- 限制 `git log` 输出的选项

选项|说明
:-|:-
-(n)|仅显示最近的 n 条提交
--since, --after|仅显示指定时间之后的提交
--until, --before|仅显示指定时间之前的提交
--author|仅显示指定作者相关的提交
--committer|仅显示指定提交者相关的提交
--grep|仅显示含指定关键字的提交
-S|仅显示添加或移除了某个关键字的提交

---

## 2.4 Git 基础 - 撤消操作

- 撤消操作

> 有时候我们提交完了才发现漏掉了几个文件没有添加，或者提交信息写错了。 此时，可以运行带有 `--amend` 选项的提交命令尝试重新提交：

`$ git commit --amend`

- 取消暂存的文件

> 例如，你已经修改了两个文件并且想要将它们作为两次独立的修改提交，但是却意外地输入了 git add * 暂存了它们两个。 如何只取消暂存两个中的一个呢？

> 第一种(官方文档):

```sh
$ git add *
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

    renamed:    README.md -> README
    modified:   CONTRIBUTING.md

# 在 “Changes to be committed” 文字正下方，提示使用 git reset HEAD <file>... 来取消暂存。 所以，我们可以这样来取消暂存 CONTRIBUTING.md 文件：

$ git reset HEAD CONTRIBUTING.md
Unstaged changes after reset:
M	CONTRIBUTING.md
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

    renamed:    README.md -> README

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

    modified:   CONTRIBUTING.md
```

> 第二种(个人认为这样也行):

```sh
touch test1
touch test2
git add .
$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   test1
        new file:   test2

$ git rm --cached test2
rm 'test2'

$ ls -l test*
-rw-r--r-- 1 Administrator 197121 0 Jul  8 11:04 test1
-rw-r--r-- 1 Administrator 197121 0 Jul  8 11:04 test2

$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   test1

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        test2

```

- 撤消对文件的修改

`git checkout -- [file]`

> 注:你需要知道 `git checkout -- [file]` 是一个危险的命令，这很重要。 你对那个文件做的任何修改都会消失 - 你只是拷贝了另一个文件来覆盖它。 除非你确实清楚不想要那个文件了，否则不要使用这个命令。

> 在 Git 中任何 已提交的 东西几乎总是可以恢复的。 甚至那些被删除的分支中的提交或使用 `--amend` 选项覆盖的提交也可以恢复。然而，任何未提交的东西丢失后很可能再也找不到了。

---

## 2.5 Git 基础 - 远程仓库的使用

- 远程仓库的使用

- 查看远程仓库

`git remote` 默认可以看到`origin`

- 添加远程仓库

`git remote add <shortname> <url>`

- 从远程仓库中抓取与拉取

`$ git fetch [remote-name]`

> 运行 `git pull` 通常会从最初克隆的服务器上抓取数据并自动尝试合并到当前所在的分支。`git fetch`也会将数据拉去到本地仓库，但是不会自动合并。

- 推送到远程仓库

`git push [remote-name] [branch-name]`

