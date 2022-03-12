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
                elif str(var.tag) == "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t":
                    newParagraph.text += var.text
                else:
                    pass#print(var.tag)
            else:#Used to instantiate your first paragraph
                if str(var.tag) == "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p":
                    newParagraph.paraId = var.attrib["{http://schemas.microsoft.com/office/word/2010/wordml}textId"]
                    newParagraph.textId = var.attrib["{http://schemas.microsoft.com/office/word/2010/wordml}paraId"]
                    activeParagraph = True

        for i in document:
            i.processContent()
            print(i.text)
        self.validate(document)
    def validate(self,document):
        fp = open('Changes/requiredChanges.txt', 'w')
        byLine = 0
        for i in range(4): #Ensure the by line exists, and then that the preceeding lines are capitalized. Maximum length = 4 lines.
            if document[i].text == "by":
                byLine = i
        for i in range(byLine):
            if document[i].caps == False:
                fp.write('All title lines must be completely capitalized ')
                break
        if byLine == 0:
            fp.write('Missing line {by}')
            fp.write('Fix this first and disregard subsequent errors')

        fp.write('ISSUE Comment Here')
        fp.close()




if __name__ == '__main__': #Code to test fileParser independently
    validate = validatorMain()
    validate.readLines("Completed Example ETD.docx")