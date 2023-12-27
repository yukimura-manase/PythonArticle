# 2. with構文を使用する場合: 定型の前処理・後処理が省略されるので、Codeがコンパクトになる。
with open('sample.txt', 'r') as f:
    result = f.read()
    print(result)

# `open()`という関数は`with`構文の処理に対応しているので、上記のように書き直すことができます。