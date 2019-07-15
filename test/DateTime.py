import time


# エポックからの秒数を浮動小数点で返します。
currentTime = time.time()
print("currentTime=" + str(currentTime))
print("localTime(currentTime)=" + str(time.localtime(currentTime)))

# time.struct_time型を返します。
# gmtime()、localtime()、strptime()が該当します。
# 引数はtime.time()のエポックタイムになります。
currentLocalTime = time.localtime()
print("currentLocalTime=" + str(currentLocalTime))
currentGlobalTime = time.gmtime()
print("currentGlobalTime=" + str(currentGlobalTime))

print(time.ctime(currentTime))
print(time.strftime("%Y/%m/%d %H:%M:%S", currentLocalTime))
print(time.strftime("%Y/%m/%d %H:%M:%S", currentGlobalTime))
