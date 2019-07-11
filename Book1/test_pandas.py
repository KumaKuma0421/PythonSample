"""
外部ライブラリ pandas
"pandas"はデータ分析用の外部ラリブラリです。
"""

import pandas as pd

# データフレームの作成
df = pd.DataFrame([
    ['001', 'amada', '神奈川'],
    ['002', 'masaru', '沖縄'],
    ['003', 'satoru', 'スペイン']],
    columns=['ID', '名前', '出身地'])

# CSVファイルの作成
df.to_csv('./hoge.csv', index=False)