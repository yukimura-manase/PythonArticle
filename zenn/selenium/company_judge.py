from selenium import webdriver
from selenium.webdriver.common.by import By
import traceback
from selenium.webdriver.chrome.options import Options

### 作成・Module ########################################################

# 1. 電話番号(会社の代表番号: 固定電話)から、会社名を特定する

########################################################################

# 電話番号
tell = '050-5581-6910'  # 楽天株式会社・Tell

# 電話番号検索の Web サイト URL に 検索パラメーター(電話番号)を付与する
phone_number_search_web_url = f'https://www.jpnumber.com/searchnumber.do?number={tell}'
print('検索パラメーター付きの URL')
print(phone_number_search_web_url)

try:
    # Chrome Browser Instance
    browser = webdriver.Chrome()
    # ページに移動する
    browser.get(phone_number_search_web_url)

    # 会社名の要素を取得する
    result_element = browser.find_element(By.XPATH, '//*[@id="result-main-right"]/div[2]/table/tbody/tr/td[1]/div/dt[2]/strong/a')
    print(result_element.text)

    # 会社名を取得する
    result = result_element.text

except Exception as error:
    # traceback.format_exc() で例外の詳細情報を取得する
    error_msg: str = traceback.format_exc()
    print(error_msg)
    # 例外を無視したい場合は、pass を使用する
    pass


finally:
    # ブラウザを閉じる (エラーが発生しても必ず実行)
    browser.quit()
    print('処理完了')
