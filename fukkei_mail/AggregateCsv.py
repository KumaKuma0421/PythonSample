import os
from glob import glob
import csv
import re
from Container import *

table1 = Table1()
table2 = Table2()
kind_set = set()
address_set = set()
category_set = set()
datetime_set = set()
receive_set = set()
station_set = set()
contents_set = set()

trans_table_number = str.maketrans({
    "０": "0", "１": "1", "２": "2", "３": "3",
    "４": "4", "５": "5", "６": "6", "７": "7",
    "８": "8", "９": "9"}
)

expression_table_ward = {
    "小倉北区": "北九州市小倉北区",
    "小倉南区": "北九州市小倉南区",
    "八幡東区": "北九州市八幡東区",
    "八幡西区": "北九州市八幡西区",
    "門司区": "北九州市門司区",
    "若松区": "北九州市若松区",
    "戸畑区": "北九州市戸畑区",
    "博多区": "福岡市博多区",
    "中央区": "福岡市中央区",
    "早良区": "福岡市早良区",
    "城南区": "福岡市城南区",
    "東区": "福岡市東区",
    "西区": "福岡市西区",
    "南区": "福岡市南区",
}

expression_table_category = {
    ".*ひったくり.*": "ひったくり",
    ".*ひたっくり.*": "ひったくり",

    ".*のぞき.*": "のぞき",
    ".*ぞき.*": "のぞき",
    ".*覗き.*": "のぞき",

    ".*わせつ.*": "わいせつ",
    ".*わい[させ]つ.*": "わいせつ",
    ".*卑(わい|猥).*": "わいせつ",
    ".*露出.*": "わいせつ",

    ".*[付つ]きまと.*": "つきまとい",
    "つきまい.*": "つきまとい",

    ".*ちかん.*": "ちかん",
    ".*チカン.*": "ちかん",
    ".*痴漢.*": "ちかん",
    ".*スカート.*": "ちかん",
    ".*身体接触.*": "ちかん",

    ".*オレオレ.*": "オレオレ詐欺",
    ".*振.*込め.*": "オレオレ詐欺",
    ".*不正送金.*": "オレオレ詐欺",

    ".*(偽|ニセ|アポ|予兆)電.*": "不審電話",
    ".*不審.*電話.*": "不審電話",
    ".*警察官を名乗る電話.*": "不審電話",
    ".*警察官を騙る電話.*": "不審電話",
    ".*連続電話.*": "不審電話",

    ".*不審.*(ハガキ|はがき|はき|封書|文書|手紙).*": "不審文書",

    ".*(不審|偽|便乗).*(者|火|業者|車両|メール).*": "不審\\2",

    ".*住(宅|居)侵入.*": "住居侵入",

    ".*(刃物|凶器).*(使用|所持).*": "銃刀法違反",
    ".*包丁.*": "銃刀法違反",
    ".*銃砲刀剣類.*": "銃刀法違反",
    ".*けん銃発砲.*": "銃刀法違反",

    ".*場所訂正.*": "場所訂正",

    ".*日.*訂正.*": "日時訂正",
    ".*時間.*訂正.*": "日時訂正",
    ".*(タイトル|内容).*訂正.*": "\\1訂正",

    ".*声.*か[えけ].*": "声かけ",
    ".*声掛け.*": "声かけ",

    ".*(さる|サル|ザル|イノシシ|猪|猿|犬|猫|動物).*": "動物関連",

    ".*(盗撮|撮影|写真|カメラ).*": "盗撮",

    ".*さい銭.*": "さい銭",

    ".*傷害.*": "傷害",

    ".*暴行.*": "暴行",

    ".*強盗.*": "強盗",

    ".*咬傷.*": "咬傷",

    ".*車(両|上)(狙い|ねらい).*": "車上狙い",

    ".*窃盗.*": "窃盗",

    ".*色情.*": "色情",

    ".*盗難.*": "盗難",

    ".*器物損壊.*": "器物損壊",

    ".*(投石|投てき).*": "危険物投てき",

    ".*公妨.*": "公務執行妨害",

    ".*忍.*込み.*": "住居侵入",
    ".*住居侵入.*": "住居侵入",
    ".*侵入盗.*": "侵入盗",

    ".*空き巣.*": "空き巣",

    ".*未成年者誘拐.*": "未成年者誘拐",

    ".*悪(徳|質).*": "悪徳商法",

    ".*架空.*請求.*": "架空請求",

    ".*下着.*(泥棒|盗).*": "下着泥棒",

    ".*殺人(事件|未遂).*": "殺人\\1",

    ".*特殊詐欺.*": "特殊詐欺",

    ".*詐欺.*": "詐欺",

    ".*燃える.*": "放火",

    "(.*)(について|事案)": "\\1"
}


