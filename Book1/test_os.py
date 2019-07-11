"""
標準ライブラリ os
"OS"はOSに依存した機能を扱うためのライブラリです。
カレントディレクトリを調べたり、ファイルパスを分割したりする場合などに利用します。
"""

import sys
import os

# カレントディレクトリの取得
print(os.getcwd(), '\n')

# パス区切り文字の取得
print(os.sep, '\n')

# パスを親ディレクトリとファイルに分割
print(os.path.split(sys.argv[0]), '\n')

# パスを連結
print(os.path.join(os.getcwd(), 'hoge.py'), '\n')

# ファイル名を名前と拡張子に分割
print(os.path.splitext('hoge.py'), '\n')