import re
from tqdm import tqdm

targetLog = r"..\LogParser\flowengine.log"
outputLog = r".\output.txt"

contents = list()

fout = open(outputLog, "w", encoding="shift_jis")

with open(targetLog, "r", encoding="shift_jis") as f:
    contents = f.readlines()

outputString = "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n".format(
    "Date", "Time", "ms", "PID", "Category", "Message")
fout.writelines(outputString)

expression = re.compile(r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}),(\d{3}) (\d{3,5}) (\w+)(\s+-\s+)")

for row in tqdm(contents):
    if (len(row) == 0):
        continue
    elif (row[0:4] != "2020"):
        continue

    row = row.replace("\t", " ")

    row = expression.sub(r"\1\t\2\t\3\t\4\t\5\t", row)

    #print(row)
    fout.writelines(row)

fout.close()