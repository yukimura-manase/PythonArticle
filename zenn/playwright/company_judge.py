from playwright.sync_api import sync_playwright

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

with sync_playwright() as p:

    # Chromium (Web Browser)のインスタンスを作成する
    browser = p.chromium.launch()

    # 新しい・ページを作成する
    page = browser.new_page()

    # page.goto() で Playwright のサイトにアクセス
    page.goto(phone_number_search_web_url)

    result_text = page.locator('.result').text_content()
    print(result_text)

    # #result-main-right > div.frame-728-orange-l > table > tbody > tr > td:nth-child(1) > div > dt:nth-child(2) > strong > a

    # html_content = page.content()  # ページのHTMLを取得
    # print(html_content)  # HTMLの内容を表示

    # Locator を使用して、Page内のHTML要素を取得する

    # 特定の要素のテキストを取得する
    # text = page.get_by_text("事業者名：")
    # print(text)
    # print(type(text))

    # Browser を閉じる。
    browser.close()


## 参考・引用 ##

# 1. [Playright Locator](https://playwright.dev/python/docs/locators)
