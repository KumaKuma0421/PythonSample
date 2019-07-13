"""
標準ライブラリ filecmp
"filecmp"はファイルやディレクトリを比較するためのライブラリです。
ファイルの比較には"cmp"函数を使用します。
"""

import filecmp

print(filecmp.cmp('./hoge.txt', './hogehoge.txt'))