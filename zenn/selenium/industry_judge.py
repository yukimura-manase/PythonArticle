
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback

### 作成・Module ########################################################

# 1. 電話番号(会社の代表番号: 固定電話)と会社名から「事業内容・業種」の情報を取得する

########################################################################

# 電話番号
tell = '050-5581-6910'  # 楽天株式会社・Tell

# 会社名
company_name = '楽天株式会社'

browser = webdriver.Chrome()

try:
    browser.get('https://www.google.com/')

    # 検索ボックスを見つける
    search_box = browser.find_element(By.ID, 'APjFqb')

    # 検索キーワード
    search_word = f'{company_name} {tell} 事業内容・業種'
    print(search_word)

    # 検索キーワードを入力
    search_box.send_keys(search_word)

    # 検索を実行する(Enterキーを送信して検索を実行)
    search_box.send_keys(Keys.RETURN)

    # submit() でも検索できる
    # search_box.submit()

    # 検索結果画面が表示されるまで待機
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'search'))
    )

    # description (説明文)のTextを格納する List
    search_result_list = []

    # 上から、3つまでの description (説明文)を取得する
    target_max = 3

    # find_elements で、検索結果の description (説明文)をすべて取得する
    description_lists = browser.find_elements(By.CLASS_NAME, 'VwiC3b')
    # print(description_lists)

    # 各要素の中の <span> タグからテキストを取得する (上から、3つまで)
    for index in range(len(description_lists)):
        try:
            if index + 1 > target_max:
                break
            else:
                element = description_lists[index]

                span_text = element.find_element(By.TAG_NAME, 'span').text
                print(span_text)
                print('-------------------------------------------------------------')
                search_result_list.append(span_text)

        except Exception as error:
            # 例外を無視したい場合は、pass を使用する
            pass

except Exception as error:
    # traceback.format_exc() で例外の詳細情報を取得する
    error_msg: str = traceback.format_exc()
    print(error_msg)
    pass


finally:
    # ブラウザを閉じる (エラーが発生しても必ず実行)
    browser.quit()
    print('取得した説明文・Text の List')
    print(search_result_list)
