# Beautiful Soup で スクレイピングを試す

## Web スクレイピングの 3 Step (Web スクレイピング基礎知識)

基本的にスクレイピングは、次のような３ステップで行われます。

1. WEB サイトの HTML などのデータ取得

2. データの抽出

   - 複雑な構造の HTML データを解析し、必要な情報だけを抽出します。

3. データの保存・活用

   - 抽出した情報をデータベースやファイルなどに保存または、処理で活用します。

## Beautiful Soup 概要 (Summary)

- Python のスクレイピングによく使われるライブラリとしては、Requests, Beautiful Soup, Selenium, などがあります。

1. Requests: HTTP・HTTPS 通信をするためのモジュール

   - HTML データの取得によく用いられます。

   - Python では Requests を利用して、簡単に WEB サイトからデータを自動的に取得することができます。

2. Beautiful Soup: HTML などからデータを抽出するためのモジュール

3. Selenium: ブラウザを操作し、データを取得するために使用するモジュール

   - プログラムからブラウザを操作できるので、Test などでも使われる。

   - ブラウザを操作してデータを取得しますので、動作が遅いことが難点です。

### WEB スクレイピングに利用する、3 つのライブラリの役割

WEB スクレイピングの３ステップの中で、それぞれのライブラリがどこで使われるのかをまとめると次のようになります。

| ライブラリ     | 1. データの取得 | 2. データの抽出 | 3. データの保存 |
| -------------- | :-------------: | :-------------: | :-------------: |
| Requests       |        ◯        |                 |                 |
| Beautiful Soup |                 |        ◯        |                 |
| Selenium       |        ◯        |        ◯        |        ◯        |

### 結論: Web スクレイピングでは Requests & Beautiful Soup

Q: Selenium と Requests & Beautiful Soup のタッグ、どちらを使うのが望ましいのか？

A: パフォーマンスの観点から、Web スクレイピングでは Requests & Beautiful Soup のタッグを使うのが望ましい。

## 環境構築

1. beautifulsoup を install する。

```bash
pip install beautifulsoup4
```

2. requests を install する

```bash
pip install requests
```

## 【参考・引用】

1. [図解！Python BeautifulSoup の使い方を徹底解説！(select、find、find_all、インストール、スクレイピングなど)](https://ai-inter1.com/beautifulsoup_1/)
