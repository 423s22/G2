from pathlib import Path
import zipfile
import xml.etree.ElementTree
import paragraph


class validatorMain:
    def parse(self,fileName):
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
        empty = True
        byLine = 0
        for i in range(4): #Ensure the by line exists, and then that the preceeding lines are capitalized. Maximum length = 4 lines.
            if document[i].text == "by":
                byLine = i
        for i in range(byLine):
            if document[i].caps == False:
                empty = False
                fp.write('All title lines must be completely capitalized ')
                break
        if byLine == 0:
            empty = False
            fp.write('Missing line {by}')
            fp.write('Fix this first and disregard subsequent errors')
        if empty:
            fp.write("All good")
            fp.close
            return True

        fp.close()




if __name__ == '__main__': #Code to test fileParser independently
    validate = validatorMain()
    validate.parse("Completed Example ETD.docx")