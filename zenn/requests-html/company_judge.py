# from requests_html import HTMLSession
from requests_html import AsyncHTMLSession
import asyncio
import lxml.html

### 作成・Module ########################################################

# 1. 電話番号(会社の代表番号: 固定電話)から、会社名を判定したCSVファイルを作成する

########################################################################

# 電話番号
tell = '019-625-5205'

# 電話番号検索の Web サイト URL
phone_number_search_web = 'https://www.jpnumber.com/searchnumber.do'

# 検索パラメーター付きの URL
phone_number_search_web_url = f'https://www.jpnumber.com/searchnumber.do?number={tell}'
print('検索パラメーター付きの URL')
print(phone_number_search_web_url)

# HTMLSession の作成: スクレイピングを開始するには、まず HTMLSession オブジェクトを作成します
# session = HTMLSession()
# print(session)
async_session = AsyncHTMLSession()
print(async_session)
print('---------------------------------------------------')


async def exec_js():
    # ウェブページへのアクセス: get() メソッドを使用して、スクレイピングしたいウェブページにアクセスします。
    # response = session.get(phone_number_search_web_url)
    response = await async_session.get(phone_number_search_web_url)
    print(response)
    print('---------------------------------------------------')

    # JSも実行して、描画する
    await response.html.arender()

    print(response)
    print(response.html.find('div'))
    print('---------------------------------------------------')
    print(response.html.find('.result', first=True))
    print('---------------------------------------------------')
    print(response.html.find('.main-wrapper', first=True))
    print('---------------------------------------------------')
    print(response.html.find('#result-main-right > div.frame-728-orange-l > table > tbody > tr > td:nth-child(1) > div > dt:nth-child(2) > strong > a'))
    print('---------------------------------------------------')

    return response


loop = asyncio.get_event_loop()
loop.run_until_complete(exec_js())

# HTML 要素の検索と操作: レスポンスから特定のHTML要素を検索し、その内容を操作することができます。
# 例えば、find() メソッドを使って特定の要素を見つけることができます。
# elements = response.html.find('div')
# elements = page.html.find('#result-main-right > div.frame-728-orange-l > table > tbody > tr > td:nth-child(1) > div > dt:nth-child(2) > strong > a')
# print(elements)
# print('---------------------------------------------------')


# レンダリングされたJavaScriptの処理:
# requests-html は pyppeteer を内部的に利用しており、JavaScriptによってレンダリングされたコンテンツも扱うことが可能です。
# これには render() メソッドを使用します。


#
