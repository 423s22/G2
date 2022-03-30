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
            #print(i.text)
        self.validate(document)
    def validate(self,document):
        fp = open('Changes/requiredChanges.txt', 'w')
        empty = True
        byLine = 0
        for i in range(4): #Ensure the by line exists, and then that the preceeding lines are capitalized. Maximum length = 4 lines.
            if document[i].text == "by":
                byLine = i
                break
        for i in range(byLine):
            if document[i].caps == False:
                empty = False
                fp.write('All title lines must be completely capitalized ')
                break
        if byLine == 0:
            empty = False
            fp.write('Missing line {by}')
            fp.write('Fix this first and disregard subsequent errors\n')
        if not document[byLine+2].text.__contains__("submitted in partial fulfillment") and document[byLine+3].text.__contains__("of the requirements for the degree"):
            empty = False
            fp.write('Document must contain proper cause of submission\n')
        if not document[byLine+4].text == "of":
            empty = False
            fp.write('Missing of line prior to appropriate degree\n')
        if not document[byLine+5].text.__contains__("Master") and not document[byLine+5].text.__contains__("Doctorate") :
            empty = False
            fp.write('Missing appropriate degree\n')

        if not document[byLine+6].text == "in":
            empty = False
            print(document[byLine+6].text)
            fp.write('Missing \"in\" line prior to program name\n')
        if not document[byLine+8].text == "MONTANA STATE UNIVERSITY" :
            empty = False
            fp.write('Missing university, or university not formatted correctly (All Capitalized)\n')
        if not checkDateFormat(document[byLine + 9].text):
            empty = False
            print(document[byLine+10].text)
            fp.write('Date is formatted as month written out and first letter capitalized, then year\n')
        if not document[byLine+11].text.__contains__("COPYRIGHT"):
            empty = False
            fp.write('Missing copyright')
        if not document[byLine+12].text.__contains__("by"):
            empty = False
            fp.write('Missing by after copyright\n')
        if not document[byLine+13].text == document[byLine+1]:
            empty = False
            fp.write('Missing name consistency\n')
        if empty:
            fp.write("All good")
            fp.close
            return True

        fp.close()


def checkDateFormat(line):
    if line.__contains__("January") or line.__contains__("February")or line.__contains__("March")or line.__contains__("April")or line.__contains__("May")or line.__contains__("June")or line.__contains__("July")or line.__contains__("August")or line.__contains__("September")or line.__contains__("October")or line.__contains__("November")or line.__contains__("December"):
        if line.__contains__("2022") or line.__contains__("2023"):
            return True
        else:
            return False
    else:
        return False
if __name__ == '__main__': #Code to test fileParser independently
    validate = validatorMain()
    validate.parse("Completed_Example_ETD.docx")