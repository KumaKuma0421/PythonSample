#
# https://ids.itmedia.jp/dl/atmarkit_ebook63_python.pdf?bpc=d6dc8f55bd03cc6f81aee8a0ba0f4de587080890295458de634bf80d601e996f#_ga=2.250632772.319519459.1593822754-1596501829.1592975760
#
# Python チートシート
#

# 制御構造 if文 for文 while文 break文 continue文
# Python は、switch文がありません。

condition = 12

if condition == 11:
    print('condition is 11.')
elif condition == 12:
    print('condition is 12.')
elif condition == 13:
    print('condition is 13.')
else:
    print('unknown value.')

myList = list(range(5))
for num in myList:
    if num % 2 == 0:  # 偶数の場合
        print(f'{num}は偶数です。')
    else:
        print(f'{num}は奇数です。')
else:
    print('リストアップが終了しました。')  # breakが行使された場合は通らない。

counter = 0
while counter < 5:
    print(counter)
    counter += 1
else:
    print('finished')

# 三項演算子

a = 1
x = 'foo' if a == 1 else 'bar'
y = 'insider' if a == 0 else 'outsider' if x == 'foo' else 'border'
print(y)

# 関数定義の基本


def some_function(value1, value2, opt1=True):
    print(value1)
    if opt1 == True:
        print(value2)
    return True


some_function('test', 'sample')


def variable_function(value1, value2, *args, **kwargs):
    print(value1)
    print(value2)
    print(args)
    print(kwargs)
    return


# 可変長位置引数はargsにタプルとして、可変長キーワード引数はkwargsに連想配列として入る。
variable_function("test1", "test2", 1, 2, 3, a=1, b=2)

# ラムダ式 lambda パラメータリスト: 式 ※式は単一の式しか利用できない。小規模な内容にしか対応できない。
myList = list(range(5))
newList = list(map(lambda x: x ** 2, myList))

# 上のラムダ式と同じ内容


def square(x):
    return x ** 2


myList = list(range(5))
newList = list(map(square, myList))

# 上のラムダ式をリスト内包表記で行う。
myList = list(range(5))
newList = [x ** 2 for x in myList]


def function01(x, y, z): return x * y * z
def function02(x, y, z): return x + y + z


response01 = function01(1, 2, 3)
response02 = function02(1, 2, 3)
responseFuncs = [response01, response02]
retA = responseFuncs[0]
retB = responseFuncs[1]