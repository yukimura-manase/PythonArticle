# requests-html を使った Web スクレイピングの実践

## requests-html の概要(Summary)

[Requests-HTML](https://github.com/psf/requests-html) は、Web スクレイピングを簡単に操作にするモジュールである。
<br>
HTML のパースなどページを取り出して目的の要素を処理する。
<br>
Requests-HTML の作者である Kenneth Reitz 氏 は、HTTP クライアントインターフェースとして広く使われている Requests モジュールの作者でもある。
<br>
Requests-HTML は、ページに含まれているすべてのリンクやコンテンツ全体の他、HTML 要素の属性を知ることができる。

[Requests-HTML](https://github.com/psf/requests-html)の README.MD によると、次のように書かれている。

> このライブラリは、HTML の解析 (Web のスクレイピングなど) をできるだけシンプルかつ直感的に行うことを目的としています。
> このライブラリを使用すると、次のものが自動的に取得されます。
>
> - JavaScript サポート
> - CSS セレクター
> - XPath セレクター
> - Mock・ユーザーエージェント
> - リダイレクトの自動フォロー
> - 接続プール
> - Cookie の永続化
> - 非同期サポート
>
> 引用元: [Requests-HTML](https://github.com/psf/requests-html)

## 環境構築

1. requests-html を install する

```bash
pip install requests-html
```

```md
Python の requests_html を使って、次の Web ページの事業者名を取得する Code を作成してください。
https://www.jpnumber.com/searchnumber.do?number=019-625-5205
```
