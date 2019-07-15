"""
ふっけいメールの内容を解析する
"種別","場所","内容","日付","受信日時","メール本文"
"""
import csv

baseDirectory = "/home/user01/Download/"
fileNames = (
    "fukkeimail_2014.csv",
    "fukkeimail_2015.csv",
    "fukkeimail_2016.csv",
    "fukkeimail_2017.csv",
    "fukkeimail_2018.csv",
    "fukkeimail_2019.csv")

for fileName in fileNames:
    fullPath = baseDirectory + fileName

    # ファイルのオープン
    csvData = open(fullPath, "r", encoding='shift-jis', errors="", newline="")

    # リスト形式で取得
    # dataList = csv.reader(
    #             csvData,
    #             delimiter=",",
    #             doublequote=True,
    #             lineterminator="\r\n",
    #             quotechar='"',
    #             skipinitialspace=True)
    # for row in dataList:
    #     print(row[0], row[1], row[2], row[3], row[4])

    # 辞書形式で取得
    rows = csv.DictReader(csvData)
    for row in rows:
        print("-----------------------------------------------------")
        # 内容
        row["内容"] = row["内容"].replace("事案", "")
        row["内容"] = row["内容"].replace("公然", "")
        # メール本文
        row["メール本文"] = row["メール本文"].replace("０", "0")
        row["メール本文"] = row["メール本文"].replace("１", "1")
        row["メール本文"] = row["メール本文"].replace("２", "2")
        row["メール本文"] = row["メール本文"].replace("３", "3")
        row["メール本文"] = row["メール本文"].replace("４", "4")
        row["メール本文"] = row["メール本文"].replace("５", "5")
        row["メール本文"] = row["メール本文"].replace("６", "6")
        row["メール本文"] = row["メール本文"].replace("７", "7")
        row["メール本文"] = row["メール本文"].replace("８", "8")
        row["メール本文"] = row["メール本文"].replace("９", "9")
        row["メール本文"] = row["メール本文"].replace("時ころ", "時頃")
        row["メール本文"] = row["メール本文"].replace("分ころ", "分頃")
        print("-----------------------------------------------------")
        print("種別:", row["種別"])
        print("場所:", row["場所"])
        print("内容:", row["内容"])
        print("受信日時:", row["受信日時"])
        print("メール本文:", row["メール本文"])

    # ファイルのクローズ
    csvData.close()