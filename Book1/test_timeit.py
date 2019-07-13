"""
標準ライブラリ timeit
"timeit"はちょっとしたスクリプトの実行時間を計測するためのライブラリです。
引数setupを使うと計測開始時に実行する処理を指定できます。
また、"timeit"函数はデフォルトでは指定した処理を100万回実行して計測するため
この回数を変更するには引数"number"を使います。
"""

import timeit

print(timeit.timeit('lst = [x for x in range(100)]'))

print(timeit.timeit('lst = [x for x in range(100)]', setup='print("start")', number=100))