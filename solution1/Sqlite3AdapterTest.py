#######################################################
# TEST
#######################################################
import Sqlite3Adapter as dbAdapter

test = dbAdapter.SqLite3Adapter()

test.openDB("./solution1/Sqlite3Adapter.db")

createTableSql = """
create table test (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    option_value TEXT,
    created_datetime TIMESTAMP DEFAULT (DATETIME('now', 'localtime'))
)"""

params=("test",) # カンマがタプル宣言に必要です。
row = test.getRow("SELECT * FROM sqlite_master WHERE type = 'table' and name = ?", params)
print(row)
if (row is None):
    test.executeSql(createTableSql)

test.executeSql("INSERT INTO TEST VALUES(?, ?, ?, ?)", (1, 'Test1', 'opt1', None))
test.executeSql("INSERT INTO TEST(id, name, option_value) VALUES(?, ?, ?)", (2, 'Test2', 'opt2'))
test.executeSql("INSERT INTO TEST(id, name) VALUES(?, ?)", (3, 'Test3'))

myRows = test.getRows("SELECT * FROM TEST")
for row in myRows:
    print(row[0], row[1], row[2], row[3])

test.executeSql("UPDATE TEST SET option_value=? WHERE id = ?", ("option1", 1))
test.executeSql("UPDATE TEST SET option_value=? WHERE id = ?", ("option2", 2))

myRows = test.getRows("SELECT * FROM TEST")
for row in myRows:
    print(row[0], row[1], row[2], row[3])

#test.commitDB()
test.closeDB()