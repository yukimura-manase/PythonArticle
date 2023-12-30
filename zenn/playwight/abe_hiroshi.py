from playwright.sync_api import sync_playwright, expect

expect.set_options(timeout=0)

### 作成・Module ########################################################

# 1. 『阿部 寛のホームページ』から情報を取得する Module

########################################################################

abe_hiroshi_homepage = 'http://abehiroshi.la.coocan.jp/'

with sync_playwright() as p:

    # Chromium (Web Browser)のインスタンスを作成する
    browser = p.chromium.launch()

    # 新しい・ページを作成する
    page = browser.new_page()

    # page.goto() で Playwright のサイトにアクセス
    page.goto(abe_hiroshi_homepage)

    # ページのHTMLを取得する
    html_content = page.content()
    print(html_content)  # 『阿部 寛のホームページ』のHTML を出力する

    # titleタグを取得する
    title = page.title()
    print(title)  # 阿部寛のホームページ

    # page.screenshot() で、『阿部 寛のホームページ』のスクリーンショットを取得する
    page.screenshot(path='images/abe-hiroshi-homepage.jpg')

    # # 特定の要素のテキストを取得する Ver. 完全一致
    text_locator = page.get_by_text('生年月日', exact=True)
    print(text_locator)  # <Locator frame=<Frame name= url='http://abehiroshi.la.coocan.jp/'> selector='internal:text="/^\\u751f\\u5e74\\u6708\\u65e5$/"i'>
    print(type(text_locator))  # <class 'playwright.sync_api._generated.Locator'>

    # Browser を閉じる。
    browser.close()