def read_address_data(targetFile):
    with open(targetFile, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            entity2 = Entity2(row[0], row[1], row[2])
            table2.append(entity2)


def aggregate_files(targetDirectory):
    files = glob(pathname=targetDirectory)
    for file in files:
        if os.path.exists(file):
            with open(file, "r", encoding="sjis") as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    # メール本文を分割
                    contents1 = row[5]
                    contents2 = contents1.replace('\n\n', '\n')
                    contents3 = contents2.split(sep="配信者：")
                    contents4 = contents3[1].split(sep="お問い合わせ・情報提供先")
                    row.append(contents4[0].replace('\n', ''))
                    contents5 = contents3[0].replace('\n', '').lstrip()
                    # 数値を半角化
                    contents6 = contents5.translate(trans_table_number)
                    contents7 = re.sub('([旬月日時分秒])ころ', '\\1頃', contents6)
                    row[5] = contents7

                    # 日付を半角化
                    row[3] = row[3].translate(trans_table_number)
                    row[3] = re.sub('([旬月日時分秒])ころ', '\\1頃', row[3])

                    # １次加工したデータを保管
                    entity1 = Entity1(kind=row[0], distributor=row[6], received=row[4],
                                      occured=row[3], category=row[2], place=row[1], contents=row[5])
                    table1.append(entity1)


def processing_data():
    for row in table1.yield_data():
        if row.Category.find("訂正") > 0:
            row.Kind = "訂正"
        if row.Place.find("訂正") > 0:
            row.Kind = "訂正"
        if row.Contents.find("訂正") > 0:
            row.Kind = "訂正"

        for key, value in expression_table_ward.items():
            changed = re.sub(key, value, row.Place)
            if changed != row.Place:
                row.Place = changed
                break

        for key, value in expression_table_category.items():
            changed = re.sub(key, value, row.Category)
            if changed != row.Category:
                row.Category = changed
                break

        adrs = row.Place
        adrs = adrs.replace("「", "")
        adrs = adrs.replace("、", "")
        adrs = adrs.replace("お知らせした", "")
        adrs = adrs.replace("お知らせした", "")
        adrs = adrs.replace("お知らせしました", "")
        adrs = adrs.replace("お知らせしていた", "")
        adrs = adrs.replace("お知らせしていました", "")
        adrs = adrs.replace("お報せしました", "")
        adrs = adrs.replace("福岡県", "")
        adrs = adrs.replace("大字", "")
        adrs = adrs.replace("福岡市", "")
        adrs = adrs.replace("北九州市", "")
        for key, value in expression_table_ward.items():
            changed = re.sub(key, value, adrs)
            if changed != adrs:
                row.Place = changed
                break


def make_response():
    with open("result.csv", "w", encoding="utf-8", newline='') as f:
        #writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer = csv.writer(f)
        for row in table1.yield_data():
            writer.writerow(row.row_context())


def write_list(set_list, file_name):
    with open(file_name, "w", encoding="utf-8", newline="") as f:
        for row in sorted(set_list):
            f.write(row + os.linesep)


def aggregate_cols():
    for row in table1.yield_data():
        kind_set.add(row.Kind)
        address_set.add(row.Place)
        category_set.add(row.Category)
        datetime_set.add(row.Occured)
        receive_set.add(row.Received)
        contents_set.add(row.Contents)
        station_set.add(row.Distributor)

    write_list(kind_set, "set_kind.csv")
    write_list(address_set, "set_address.csv")
    write_list(category_set, "set_category.csv")
    write_list(datetime_set, "set_datetime.csv")
    write_list(receive_set, "set_receive.csv")
    write_list(contents_set, "set_contents.csv")
    write_list(station_set, "set_station.csv")


if __name__ == "__main__":
    os.chdir("fukkei_mail")

    read_address_data(".\\CSV\\40_address.csv")

    aggregate_files(".\\CSV\\fukkeimail*")
    processing_data()
    make_response()

    aggregate_cols()

    print("kind_set:" + str(len(kind_set)))
    print("address_set:" + str(len(address_set)))
    print("category_set:" + str(len(category_set)))
    print("datetime_set:" + str(len(datetime_set)))
    print("receive_set:" + str(len(receive_set)))
    print("station_set:" + str(len(station_set)))
    print("Entity1:" + str(table1.count()))
