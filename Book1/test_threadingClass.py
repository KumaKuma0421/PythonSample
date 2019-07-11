"""
標準ライブラリ threading
この処理は"threading.Thread"クラスを継承した自作クラスを使う方法でも実現できます。
"""

import time
import threading

class My_Thread(threading.Thread):
    def __init__(self):
        super(My_Thread, self).__init__()
    
    def run(self):
        for i in range(0, 4):
            time.sleep(1)
            print('count', i)

thread1 = My_Thread()
thread2 = My_Thread()

thread1.start()
time.sleep(0.1)
thread2.start()