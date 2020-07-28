"""
一番シンプルなファイル一覧取得ロジック
"""

import glob
import os

path = "C:/Users/User01/Documents/**"
#path = "/home/user01/**"

file_list = [p for p in glob.glob(path, recursive=True) if os.path.isfile(p)]
for file in file_list:
    print(file)