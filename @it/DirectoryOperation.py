#
# https://www.atmarkit.co.jp/ait/articles/1910/25/news021.html
# [Python入門] ディレクトリ操作の基本

import os

# カレントディレクトリの取得
pwd = os.getcwd()
print(pwd)

# カレントディレクトリの変更
os.chdir(".\\@IT")
print(os.getcwd())

# ディレクトリの内容の取得
os.chdir(pwd)
response = os.listdir(path=".")  # ファイル、ディレクトリのリストを返します。
for name in response:
    if os.path.isfile(name):
        print(f'file: {name}')
    else:
        print(f'dir: {name}')

for entry in os.scandir():
    if entry.is_file():
        print(f'file: {entry.name}')
    else:
        print(f'dir: {entry.name}')

# ディレクトリの新規作成
os.mkdir("TEST_1") # 存在しないパスが途中に入ると、FileNotFoundErrorが発生する。
os.makedirs("TEST_2\\TEST_2-1") # 強制的に途中パスの存在しないディレクトリも作る。

# 一時ファイルの作成
os.system('echo TEST > test.txt')
os.system('echo TEST > sample.txt')

# ファイルの削除
os.remove('test.txt')
os.unlink('sample.txt')

# ディレクトリの削除（どちらもディレクトリが空であることが前提）
# なので、system()で、rm -fr した方が楽かも
os.rmdir("TEST_1")
os.removedirs("TEST_2\\TEST_2-1")

# ファイル階層の走査
os.walk('C:\\Windows\\Temp', topdown=True)