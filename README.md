# wechat_article_url_to_pdf
根据微信文章链接地址生成 PDF

## 依赖
- pdfkit
  - wkhtmltopdf
- wechatsogou

需要根据 [pdfkit](https://github.com/JazzCore/python-pdfkit) 项目自行安装 wkhtmltopdf。

再安装项目依赖：

```python
pip install -r requirements.txt 
```

## 代码

```python
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
```

## 效果

![image-20200324063856106](https://klause-blog-pictures.oss-cn-shanghai.aliyuncs.com/ipic/2020-03-23-223856.png)