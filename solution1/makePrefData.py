#######################################################
# 福岡県の市区町村情報をデータベース化します
#######################################################
import Sqlite3Adapter as dbAdapter
import csv

test = dbAdapter.SqLite3Adapter()

# データベースの作成、オープン
test.openDB("./solution1/solution1.db")

# "町村名一文字目カナ","都道府県市区郡名","町村名","都道府県市区郡コード","町村コード","小字コード"
createTableSql = """
create table PrefTable (
    ID        INTEGER PRIMARY KEY,
    WARD_ID   INTEGER NOT NULL,
    WARD_NAME TEXT    NOT NULL
)
"""

insertTableSql = """
INSERT INTO PrefTable
    (WARD_ID, WARD_NAME)
    VALUES(?, ?)
"""
# テーブルの存在確認
params=("PrefTable",) # カンマがタプル宣言に必要です。
row = test.getRow("SELECT * FROM sqlite_master WHERE type = 'table' and name = ?", params)
print(row)
if (row is None):
    test.executeSql(createTableSql)

# テーブルへの追加

# ファイルのオープン
csvData = open("/home/user01/Download/40_20190705.csv", "r", encoding='shift-jis', errors="", newline="")

# リスト形式で取得
dataList = csv.reader(
            csvData,
            delimiter=",",
            doublequote=True,
            lineterminator="\r\n",
            quotechar='"',
            skipinitialspace=True)

for row in dataList:
    if (row[2] != "町村名") : # 先頭行はスキップします。
        wardID = "{0:5}{1:4}".format(row[3],row[4])
        wardName = "{0}{1}".format(row[1][3:], row[2])
        test.executeSql(insertTableSql, (wardID, wardName))
        #print(prefID, wardID, prefName, wardName)

# テーブルから抽出
myRows = test.getRows("SELECT * FROM PrefTable")
for row in myRows:
    print(row[0], row[1], row[2])

# 更新情報を確定する
test.commitDB()

# データベースをクローズする。
test.closeDB()