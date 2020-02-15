# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "smallwhispers/Wiki@gh-pages"
}

# 站点设置
site_name = "三刀魚"
site_logo = "${static_prefix}logo.png"
site_build_date = "2020-02-09T16:51+08:00"
author = "Anony"
email = "1046880355@qq.com"
author_homepage = "http://anony.pp.ua"
description = "你保护世界，我保护你。"
key_words = ['三刀魚', '科技', 'Anony', '学习', 'Wiki']
language = 'zh-CN'
external_links = [
    {
        "name": "三刀魚",
        "url": "http://anony.pp.ua",
        "brief": "🏄‍ Go My Own Way."
    },
    {
        "name": "小游戏",
        "url": "https://weigame.pp.ua",
        "brief": "放松小游戏"
    },
    {
        "name": "云盘",
        "url": "https://onedrive.pp.ua",
        "brief": "Anony的云盘"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitte",
        "url": "https://twitter.com/Cv2Ln",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/jhx520",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/2975939221/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''

valine = {
    "enable": True,
    "el": '#vcomments',
    "visitor": 'true',
    "avatar":'mp',
    "appId": "uM4TdSOqBxnHFm3gcy0VRcVC-gzGzoHsz",
    "appKey": "S8PiDx66GTKdtjwmQ5dMnCK6",
}