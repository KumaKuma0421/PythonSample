import xml.etree.ElementTree as XML

def writeXml():
    root = XML.Element('root')
    tree = XML.ElementTree(element=root)

    fruits = XML.SubElement(root, 'fruits')

    fruit = XML.SubElement(fruits, 'fruit')
    fruit_id = XML.SubElement(fruit, 'name')
    fruit_id.text = 'apple'
    fruit_id = XML.SubElement(fruit, 'price')
    fruit_id.text = '100'

    fruit = XML.SubElement(fruits, 'fruit')
    fruit_id = XML.SubElement(fruit, 'name')
    fruit_id.text = 'orange'
    fruit_id = XML.SubElement(fruit, 'price')
    fruit_id.text = '80'

    fruit = XML.SubElement(fruits, 'fruit', {'country':'Japan'})
    fruit_id = XML.SubElement(fruit, 'name', {'value':'priceless', 'limit':'free'})
    fruit_id.text = 'pineapple'
    fruit_id = XML.SubElement(fruit, 'price')
    fruit_id.text = '200'

    tree.write('./fruits.xml', encoding='utf-8', xml_declaration=True)

def readXml():
    tree = XML.ElementTree(file = 'fruits.xml')
    root = tree.getroot()

    for fruits in root:
        for fruit in fruits:
            for item in fruit:
                print(item.tag, ":", item.text)
                for attr in item.attrib:
                    print(attr, attr.value)

#
# main
#
writeXml()
readXml()