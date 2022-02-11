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
        try:
            open(fileName)
        except:
            print("File address error")
            return("error")
        return(fileName)