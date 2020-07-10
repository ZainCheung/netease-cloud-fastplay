# 网易云音乐个性化纠正工具

简单来说就是可以快速增加指定歌曲的播放次数。

<p align="center">
    <a href="https://github.com/ZainCheung"><img alt="Author" src="https://img.shields.io/badge/author-ZainCheung-blueviolet"/></a>
    <img alt="PHP" src="https://img.shields.io/badge/code-Python-success"/>
    <img src="https://visitor-badge.glitch.me/badge?page_id=ZainCheung.netease-cloud-fastplay"/>
</p>



[📷 效果演示](#效果演示)

[🎁 下载地址](#下载地址)

[🔔 注意事项](#注意事项)

[🎨 项目结构](#项目结构)

[👻 免责声明](#免责声明)



------



# 效果演示

使用前可以看到两首歌分别是**92**次和**41**次

![使用前](https://s1.ax1x.com/2020/07/08/UZyQv8.png)

使用后两首各自涨了**300**首

![使用后](https://s1.ax1x.com/2020/07/08/UZyUCq.png)

有人可能会问上面那个累计播放次数**2218**首没有变化，那是因为总数的累计播放只计算不重复的歌曲。

调用的API地址是（这个API可以自己搭建）：

![](https://s1.ax1x.com/2020/07/08/UZ6geg.png)

打开软件填好账号密码（**MD5**）和**API**就可以开始执行任务了

软件的截图是这样

![](https://s1.ax1x.com/2020/07/10/UuoCMF.png)

这个歌单的`id`为`5101628912`，一共有三首歌，播放次数填写为`2`，点击开始执行后等待几秒钟便可以在软件下方的状态栏看到反馈。

# 下载地址

软件地址：[https://zaincheung.lanzous.com/i9HD9ehj29g](https://zaincheung.lanzous.com/i9HD9ehj29g)

软件项目地址：[https://github.com/ZainCheung/netease-cloud-fastplay](https://github.com/ZainCheung/netease-cloud-fastplay)

api接口项目地址：[https://github.com/ZainCheung/netease-cloud-api](https://github.com/ZainCheung/netease-cloud-api)

api的Demo演示地址：[https://netease-cloud-api.glitch.me](https://netease-cloud-api.glitch.me)

------



# 注意事项

### 1. API

API最好自己搭建，使用默认的API将会因为使用的人数较多导致**非常慢甚至进不去**，这个软件使用的API依旧是上次的API，只不过项目新增了接口，如果之前你搭建过就不需要重新搭建了，只需要复制项目的`index.php`文件的全部内容，然后粘贴到你的api项目里的`index.php`里面去，重启项目即可。

API项目最新地址：[https://github.com/ZainCheung/netease-cloud-api](https://github.com/ZainCheung/netease-cloud-api)

### 2. 密码

**密码必须自己前往MD5加密网站进行转换！！制作时选择32位小写！！！**

本软件不会将你的原文密码上传到服务器，请放心使用

在线“制作”MD5：[https://tool.chinaz.com/tools/md5.aspx](https://tool.chinaz.com/tools/md5.aspx)

### 3. 听歌次数

注意：播放次数不建议设置太大，可以先设置几十试试。

### 4. 初衷

这款软件的开发初衷是为了帮助使用过网易云音乐自动升级的用户，在系统推送不够精准的情况下进行自我纠正，通过增加某几首歌的播放次数可以告知系统你的听歌偏好，以便系统为你推荐你喜欢的歌单以及歌曲。

### 5. 其他

点击执行任务之前请不要打开或者删除日志文件和配置文件！

------

# 项目结构

```
|-- 项目文件夹
    |-- LICENSE
    |-- README.md
    |-- init.config
    |-- main.py
    |-- ui.py
    |-- api.py
    |-- requirements.txt
    |-- run.log
```

`LICENSE`：开源许可证

`README.md`：项目自述文件

`init.config`：配置文件

`main.py`：主程序

`ui.py`：界面模块

`api.py`：接口模块

`requirements.txt`：依赖清单

`run.log`：运行日志

# 免责声明

本项目的所有脚本、API以及软件仅用于个人学习开发测试，所有`网易云`相关字样版权属于网易公司，勿用于商业及非法用途，如产生法律纠纷与本人无关。

------

