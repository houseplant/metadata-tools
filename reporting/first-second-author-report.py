# the purpose of this script will be to identify osm metadata records that contain certain
# instDivision affiliations for the first or second authors

__author__ = 'jblomer'
from lxml import etree

file = raw_input("type the file path to xml file to be parsed:\n")
parser = etree.XMLParser(recover=True, encoding='utf-8')
tree = etree.parse(file, parser)

print(etree.tostring(tree.getroot()))
