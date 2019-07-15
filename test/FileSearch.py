"""
ディレクトリを探索します。
"""

import os
import time
import glob

def getFormatDateTime(epocTime):
    """
    エポックタイムをYYYY/MM/DD HH:MM:SS形式に変換します。
    """
    return time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(epocTime))

# ディレトリを探索します。
for currentFile in glob.glob("/etc/**"):
    try:
        directoryName = os.path.dirname(currentFile)
        fileName = os.path.basename(currentFile)
        extName = os.path.splitext(currentFile)[-1]
        aDateTime = getFormatDateTime(os.path.getatime(currentFile))
        mDateTime = getFormatDateTime(os.path.getmtime(currentFile))
        cDateTime = getFormatDateTime(os.path.getctime(currentFile))
        fileSize = os.path.getsize(currentFile)
        print("------------------------------------------------")
        print("Directory:{0} FileName:{1}".format(directoryName, fileName))
        print("            Extent:" + extName)
        print("    LastUpdateTime:" + aDateTime)
        print("    LastModifyTime:" + mDateTime)
        print("LastModifyMedaData:" + cDateTime)
        print("          FileSize:{0:>8,}".format(fileSize))

    except FileNotFoundError:
        print ("FileNotFound:" + currentFile)
    
    except PermissionError:
        print ("PermissionError:" + currentFile)
    
    finally:
        print("------------------------------------------------")
