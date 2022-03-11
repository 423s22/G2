from pathlib import Path
from xml.dom import minidom
class fileParser:
    def __init__(self, fileName):
        self.name = fileName
    def parseFile(self):
        print("File has been parsed: " + self.name)
        resultsFileName = (self.name+"results.txt")
        print("ResultsFilePostedAs: " + resultsFileName)
class validatorMain:
    def processFileAddress(self):
        fileName = input("Please enter the address of the file:")
        file_path = Path(fileName)
        print(fileName)
        print(file_path + " file")
        try:
            open(file_path)
            self.readLines(file_path)
        except:
            print("File address error")
            return("error")
        return(file_path)
    def readLines(self,fileName):
        import zipfile
        import xml.etree.ElementTree

        WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
        PARA = WORD_NAMESPACE + 'p'
        TEXT = WORD_NAMESPACE + 't'
        TABLE = WORD_NAMESPACE + 'tbl'
        ROW = WORD_NAMESPACE + 'tr'
        CELL = WORD_NAMESPACE + 'tc'

        with zipfile.ZipFile('Completed Example ETD.docx') as docx:
            tree = xml.etree.ElementTree.XML(docx.read('word/document.xml'))

        print(tree)
        for text in tree.iter(TEXT):
            print(text.text)



if __name__ == '__main__': #Code to test fileParser independently
    validate = validatorMain()
    validate.readLines("C:\\null.txt")