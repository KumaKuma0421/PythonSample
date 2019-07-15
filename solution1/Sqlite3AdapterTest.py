#######################################################
# TEST
#######################################################
import Sqlite3Adapter as dbAdapter

test = dbAdapter.SqLite3Adapter()

# データベースの作成、オープン
test.openDB("./solution1/Sqlite3Adapter.db")

# https://gray-code.com/php/create-table-by-using-sqlite3/#section3
#
# SQLite3では、「CREATE TABLE」の際に「AUTO INCREMENT」を指定する必要はありません。
# もし主キーを連番のIDにしたい場合、INTEGERで「PRIMARY KEY」を指定するようにします。
#
# データを登録や更新する際に、ほとんどの場合その時点の日時も保存します。
# 次のSQLにある「created_datetime」のように設定を宣言すると、その時点での日時を
# 自動的に取得して保存してくれるようになります。
createTableSql = """
create table test (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    option_value TEXT,
    created_datetime TIMESTAMP DEFAULT (DATETIME('now', 'localtime'))
)"""

# テーブルの存在確認
params=("test",) # カンマがタプル宣言に必要です。
row = test.getRow("SELECT * FROM sqlite_master WHERE type = 'table' and name = ?", params)
print(row)
if (row is None):
    test.executeSql(createTableSql)

# テーブルへの追加
# コミットすると、次回の動作で例外が発生します。
# IDを指定すると、指定値で設定されてしまいます。
# test.executeSql("INSERT INTO TEST VALUES(?, ?, ?, ?)", (1, 'Test1', 'opt1', None))
# test.executeSql("INSERT INTO TEST(id, name, option_value) VALUES(?, ?, ?)", (2, 'Test2', 'opt2'))
# test.executeSql("INSERT INTO TEST(id, name) VALUES(?, ?)", (3, 'Test3'))
test.executeSql("INSERT INTO TEST(name, option_value) VALUES(?, ?)", ('Test1', 'opt1'))
test.executeSql("INSERT INTO TEST(name, option_value) VALUES(?, ?)", ('Test2', 'opt2'))
test.executeSql("INSERT INTO TEST(name) VALUES(?)", ('Test1',))
test.executeSql("INSERT INTO TEST(name) VALUES(?)", ('Test2',))

# テーブルから抽出
myRows = test.getRows("SELECT * FROM TEST")
for row in myRows:
    print(row[0], row[1], row[2], row[3])

# テーブルの更新
test.executeSql("UPDATE TEST SET option_value=? WHERE option_value = ?", ("option1", "opt1"))
test.executeSql("UPDATE TEST SET option_value=? WHERE option_value = ?", ("option2", "opt2"))

# テーブルの更新結果の抽出
myRows = test.getRows("SELECT * FROM TEST")
for row in myRows:
    print(row[0], row[1], row[2], row[3])

# 更新情報を確定する
test.commitDB()

# データベースをクローズする。
test.closeDB()