#
# 配列・連想配列
#

# 配列の種類
#  タプル(tuple)
#   任意の数の要素を持つことができる配列。作成後の追加削除は不可。
#  リスト(list)
#   任意の数の要素を持つことができる配列。作成後の追加削除が可能。
#  ディクショナリ・辞書(dict)
#   任意の数の要素を持つことができる配列。keyとvalueのペアを一要素とします。
#   １つのディクショナリの中で同じkeyを持つことができない。
#  セット・集合(set)
#   任意の数の要素を持つことができる配列。作成後の追加削除が可能。
#   １つのセットの中で重複した要素を持つことができない。

# タプル

import datetime


def get_today():

    today = datetime.datetime.today()
    value = (today.year, today.month, today.day)  # ()を使用して、タプルを作成します。

    return value  # 複数の値を返す関数をタプルで実装する。


test_tuple = get_today()

print(test_tuple)
print(test_tuple[0])
print(test_tuple[1])
print(test_tuple[2])

# リスト

test_list_1 = ['python', '-', 'izm', '.', 'com']  # []を使用してリストを作成します。
print(test_list_1)
for i in test_list_1:
    print(i)

test_list_1.append(' Hallo!')
print(test_list_1)

test_list_1.insert(1, '--')
print(test_list_1)

test_list_1.remove('izm')
print(test_list_1)

# see also https://www.sejuku.net/blog/23044
try:
    test_list_1.remove('none')  # 見つからないと、ValueErrorを返します。
except ValueError:
    print("ValueErrorが発生しました。")
except:
    print("例外が発生しました。")
else:
    print("例外は発生しませんでした。")
finally:
    # 最終的にはどこを通ろうとも、ここは通過します。
    print("finally句です。")

removeKey = test_list_1.pop(2)
print(removeKey)
print(test_list_1)

searchIndex = test_list_1.index('com')
print("searchIndex:" + str(searchIndex))
print("count:" + str(test_list_1.count("python")))

# ディクショナリ

test_dict_1 = {"YEAR": "2010", "MONTH": "1", "DAY": "20"}
print(test_dict_1)

for i in test_dict_1:
    print("-----")
    print(i)  # key値が取れる
    print(test_dict_1[i])  # valueが取れる
    print(test_dict_1.get(i))  # valueが取れる
    print("-----")
