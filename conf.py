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
    "name": "Kepler",
    "type": "local",
    "path": "../Kepler"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "smallwhispers/Wiki@gh-pages"
}

# 站点设置
site_name = "秋刀鱼"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "Anony"
email = "1046880355@qq.com"
author_homepage = "https://janony.tk"
description = "你保护世界，我保护你。"
key_words = ['科技', 'Anony', '心得', 'Wiki']
language = 'zh-CN'
external_links = [
    {
        "name": "主页",
        "url": "http://anony.pp.ua",
        "brief": "🏄‍ Go My Own Way."
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
        "name": "Twitter",
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
