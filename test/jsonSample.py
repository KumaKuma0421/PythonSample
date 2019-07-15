import json

# JSON形式のデータ
data = {
    "title": "JSON サンプル",
    "date": "2017. 07. 01",
    "items": [
        { "title": "タイトル １", "contents": "内容" },
        { "title": "タイトル ２", "contents": "内容" }
    ]
}

# ファイルに書き込む
save_path = "sample.json"
with open(save_path, "w") as outfile:
    json.dump(data, outfile, ensure_ascii = False)

# 文字列に変換する
json_str = json.dumps(data)
print(json_str)
json_str = json. dumps(data, ensure_ascii = False)
print(json_str)

#ローカルJSONファイルを読み込む
try:
    with open("sample.json","r") as f:
        data = json.load(f)
        print(data)
        print(data["title"])
        print(data["date"])
        print(data["items"])
except json.JSONDecodeError as e:
    print('JSONDecodeError:',e)