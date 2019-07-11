"""
外部ライブラリ numpy
"numpy"は高度な数値演算（科学技術計算など）のためのライブラリで、
最も有名なPythonライブラリの一つです。
"""

import numpy as np

# １次元配列の生成
arr = np.asarray([1, 2, 3])
print('壱', arr)

# ２次元配列の生成
arr = np.asarray([[1, 2, 3], [4, 5, 6]])
print('弐', arr)

# 平均の取得
print('参', np.mean(arr))

# 最大値、最小値の取得
print('四', np.max(arr))
print('五', np.min(arr))

# 和の取得
print('六', np.sum(arr))

# 標準偏差の取得
print('七', np.std(arr))