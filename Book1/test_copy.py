"""
標準ライブラリ copy
"copy"はオブジェクトの浅いコピーや深いコピーを行うためのライブラリです。
"""
import copy

# 浅いコピー
x = [[1, 2, 3], 4, 5]
y = copy.copy(x)
y[0][0] = 100
print('浅いコピー', x, y)

# 深いコピー
xx = [[1, 2, 3], 4, 5]
yy = copy.deepcopy(xx)
yy[0][0] = 100
print('深いコピー', xx, yy)