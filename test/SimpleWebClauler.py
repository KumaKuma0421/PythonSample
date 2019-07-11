import re
from urllib.request import urlopen

# HTTPRequest型のクラスを取得する
f = urlopen ("http://www.yahoo.co.jp/")
content = f.read()
print (f.status)

decode_str = content[:1024].decode("ascii", errors="replace")

match = re.search (r"charset=['\']?([\w-]+)", decode_str)
if match:
    enc_type = match.group(1)
else:
    enc_type = "utf-8"
print (enc_type)

# エンコーディング種類の取得
enc_type = f.info().get_content_charset(failobj="utf-8")
print (enc_type)

# HTTPヘッダの取得
print (f.getheader("Content-Type"))


# HTTPレスポンス
data = f.read().decode(enc_type)
print (data)