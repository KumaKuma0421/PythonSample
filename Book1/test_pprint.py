"""
標準ライブラリ pprint
"pprint"は、データ構造を見やすい形で出力するためのライブラリです。
"""
from pprint import pprint

data = [(i, {'hoge':'HOGE', 'fuga':'FUGA'}) for i in range(3)]

# printで出力
print(data)

# pprintで出力
pprint(data)

# 出力画面の幅に応じて出力調整
pprint(data, compact=True)