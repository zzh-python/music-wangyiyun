 ![spider163 logo](https://github.com/Chengyumeng/spider163/blob/master/logo.jpeg)
# spider163
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)][license] [![pyversions](https://img.shields.io/github/tag/Chengyumeng/Spider163.svg)][releases] [![pyversions](https://img.shields.io/pypi/pyversions/spider163.svg)][pyversions] [![Build Status](https://travis-ci.org/chengyumeng/spider163.svg?branch=master)][buildstatus]

[license]: https://github.com/Chengyumeng/spider163/blob/master/LICENSE

[releases]:https://github.com/Chengyumeng/spider163/releases

[pyversions]:https://pypi.python.org/pypi/spider163

[buildstatus]:https://travis-ci.org/chengyumeng/spider163

###### GitHub上最易用的网易云音乐爬虫系统


## 安装模块
- 第一步：指定SPIDER163_PATH环境变量，缺省情况下为$HOME/spider163
- 第二步：把默认配置文件spider163.conf拷贝到SPIDER163_PATH下，并配置数据库
- 第三步：pip install spider163
- spider163 --help

## 历史文档
- [不重要，2018年spider163发布的5个版本](https://mp.weixin.qq.com/s/pim5tYPHd0zBTKYQaijkbQ)
- [Spider163同时支持python2.x和python3.x的演进之路](https://mp.weixin.qq.com/s/FFoD3gKM5touGVbvKebRlA)
- [Spider163支持下载网易付费歌曲了](https://mp.weixin.qq.com/s/L8uvPV_CiAS6vcnaOaifJw)
- [非重磅 | 网易云音乐爬虫Spider163更新v2.0](https://mp.weixin.qq.com/s?__biz=MzI2NTMxMDYxMg==&mid=2247483955&idx=1&sn=c1d8a38b4929cb298fc6172cf894e641&chksm=ea9e1ac8dde993de1d6095d000f289389ee92609bccebda3d2ebc88bfa1939eceb6b94cc3fce&scene=38#wechat_redirect)
- ...


## 使用指南

```console
$ spider163 initdb
$ # 根据配置文件的数据库信息自动创建数据库表，删除全部数据通过resetdb实现
```
```console
$ spider163 resetdb
$ # 重建相关数据库
```
```console
$ spider163 updatedb
$ # 根据时间重置过期数据重新抓取
```
```console
$ spider163 classify
$ # 获取已知曲风列表
```
```console
$ spider163 playlist
$ # 默认下载全部推荐歌单（1000+），也可以通过指定页码去下载（-p=1）,以及歌曲风格（--classify=小语种，默认为全部）
```
```console
$ spider163 mp3 --playlist=2033391777
$ # 默认下载指定歌单列表内的全部包含版权的歌曲
```
```console
$ spider163 music
$ # 默认下载10个歌单的歌曲数据，也可以通过指定循环大小（-c=2）来下载10 * c 个歌单内歌曲
```
```console
$ spider163 comment
$ # 默认根据数据库存储的未下载歌曲随机下载一首单曲的评论，也可以通过-c指定需要下载的单曲数量和-s强制指定歌曲id
$ # spider163 comment -c 10 | spider163 comment -s 209115
```
```console
$ spider163 lyric --count=10
$ # 抓取10首音乐的歌词，可以通过制定歌曲ID抓取特定一首音乐（--song）
```
```console
$ spider163 search -q="林依晨"
$ # 搜索功能（待完善，暂支持歌曲搜索）
```
```console
$ spider163 get -s 209115
$ # 阅读歌曲基本信息、歌词、热评
```
```console
$ spider163 get --playlist 922064582
$ # 获取歌单的基本信息、歌曲等
```
```console
$ spider163 doc --playlist 922064582
$ # 歌单/歌曲信息汇总成word文档
```
```console
$ spider163 top50 --playlist 922064582 --username=xxx --password=xxx
$ # 创建TOP 50 歌单
```


## TODO
- [2018 Q2](https://github.com/Chengyumeng/spider163/blob/master/doc/2018.Q2.TODO.md)
- [2018 Q1](https://github.com/Chengyumeng/spider163/blob/master/doc/2018.Q1.TODO.md)
- [2017 Q4](https://github.com/Chengyumeng/spider163/blob/master/doc/2017.Q4.TODO.md)
- ...

# 欢迎关注微信公众账号：程天写代码
![guojingcoooool](https://github.com/Chengyumeng/spider163/blob/master/wechat.jpeg)
