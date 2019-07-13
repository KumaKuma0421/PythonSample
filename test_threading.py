"""
標準ライブラリ threading
threadingは複数スレッドの実行（並列処理）を手軽に扱うためのライブラリです。
並列処理したい関数を引数に設定して、"threading.Thread"クラスのインスタンスを作ると、
start函数で処理を実行させることができます。
"""
import time
import threading

def func():
    for i in range(0, 4):
        time.sleep(1)
        print('count', i)

thread1 = threading.Thread(target=func)
thread2 = threading.Thread(target=func)

thread1.start()
time.sleep(0.1)
thread2.start()