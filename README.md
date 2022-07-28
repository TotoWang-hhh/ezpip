# Easy PyPI帮助

## 认识Easy PyPI

Easy PyPI可以理解为pip.exe的图形化扩展，它的大部分功能仍基于pip.exe，如果您愿意，可以将其缩写为为ezpip或者pipui。

Easy PyPI是我最高产的软件之一，您需要经常查看[我的博客](https://www.cnblogs.com/totowang)来检查是否有新版存在。

新推出的1.4可以说是我最引以为傲的程序之一，它可以在您完全不看代码的情况下帮助您装好一切必须的库，我会在详细的介绍中讲解如何使用。

## 关于帮助文档

这是与软件配套的帮助文档，您可以在此在线查阅几乎一切您需要的信息。

本文档站基于Docsify，这是一个能够实时将MarkDown文件转换为HTML网页，并呈现在各位眼前的网站，更重要的是，我可以0成本搭建它，而且它的界面通俗易懂。

因为CHM繁琐的编写流程令我抓狂，所以我不得不更换帮助文档的平台，这样就有了您眼前的这些。

### 如何查阅

不知道读到这里的各位都是什么不凡的神仙，我会在这些文档里尽可能详细地介绍整个软件，您所需要做的，就是在左边的目录中挑选一个标题，或者小标题，然后单击它，最后看向右边并读完您想了解的内容。

### 在文档中查找

您可以按下<kbd>Ctrl</kbd>+<kbd>F</kbd>来调用浏览器自带的页面内查找功能，这样可以在文档中进行查找。

### 旧版文档

在这篇文档撰写完成之前，还有一个旧版本文档，如果您需要查看，请[通过此链接前往旧版文档](http://rgzz.great-site.net/soft/ezpip/WebHelp/)。

### 下载文档

如果处于设备性能或网络连接等原因，您无法正常浏览该文档或需要下载以离线阅读，您可以下载该目录下的`HELP.MD`，这是这篇文档的所有内容，但是您还需要[一个不错的Markdown阅读器](https://typora.io)来打开它。

请注意：我没有为本地阅读的文档做任何修改，您将会读到一份一模一样的副本。

# 界面与功能说明

让我们以软件的重要部分——界面为顺序，讲完所有功能。

## 界面概要

我在大部分内容上使用了系统样式的控件，以便于让自己更专注于根本，并且会让软件毫无违和感地存在于每个系统（我希望大家喜欢）。软件的主界面可以分为许多部分，我会在这部分将它们整理清晰。

## 输入框

嘿，看见界面顶部的小白条了吗？哦！不是标题栏，您看下面一排，那就是输入框呢！通常情况下，输入框用于输入库名，但如果您注意到过调试选项，那你可能会发现它的[另类使用方法](#使用内建网页查看器打开输入的网址)。

### 巧用输入框

- 您可以直接将版本要求写在库名后面，例：`requests>=2.1`。（顺便一提：这不是什么小功能，而是我最近发现的一个巧合）
- 输入网址，然后利用调试功能来用内建网页查看器内打开和浏览网页，详见[使用内建网页查看器打开输入的网址](#使用内建网页查看器打开输入的网址)。

## 功能区

这里包含软件所有主要的功能，它们非常实用，接下来我会一一介绍。

我不希望读者会读到任何冗余内容，所以我提前告诉您，这部分基本上没用！

### 针对指定库的功能

要使用这些功能，您只需要在[输入框](#输入框)输入库名，并点击对应的功能即可。

#### 安装

本功能可以调用pip.exe安装您输入的库，我使用了豆瓣镜像源，这是为了让下载更快。

#### 以管理员身份安装（1.4.0）

1.3发布后的某一天，我遇到了问题：当我试图安装一些库时，setup.py会提示权限不足，需要带上--user参数，于是我就索性将这个功能添加到了Easy PyPI。因为时间仓促，这个功能的实现十分简陋，只是简简单单地带上`--user`参数，相信我，我会在后面的版本（也许……真正的1.4.1？）中修改解决方案。

#### 卸载

本功能可以卸载已经安装的库，这很简单，您只需要输入库名，点击此功能，然后确认即可，您可以在弹出确认框时反悔。

请注意：如果您使用的是1.4.0之前的版本，则需要留意控制台或者弹出的命令行窗口，然后输入`y`或`n`来确认或取消卸载操作。


#### 关于此库

这个功能可以用内建网页查看器来显示该库在PyPI官网上的信息。

### 针对pip.exe和Easy PyPI的功能

您不需要使用[输入框](#输入框)即可使用这些功能

#### 列出所有已安装的库

这可以列出您安装过的所有库，由于程序只是调用了pip.exe，所以您需要全程注意命令行。

#### 提权

点击此功能，软件即可提权，之后您可以安装需要管理员权限才能安装的库。如果此按钮被禁用，则说明无需再次提权。

#### 更新PIP

这个功能会更新PIP至最新版，我仍然采用了豆瓣镜像源。

#### 关于PIP

这回输出PIP的版本和路径。

#### 查看环境变量中有关PIP路径的配置

这会直接运行`where pip`和`where pip3`。

#### 根据Python源码安装依赖

本功能可以直接根据`.py`文件安装一切依赖，本功能为该版本特色功能。

点击后你需要选中一个`.py`文件，然后程序会自动识别需要的库（并非完全可靠）。这之后您需要选择您想安装的库，最后确认并等待安装完成即可。

#### 显示（隐藏）调试选项

这个功能可以显示[调试选项](#调试选项)

## 软件信息和反馈按钮

您可以将这一部分理解成软件的“关于”页面，您可以进入我的网站，也可以进行反馈或查看帮助，您甚至可以阅读软件使用的开源许可！

只要您在读这些文本，那么您大概率知道这些功能是做什么的。

## 调试选项

这些选项是用来调试软件的，除非遇到问题，否则您无需太在意。如果您需要了解这些选项，请继续阅读。

在某些时候，如果您遇到了任何Bug、崩溃等，可以通过软件内置的调试功能来进行故障排除。其实在最初，调试功能是我临时开发的。

调试功能在目前的版本中作用不大，主要是为了在早期版本中更好地排除错误。

### 显示输入的内容

单击此按钮之后，可以在控制台输出您在输入框内输入的内容

### 使用内建网页查看器打开输入的网址。

您可以在[输入框](#输入框)内键入网址。

### 显示调试信息

单击后您可以查看更详（多）细（余）的输出信息。
