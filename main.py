#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2020/3/24 6:19 上午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : main.py

import pdfkit
import wechatsogou

options = {'encoding': 'utf-8'}
url = 'https://mp.weixin.qq.com/s/_aSsxFfaNW9FdAIq1ZYAEg'
ws_api = wechatsogou.WechatSogouAPI(captcha_break_time=3)

# 该方法根据文章url对html进行处理，使图片显示
content_info = ws_api.get_article_content(url)
# 得到html代码(代码不完整，需要加入head、body等标签)
html_code = content_info['content_html']
pdfkit.from_string(html_code, 'out.pdf', options=options)
