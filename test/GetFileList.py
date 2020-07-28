import os

path = "C:\\Users\\User01\\Documents"
#path = "/home/user01/"

# カレントディレクトリを取得します。
print("now we are in " + os.getcwd() + ".")

# 指定パスの絶対パスを取得します。
absPath = os.path.abspath(path)
print("targetPath=" + absPath + ".")

with os.scandir(absPath) as it:
    for file in it:
        print("name=" + file.name)
        print("fillPath=" + file.path)
        print(" is_dir=" + str(file.is_dir()))
        print(" is_file=" + str(file.is_file()))
        print(" is_symlink=" + str(file.is_symlink()))
        stat_result = file.stat()
        print("  stat_result.st_size=" + str(stat_result.st_size))
        print("  stat_result.st_mtime=" + str(stat_result.st_mtime))
        print("  stat_result.st_file_attributes=" +
              str(stat_result.st_file_attributes))

files = os.listdir(path)
print(files)
