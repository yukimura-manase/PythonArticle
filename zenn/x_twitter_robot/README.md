# X(旧: Twitter の Bot を作成する)

## 今回、作成する X(旧: Twitter) Bot の概要

1. 毎日、朝(9:00), 昼(12:00), 夕(19:00) の 3 回、投稿(定期実行)をする

2. 投稿する記事の選択は、ランダムに変わる

### 機能要件を分析する

1. 定期実行する機能

2. 自動投稿する機能

3. 投稿をランダムに選択する機能

4. 投稿文章を作成する機能

## 環境構築

1. tweepy を install する。

```bash
pip install tweepy
```

## API の利用の内容を提出

```md: 提出内容
I plan to use X's API to create an X bot that will automate the posting of some of my blog's content and blog URL.

The following link is a link to my blog.
https://masanyon.com/

We are planning to create the following functions.

1. At designated times in the morning, noon, and night, I will post posts that introduce the content of my blog and include URL links.
2. The content to be posted is randomly selected from among the articles each time.
```

```md: 提出内容 Ver. 日本語
X の API を使用して、ブログのコンテンツとブログ URL の一部の投稿を自動化する X ボットを作成する予定です。

以下のリンクは私のブログへのリンクです。
https://masanyon.com/

以下の機能を作成する予定です。

1. 朝、昼、夜の指定された時間に、ブログの内容を紹介し、URLリンクを記載した投稿を投稿します。
2. 掲載する内容は毎回記事の中からランダムに選択されます。
```

## 【参考・引用】
