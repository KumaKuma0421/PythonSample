# 四則演算
test_integer = 100

print(test_integer + 10)
print(test_integer - 10)
print(test_integer * 10)
print(test_integer / 10)    # サンプルは10となっていたが、実際の出力は10.0になっている。

print(int(test_integer / 10))

test_string = '100.5'
print(float(test_string) + 100)

# 複素数
test_complex = 100 + 5j
print(test_complex)
print(test_complex.real)
print(test_complex.imag)
