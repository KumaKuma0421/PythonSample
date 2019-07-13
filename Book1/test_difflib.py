"""
標準ライブラリ difflib
"difflib"はシーケンスを比較するためのライブラリです。
テキスト内容を比較して差分を出力したり、差分をHTML形式で出力することもできます。
"""

import difflib
from pprint import pprint

txt1 = """
1,2,3,4,5
2,3,4,5,6
3,4,5,6,7
"""

txt2 = """
1,2,3,4,5
0,3,4,5,6
4,5,6,7,8
"""

# 差分の取得
d = difflib.Differ()
diff = d.compare(txt1.splitlines(), txt2.splitlines())
pprint(list(diff))

d2 = difflib.HtmlDiff()
print(d2.make_table(txt1.splitlines(), txt2.splitlines()))