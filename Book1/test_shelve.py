"""
標準ライブラリ shelve
"shelve"は、オブジェクトをファイルに保存して永続化するためのライブラリです。
このライブラリを使うと、辞書のようにキー／バリュー形式で手軽にデータを扱うことができます。
"""

import shelve

with shelve.open('mydb') as db:
    # データの保存
    db['Key1'] = 'Val1'
    db['Key2'] = 'Val2'
    db['Key3'] = 'Val3'

    # データの読み込み
    print(db['Key1'], db['Key2'], db['Key3'])