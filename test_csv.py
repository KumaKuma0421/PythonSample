"""
標準ライブラリ csv
"csv"はCSVを扱うためのライブラリです。
"""

import csv

try:
    # ファイルを開く
    with open('hoge.csv', 'w') as csvfile:

        # writerオブジェクトの作成
        writer = csv.writer(csvfile, lineterminator = '\n')
        
        # 内容の書き込み
        writer.writerow(['a', 'b', 'c'])
        writer.writerow(['あ', 'い', 'う'])

except FileNotFoundError as e:
    print(e)

except csv.Error as e:
    print(e)


try:
    # ファイルを開く
    with open('hoge.csv') as csvfile:

        # readオブジェクトの作成
        reader = csv.reader(csvfile)

        # 内容の読み込み
        for r in reader:
            print(r)

except FileNotFoundError as e:
    print(e)

except csv.Error as e:
    print(e)