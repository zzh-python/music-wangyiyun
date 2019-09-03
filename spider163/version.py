# -*- coding: utf-8 -*-
import os
import sys

PYTHON3 = False
if sys.version > "3":
    PYTHON3 = True

VERSION = "2.7.8"
DESCRIPTION = ""
root_path = os.path.dirname(os.path.abspath(__file__))

MAILBODY = """
<h2 style="color: #C20C0C; margin: 10px 0;"><a href="https://github.com/Chengyumeng/spider163" target="_blank">Spider163</a> 云音乐今日精彩推荐(微信公众号：pod1024)</h2>
<h2 style="color: #C20C0C; margin: 10px 0;"></h2>
<p  style="color: #C10B0B; margin: 10px 0;" >今日分享 {} 摘编歌曲：</p>
<ul>{}</ul>
<div style="margin: 20px 0 0 0;">
<p style="font-weight: 400;font-style: normal;font-size: 30px;color: #333;text-align: center;margin: 30px auto;">欢迎关注程天写代码微信公众号：pod1024</p>
</div>
"""

MAILMUSIC = """
<li><span style="font-weight: bold; margin: 2px 10px 5px 10px;"><a href="http://music.163.com/#/song?id={}" target="_blank">{}</a></span>
<span style="font-weight: bold; margin: 2px 10px 5px 10px;">{}</span> 
<span style="font-weight: bold; margin: 2px 10px 5px 10px;">评论数：{}</span></li><hr>
{}
"""

MAILCOMMENT = """
<p><span style="font-weight: bold; margin: 2px 10px 5px 10px;color: #a40011;">{}</span>
<span style="font-weight: bold; margin: 2px 10px 5px 10px;color:">{} :</span> </p>
<p style="margin: 12px 20px 15px 20px;">{}</p>
"""
