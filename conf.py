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
    "type": "git",
    "url": "https://github.com/AlanDecode/Maverick-Theme-Kepler.git",
    "branch": "latest"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "kalong0126/blog-site@gh-pages"
}
category_by_folder = "True"
# 站点设置
site_name = "散人陈的个人博客"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "chinwer"
email = "kalong126@gmail.com"
author_homepage = "https://chinwer.top"
description = "存档专用"
key_words = ['Maverick', 'chinwer', 'Galileo', 'blog']
language = 'zh-CN'
external_links = [
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
        "name": "GitHub",
        "url": "https://github.com/kalong0126",
        "icon": "gi gi-github"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
