"""
標準ライブラリ calendar
"calendar"は日付操作を行うためのライブラリです。
"""

import calendar

# 月末日の表示
print(calendar.monthrange(2018, 1)[1])
print(calendar.monthrange(2018, 2)[1])

# 年月を指定してカレンダーを表示
calendar.prmonth(2018, 1)

# 起点を日曜にしたカレンダーを表示
c = calendar.TextCalendar(calendar.SUNDAY)
c.prmonth(2018, 1)

# うるう年かどうか
print(calendar.isleap(2018))
print(calendar.isleap(2020))