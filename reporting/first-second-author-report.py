from lxml import etree
import os


class AuthorReporter():
    '''
    This class identifies osm metadata records that contain MMM affiliations for the first
    or second authors. User inputs the directory path containing records to be parsed.
    '''

    def __init__(self, directory):
        self.counter = 0
        self.directory = directory
        for file in os.listdir(directory):
            if file.endswith(".xml"):
                self.parseFile(os.path.join(directory, file))


    def parseFile(self, file):
        parser = etree.XMLParser(recover=True, encoding='utf-8')
        tree = etree.parse(file, parser)
        # print(etree.tostring(tree.getroot()))

        ns = {'osm': 'http://nldr.library.ucar.edu/metadata/osm'}

        recordID = tree.xpath("string(//osm:recordID)", namespaces=ns)
        isResult = tree.xpath('boolean(//osm:person[@order="1" or '
                              '@order="2"]/osm:affiliation/osm:instDivision[contains(text(), '
                              '"Mesoscale and Microscale Meteorology Division")])', namespaces=ns)

        if isResult:
            self.counter += 1
            print recordID
        else:
            print recordID + " doesn't count."


if __name__ == '__main__':
    directory = raw_input("type file path of directory to report on:\n")
    print "For fiscal year " + directory + " files that contain MMM authors in 1st or 2nd place:"
    reporter = AuthorReporter(directory)
    print "Final count of resulting records: " + str(reporter.counter)
