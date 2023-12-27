## with文に対応する Class を定義する ##

# ファイルの処理で利用したopen()関数はPythonの組み込み関数（定義済み関数）で、デフォルトでwith文に対応しているため、特に事前準備がなくてもwith文を使うことができました。

# with文に対応するようなオブジェクトは自分でも独自に作成することができます。 

# `open()`と似たような処理を、自分で書いてみることにします。

# with文で利用できる、Classを作成する条件は、`__enter__()`メソッドと`__exit__()`メソッドを実装することです。

class CustomFileReader:
    def __init__(self, filename):
        print('init Block')
        self.filename = filename
        self.file = None

    # 1. __enter__(): with文で利用されるオブジェクトの前処理を定義する
    def __enter__(self):
        """ with文で最初に呼ばれる処理 """
        print('enter Block')
        self.file = open(self.filename, 'r')
        return self.file

    # 2. __exit__(): with文で利用されるオブジェクトの後処理を定義する
    def __exit__(self, exc_type, exc_value, traceback):
        """ withブロックから抜ける時の処理 """
        print(f'exit Block: {exc_type}, {exc_value}, {traceback}')
        self.file.close()

if __name__ == '__main__':
    with CustomFileReader('sample.txt') as f:
        print(f.read())

## [ 実行結果 ] ##
# init Block
# enter Block
# Hellow Python!
# exit Block: None, None, None

# このサンプルの出力からもわかるように、with文に対応したMyFileReaderクラスの処理は、次のように動きます。

# インスタンスのイニシャライズを行う（init）
# 前処理を動かす（enter）
# withブロック内の処理を実行する（f.read）
# 後処理を実行する（exit）
# ここで、__enter__と__exit__の役割をもう少し詳しくみてみます。


## 1. __enter__の役割 ##

# __enter__は、with文で利用されるオブジェクトの処理の前処理を行います。

# with文にターゲット（with 〜 as f: の f の部分）を指定した場合には、`__enter__()`の戻り値(実行結果)がそのターゲットに指定された変数に代入されて利用できます。

# そのため、戻り値は、これが実装されたクラスのインスタンスを返すように設定することが多いです。

# `CustomFileReader`では、開いたファイルオブジェクトを返しているので、withブロック内ではこの`f`に対してファイルの操作を実行していることになります。

## 2. __exit__の役割 ##

# __exit__では後処理の部分を担います。

#  withブロック内の処理を行った後にこちらのメソッドが呼び出され、withブロック内で発生した例外の処理もこちらに記述することができます。

# __exit__には３つの引数を持たせることができます。ここにwithブロック内の例外のデータが入ってきますが、うまくいっていればすべてNoneが返ってきます。

# exc_type: 例外の型
# exc_value: 例外の値
# traceback: 例外のtraceback

# 注意点として、__exit__メソッド内での例外は、withブロックの中身で発生した例外のみ扱えるので、
# たとえば、with文自体で実行している処理（open()メソッドなど）の処理のエラー処理は行いません。
# 指定されたファイルが存在しないなどのエラーは__exit__に届く前に処理されます。

# 実際に__exit__メソッドでエラーを処理するパターンも確認してみます。

