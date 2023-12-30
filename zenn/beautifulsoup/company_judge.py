import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

### 作成・Module ########################################################

# 1. 電話番号(会社の代表番号: 固定電話)から、会社名を判定したCSVファイルを作成する

########################################################################

# 電話番号
tell = '019-625-5205'

# 電話番号検索の Web サイト URL
PHONE_NUMBER_SEARCH_WEB = 'https://www.jpnumber.com/searchnumber.do'

# 検索パラメーター付きの URL
PHONE_NUMBER_SEARCH_WEB_URL = f'https://www.jpnumber.com/searchnumber.do?number={tell}'
print('検索パラメーター付きの URL')


# URLからHTMLを取得
# response = requests.get(PHONE_NUMBER_SEARCH_WEB_URL)

session = HTMLSession()
response = session.get('https://www.example.com')

# JavaScriptを実行してHTMLをレンダリング
response.html.render()

# HTMLコンテンツを文字列として、取得する
text_html_content = response.text
print(text_html_content)
print(type(text_html_content))
print('---------------------------------------------------')

# BeautifulSoupを使用してHTMLを解析する
soup = BeautifulSoup(text_html_content, "html.parser")
# print(soup)
# print(type(soup))
# print('---------------------------------------------------')

search_result_content = soup.select('.content')
print(search_result_content)
print('---------------------------------------------------')
