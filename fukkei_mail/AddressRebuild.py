#
# 40_20200717.csv を再構成します。
#

import os
import csv

data_path = ".\\CSV\\40_20200717.csv"
new_data_path = ".\\CSV\\40_address.csv"
write_data = list()


def rebuild_address_info():
    if not os.path.exists(data_path):
        print("file:{0} is not found.".format(data_path))
        return False

    with open(data_path, "r", encoding="sjis") as zip:
        reader = csv.reader(zip)
        next(reader)
        for row in reader:
            # "町村名一文字目カナ","都道府県市区郡名","町村名","都道府県市区郡コード","町村コード","小字コード"
            if len(row[5]) > 0 and int(row[5]) > 99:
                print(row)
                raise ValueError("小字コードが99を超えています。")

            row[1] = row[1].replace('福岡県', '')
            address_code = "{0:5}_{1:3}_{2:02}".format(
                row[3], row[4], int(row[5]) if len(row[5]) > 0 else 0)
            write_data.append((address_code, row[1], row[2]))

    return True


def write_new_data():
    csv.QUOTE_ALL
    header = ("コード", "住所1", "住所2")
    write_data.insert(0, header)
    with open(new_data_path, "w", encoding="utf-8", newline='') as zip:
        writer = csv.writer(zip, quoting=csv.QUOTE_ALL)
        print("now writing address data.")
        writer.writerows(write_data)
        print("writing address data done.")


if __name__ == "__main__":
    os.chdir("fukkei_mail")
    ret = rebuild_address_info()
    if ret == True:
        write_new_data()
