import requests
from bs4 import BeautifulSoup

AIQ_HOMEPAGE = 'https://www.aiqlab.com/'

# URLからHTMLを取得
response = requests.get(AIQ_HOMEPAGE)

# HTMLコンテンツを文字列として、取得する
text_html_content = response.text
print(text_html_content)
print(type(text_html_content))
print('---------------------------------------------------')

# BeautifulSoupを使用してHTMLを解析する: BeautifulSoup(解析対象のHTML/XML, 利用するパーサー)
soup = BeautifulSoup(text_html_content, "html.parser")
print(soup)
print(type(soup))
print('---------------------------------------------------')

# CSS のセレクターと同じ記述で、HTMLタグを取得することができる
h1_title_tag = soup.select('h1')
print(h1_title_tag)
print('---------------------------------------------------')

# 特定の CSS class を持つタグを取得する
title_tag = soup.select('.s-mv__title')
print(title_tag)
print('---------------------------------------------------')

# タグから、テキストのみを取得する
title_text = title_tag[0].get_text()
print(title_text)
print('---------------------------------------------------')

# 'c-header__logo' CSS class のタグの中にある imgタグを取得する
img_tag = soup.select('.c-header__logo img')
print(img_tag)
print('---------------------------------------------------')

# SVGを書き出せたが、Access 拒否でエラー
# img_url = img_tag[0]['src']
# img_response = requests.get(AIQ_HOMEPAGE + img_url)
# with open('downloaded_image.svg', 'wb') as f:
#     f.write(img_response.content)
