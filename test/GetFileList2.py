"""
一番シンプルなファイル一覧取得ロジック
"""

import glob
import re
import os

#path = "C:/Users/User01/Documents/**"
path = "/home/user01/**"

#myFileList = glob.glob(path, recursive=True)
myFileList = [p for p in glob.glob(path, recursive=True) if os.path.isfile(p)]
for myFile in myFileList:
    print(myFile)