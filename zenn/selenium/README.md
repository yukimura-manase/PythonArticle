# Selenium を使った Web スクレイピングの実践

## Selenium の概要(Summary)

- Selenium は、主に Web アプリケーションのブラウザ操作を自動化するためのテストフレームワークです。
- ブラウザでの操作を自動化するスクリプトを作成することができるため、テスト自動化だけでなく、Web スクレイピングにも使用されます。
- Selenium の主な特徴とメリット、デメリットは、次のとおりです。

### 特徴

1. オープンソース: Selenium はオープンソースのテストフレームワークで、無償で利用することができます。

2. ブラウザの操作自動化: Web ブラウザの操作を自動化し、ユーザーのアクションをシミュレートすることが可能です。

3. 多言語対応: Python の他にも、Java、C#、Ruby など複数のプログラミング言語でスクリプトを記述できます。

4. クロスブラウザテスト: 複数のブラウザでテストを実行することが可能です。

### メリット

1. 豊富なオプション: 様々なテストニーズに対応できる幅広いオプションが利用可能です。
2. サポート環境の幅広さ: 多様なブラウザや OS で動作し、幅広いテストシナリオに対応しています。

### デメリット

1. ブラウザ操作に限定: Web ブラウザの操作以外は実行できないため、それ以外の環境では使用できません。

2. 実行時間: 高機能である一方、処理に時間がかかる場合があります。

### まとめ

Selenium は、Web アプリケーションのテスト自動化において非常に有効なツールですが、使用する際にはその特徴と限界を理解し、適切に活用することが重要です。

## 環境構築

1. Selenium を install する

```bash
pip install selenium
```

2. ChromeDriver を install する

```bash
brew install chromedriver
```

3. ChromeDriver の バージョン情報を確認する

```bash
chromedriver --version

## [出力結果] ##
# ChromeDriver 120.0.6099.109 (3419140ab665596f21b385ce136419fde0924272-refs/branch-heads/6099@{#1483})
```

4. pip で install することもできる

```bash
pip install chromedriver-binary==110.0.5481.77
```

5. Docker で Selenium & ChromeDriver の環境構築

```Dockerfile
FROM python:3-alpine

ENV PYTHONIOENCODING utf-8
WORKDIR /app

RUN apk add --update \
        wget \
    # Add chromium and dependences
        udev \
        ttf-freefont \
        chromium \
        chromium-chromedriver \
    # Add Japanese font
    && mkdir noto \
    && wget -P /app/noto https://noto-website.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip \
    && unzip /app/noto/NotoSansCJKjp-hinted.zip -d /app/noto \
    && mkdir -p /usr/share/fonts/noto \
    && cp /app/noto/*.otf /usr/share/fonts/noto \
    && chmod 644 -R /usr/share/fonts/noto/ \
    && fc-cache -fv \
    && rm -rf /app/noto \
    # Add selenium
    && pip install selenium
```

## [参考・引用]

1. [chromedriver mac インストール](https://xs735978.xsrv.jp/692.html)

2. [【Python】Chromedriver を pip コマンドでインストールする方法](https://pineplanter.moo.jp/non-it-salaryman/2023/04/13/py-chromedriver-pip/)

3. [ChromeDriver - WebDriver for Chrome](https://chromedriver.chromium.org/downloads)

4. [[selenium 向け] ChromeDriver を pip でインストールする方法（パス通し不要、バージョン指定可能）](https://qiita.com/hanzawak/items/2ab4d2a333d6be6ac760)

5. [Selenium×docker でテスト自動化してみた](https://zenn.dev/carenet/articles/4ca98b5e35bb24)
