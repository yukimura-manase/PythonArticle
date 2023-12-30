import requests
from bs4 import BeautifulSoup

### 作成・Module ########################################################

# 1. 『阿部 寛のホームページ』から情報を取得する Module

########################################################################

abe_hiroshi_homepage = 'http://abehiroshi.la.coocan.jp/'

# URLからHTMLを取得
response = requests.get(abe_hiroshi_homepage)
html_content = response.text
print(html_content)
print('---------------------------------------------------')

# BeautifulSoupを使用してHTMLを解析
soup = BeautifulSoup(html_content, "html.parser")
print(soup)
print('---------------------------------------------------')

# CSS のセレクターと同じ記述で、HTMLタグを取得することができる
h1_title_tag = soup.select('h1')
print(h1_title_tag)

# 阿部寛の誕生日・データ
abe_hiroshi_birthday = soup.select('body > table > tbody > tr:nth-child(1) > td:nth-child(1) > table > tbody > tr:nth-child(2) > td:nth-child(2)')

print(abe_hiroshi_birthday)
