from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    # Chromium (Web Browser)のインスタンスを作成する
    browser = p.chromium.launch()
    print('browser: ', browser)
    ## 出力結果 ##
    # browser:  <Browser type=<BrowserType name=chromium executable_path=/Users/robotama/Library/Caches/ms-playwright/chromium-1091/chrome-mac/Chromium.app/Contents/MacOS/Chromium> version=120.0.6099.28>

    # 新しい・ページを作成する
    page = browser.new_page()
    print('page: ', page)
    ## 出力結果 ##
    # page:  <Page url='about:blank'>

    # page.goto() で Playwright のサイトにアクセス
    page.goto('https://playwright.dev/')

    # page.title() で title tag の値（タイトル）を取得している
    title = page.title()
    print(title)  # Fast and reliable end-to-end testing for modern web apps | Playwright

    # page.locator() を使ってセレクタを記述できるので，page.locator('.hero__title') で画面上部の「ヒーロー」を特定
    hero_title_text = page.locator('.hero__title').text_content()
    print(hero_title_text)  # Playwright enables reliable end-to-end testing for modern web apps.

    # page.screenshot() で、スクリーンショットを取得する　Ver. Lightモード
    page.screenshot(path='images/playwright-light.png')

    # toggleButton_gllPクラスの button 要素を取得して、Clickする => Darkモードにする
    page.locator('.toggleButton_gllP').click()

    # # page.screenshot() で、スクリーンショットを取得する　Ver. Darkモード
    page.screenshot(path='images/playwright-dark.png')

    # Browser を閉じる。
    browser.close()

## 参考・引用 ##
# 1. [Playwright for Python: ブラウザ操作を自動化しよう！](https://kakakakakku.hatenablog.com/entry/2022/10/24/091056)
