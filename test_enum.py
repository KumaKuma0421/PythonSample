"""
標準ライブラリ enum
"enum"は列挙型を扱うためのライブラリです。
"""

from enum import Enum

# 定義
class Color(Enum):
    red = 1
    green = 2
    blue = 3

# 利用
print(Color.blue.name)
print(Color.blue.value)

# 簡略化した定義
Language = Enum('Language', 'jp en vn')
print(Language.jp.name)
print(Language.jp.value)