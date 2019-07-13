"""
標準ライブラリ tempfile
"tempfile"は一時的なファイルやディレクトリを作成するためのライブラリです。
いわゆる「中間生成物」を扱う際に利用します。
"""

import tempfile
import os

# 一時ファイルの作成
with tempfile.TemporaryDirectory() as temp_path:
    print(temp_path)
    with open(os.path.join(temp_path, 'hoge.txt'), 'w') as f:
        # 一時ファイルが存在することを確認
        print(os.path.exists(os.path.join(temp_path, 'hoge.txt')))

# 一時ファイルが消去されたことを確認
print(temp_path)
print(os.path.exists(os.path.join(temp_path, 'hoge.txt')))