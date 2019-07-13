"""
標準ライブラリ sys
"sys"はPythonのインタプリタや実行環境に関する情報を扱うためのライブラリです。
プラットフォームを調べたり、スクリプトの起動パラメータを取得する場合などに利用します。
"""

import sys

# 機動パラメータの取得
print(sys.argv, '\n')

# モジュール検索パスの取得
print(sys.path, '\n')

# プラットフォームの取得
print(sys.platform)

# スクリプトの修了
sys.exit()
