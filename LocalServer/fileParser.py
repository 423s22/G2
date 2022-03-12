from pathlib import Path
import zipfile
import xml.etree.ElementTree
import paragraph


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
        with zipfile.ZipFile(fileName) as docx:
            tree = xml.etree.ElementTree.XML(docx.read('word/document.xml'))
        activeParagraph = False
        newParagraph = paragraph.paragraph("NULL")
        document = []
        for var in tree.iter():#Iterate through the entire tree
            if activeParagraph:#After teh first paragraph is instantiated, general case
                if str(var.tag) == "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p":
                    document.append(newParagraph)
                    newParagraph = paragraph.paragraph(var.attrib["{http://schemas.microsoft.com/office/word/2010/wordml}paraId"])
                    newParagraph.textId = var.attrib["{http://schemas.microsoft.com/office/word/2010/wordml}textId"]
                elif str(var.tag) == "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}caps":
                    newParagraph.caps = True
                else:
                    print(var.tag)
            else:#Used to instantiate your first paragraph
                if str(var.tag) == "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p":
                    newParagraph.paraId = var.attrib["{http://schemas.microsoft.com/office/word/2010/wordml}textId"]
                    newParagraph.textId = var.attrib["{http://schemas.microsoft.com/office/word/2010/wordml}paraId"]
                    activeParagraph = True

        for i in document:
            print(i.paraId)
        self.validate(document)
    def validate(self,document):
        #Check first couple paras are capitalized
        #Determine
        open('')





if __name__ == '__main__': #Code to test fileParser independently
    validate = validatorMain()
    validate.readLines("Completed Example ETD.docx")