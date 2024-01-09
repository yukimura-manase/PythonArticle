# Playwright で スクレイピングを試す

## Playwright・概要 (Summary)

1. Playwright は、エンドツーエンド(E2E)のテストのニーズに対応するために、Microsoft によって、特別に作成されました。

   - Playwright は、Chromium、WebKit、Firefox などの最新のレンダリング エンジンをすべてサポートしています。

   - Windows、Linux、macOS 上で、ローカルまたは CI 上で、ヘッドレスまたはネイティブ モバイル エミュレーションを使用したヘッドでテストします。

2. E2E テストのためのツールとして開発されましたが、Web スクレイピングに使用にも適しています。

- 詳細は、参考・引用の記事を見ていただきたいのですが、[2021 年現在、Puppeteer を使う理由はなくなった。Playwright を使おう。](https://zenn.dev/yusukeiwaki/articles/db1cd8d7aa87ed)などが参考になります。

## システム・要件

1. Python 3.8 以降。

2. Windows 10 以降、Windows Server 2016 以降、または Windows Subsystem for Linux (WSL)。

3. MacOS 12 モントレーまたは MacOS 13 ベンチュラ。

4. Debian 11、Debian 12、Ubuntu 20.04、または Ubuntu 22.04。

## 環境構築

1. Playwright Pytest プラグインを install する。

```bash
pip install pytest-playwright
```

2. 必要なブラウザを install する。

```bash
playwright install
```

## 環境構築 Ver. Docker

```bash
docker pull mcr.microsoft.com/playwright/python:latest
```

## 【参考・引用】

1. [Playwright for Python (Doc) の Installation](https://playwright.dev/python/docs/intro#installing-playwright)

2. [Playwright for Python (Doc) の Installatio Ver. Docker](https://playwright.dev/python/docs/docker)

3. [playwright-python GitHub](https://github.com/microsoft/playwright-python)

4. [2021 年現在、Puppeteer を使う理由はなくなった。Playwright を使おう。](https://zenn.dev/yusukeiwaki/articles/db1cd8d7aa87ed)

5. [Python でスクレイピングする際のライブラリ選定など・調査まとめ](https://zenn.dev/manase/scraps/944f0f7a703e52)

## おまけ情報

- LangChain のツール中には、PlayWright をベースとしたツールである PlayWright Browser Toolkit というものが、あるみたいです。

1. [PlayWright Browser Toolkit で Web スクレイピングを試してみた](https://www.keywalker.co.jp/blog/playwright-browser-toolkit_web-scraping.html)

2. [PlayWright Browser](https://python.langchain.com/docs/integrations/toolkits/playwright)
