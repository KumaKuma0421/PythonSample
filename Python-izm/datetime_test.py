# 標準ライブラリのインポート
import datetime

# 日付の取得 yyyy-mm-dd
today = datetime.date.today()
print(today)

# 日付の取得 yyyy-mm-dd hh:mm:ss.dddddd
today_detail = datetime.datetime.today()
print(today_detail)

# 日付の部分取得
print(today.year)
print(today.month)
print(today.day)
print(today_detail.hour)
print(today_detail.microsecond)

# 日付のフォーマット指定
print(today.isoformat())
print(today_detail.strftime("%Y/%m/%d %H:%M:%S"))

# 明日の日付
print(today_detail + datetime.timedelta(days=1))

newyear = datetime.datetime(2010, 1, 1)

# 2010年1月1日の一週間後
print(newyear + datetime.timedelta(days=7))

# 2010年1月1日から今日までの日数
calc = today_detail - newyear

# 計算結果の戻り値は「timedelta」
print(calc.days)
