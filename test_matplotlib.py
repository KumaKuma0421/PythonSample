"""
外部ライブラリ matplotlib
"matplotlib"はデータをグラフ化するためのライブラリです。
"""

#import matplotlib
import matplotlib.pyplot as p
#matplotlib.use('TkAgg')

x = [1,2,3,4,5,6,7]
y = [9,1,5,8,6,2,4]

p.plot(x, y)
p.title('Sample')
p.legend()
p.show()

p.plot([1,2,3,4,5],[9,1,5,8,6], label='GraphA')
p.plot([5,4,3,2,1],[5,5,1,2,4], label='GraphB')
p.title('GraphTitle')
p.xlabel('X-Axis')
p.ylabel('Y-Axis')
p.legend()
p.show()