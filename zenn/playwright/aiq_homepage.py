from playwright.sync_api import sync_playwright


AIQ_HOMEPAGE = 'https://www.aiqlab.com/'

with sync_playwright() as p:

    # Chromium (Web Browser)のインスタンスを作成する
    browser = p.chromium.launch()

    # 新しい・ページを作成する
    page = browser.new_page()

    # page.goto() で Playwright のサイトにアクセス
    page.goto(AIQ_HOMEPAGE)

    # titleタグを取得する
    title = page.title()
    print(title)

    mv__title = page.locator('.s-mv__title').text_content()
    print(mv__title)  # 特許技術AIが新たな産業DXを成し遂げる

    page.screenshot(path='images/aiq-homepage.jpg')

    print(page.get_by_alt_text("AIQ株式会社"))
    # print(page.get_by_alt_text("AIQ株式会社").frame_locator())
    # <Locator frame=<Frame name= url='https://www.aiqlab.com/'> selector='internal:attr=[alt="AIQ株式会社"i]'>

    print(page.get_by_text('特許技術', exact=True))
    # <Locator frame=<Frame name= url='https://www.aiqlab.com/'> selector='internal:text="\\u7279\\u8a31\\u6280\\u8853"s'>

    # Browser を閉じる。
    browser.close()
