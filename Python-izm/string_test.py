# -------1---------2---------3---------4---------5---------6---------7---------8

# Pythonの文字列はシングルクォーテーションとダブルクォーテーション
# が使用できます。
print("パイソン サンプル。")
print('パイソン サンプル。')

# クォート記号３つで複数行に分けて書くこともできる。
test_string = """
パイソンサンプル１
パイソンサンプル２
パイソンサンプル３
"""
print(test_string)

# 文字列の連結は＋を使用する。
print("This is a " + "test string.")

# 変数に対しては＋＝も可能
test_string = "012"
test_string += "345"

print(test_string)

# * は繰り返し回数を表す。
test_string = "123" * 3
print(test_string)

# 文字列への変換は str() を使用する。
test_integer = 100
print(str(test_integer) + "円")

# 文字列の置換は replace() を使用する。
test_string = "Apple Banana Orange"
print(test_string.replace("Apple", "Grape"))

# 文字列の分割は split() を使用する。
print(test_string.split(" "))

# 文字列の桁揃えは rjust() を使用する。
# 第一引数が埋めた後の桁数
# 第二引数が埋め込む文字列 ゼロ以外も埋め込み可能
test_string = "12345"

print(test_string.rjust(10, '0'))
print(test_string.rjust(10, "!"))

# 0で桁埋めする場合は zfill() を使用する。
test_string = "12345"

print(test_string.zfill(10))
print(test_string.zfill(5))
print(test_string.zfill(3))

# 文字列の検索
test_string = "python sample string."

print(test_string.startswith("python"))
print(test_string.startswith("java"))

print("s" in test_string)
print("z" in test_string)

# 大文字・小文字変換
print(test_string.upper())
print(test_string.lower())

# 先頭・末尾の削除 rstrip() lstrip()
test_string = "This is a sample python string."
test_string = test_string.rstrip(".")
print(test_string)
test_string = test_string.rstrip("string")
print(test_string)
test_string = test_string.rstrip()
print(test_string)
