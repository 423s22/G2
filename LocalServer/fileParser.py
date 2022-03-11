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
        #with open(fileName, "r") as file:
        #    first_line = file.readline()
        #    body = file.readline()
        #self.processBody(body)
        # parse an xml file by name
        file = minidom.parse('document.xml')

        # use getElementsByTagName() to get tag
        models = file.getElementsByTagName('model')

        # one specific item attribute
        print('model #2 attribute:')
        print(models[1].attributes['name'].value)

        # all item attributes
        print('\nAll attributes:')
        for elem in models:
            print(elem.attributes['name'].value)

        # one specific item's data
        print('\nmodel #2 data:')
        print(models[1].firstChild.data)
        print(models[1].childNodes[0].data)

        # all items data
        print('\nAll model data:')
        for elem in models:
            print(elem.firstChild.data)

    """def processBody(self,content):
        tokenizedContent = []
        #<w:t is either just that or <w:t xml preserve> other starts are tab or title page.
        print(content.__len__())
        textTokenDetected = False
        skipIncrement = 0 #Used to enable better tokenizing without a while loop.
        for i in range(len(content)):
            if skipIncrement > 0:
                skipIncrement -=1
            elif textTokenDetected: #the content between language tokens
                EOT = False
                token = content[i]
                increment = 0
                while not EOT:
                    increment +=1
                    content += content[i+increment]
                    if content[i+increment] == "<":
                        EOT = True
                        textTokenDetected = False
                tokenizedContent.append(token)
            elif content[i] == "<": #the content inside the tokens
                EOT = False
                token = content[i]
                increment = 0
                while not EOT:
                    increment +=1
                    skipIncrement +=1
                    content += content[i+increment]
                    if content[i+increment] == ">":
                        EOT = True
                tokenizedContent.append(token)
                if token.__contains__("<w:t>") or token.__contains__("<w:t xml:space=\"preserve\">"):
                    textTokenDetected = True"""
if __name__ == '__main__': #Code to test fileParser independently
    validate = validatorMain()
    validate.readLines("C:\\null.txt")