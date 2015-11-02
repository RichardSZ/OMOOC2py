# DISQUS 私人教程

## 背景
Win7家庭版操作系统
github帐号：
gitbook帐号：
把disqus作为一个插件安装到gitbook，使得gitbook具有读者评论功能。

## 安装

首先进入disqus官方网站：https://disqus.com/。
首先显示的是登录页面，右上角有log in(登录）和sign up(注册）两个按键。
还没有帐号的情况下，选择sign up(注册）按键，鼠标左键点击该按键。
进入sign up(注册）页面，
页面提示你可通过用户已有的FB,TW,或者Google帐户注册，
也可通过邮件地址注册。
选择通过邮件地址注册，页面有三个输入框，分别是：
Name：disqus 上的用户名， 用户自己设定;
Email：用户的邮件地址，用于以后登录;
Password：用户自定义的登录密码
点击sign up按键，即完成了disqus帐号的注册。

还没完，请继续。
登录disqus之后，请点击右上角齿轮(setting)按键，
出现一个下拉菜单。
选择“add disqus to site”
进入engage页面，点击“start using Engage”按键，
来到“Add Disqus to your site”页面，
输入site name，
自动选择site name生成一个unique disqus url
在category里选择一个合适的内容分类。
点击右下角“finish registration”
就完成了个人站点的注册和设立。
此时会自动跳转到https://site name(站点名).disqus.com
页面上方有start engage set up 和learn,
选择set up,
选择advanced,
在trust domain 里一行输入一个网址如下: 
gitbook.com
gitbooks.io

在页面下方点击"save changes"完成设置

在gitbook 里面安装disqus插件。
登录gitbook, 点击上方help，进入官方bangzhu帮助文档。
在第一章format的第十三小节1.13就是plugins插件的使用和安装。
选择该小节，首先就是“how to find plugins”，并给出了一个网址：plugins .gitbook.com
xuanze该选择网址，即可找到disqus的对应plugin插件.
To use the Disqus plugin in your Gitbook project, add the disqus plugin to the  book.json  file, along with your shortname (you create a shortname for disqus by creating a new website on the disqus.com website)
{
    "plugins": ["disqus"],
    "pluginsConfig": {
        "disqus": {
            "shortName": "XXXXXXX"
        }
    }
}

注意，上述plugin插件无法直接从plugins网站上拷贝粘贴到github的book.json文件中。需要先粘贴到写字板notepad中，再粘贴到book.json才能成功。这可能是因为在plugins网站上的代码内容有一些格式控制符是github不接受的。

 








## 使用

## 体验

