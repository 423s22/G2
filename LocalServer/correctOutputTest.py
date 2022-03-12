import fileParser


def testValidDocValidates():
    validate = fileParser.validatorMain()
    validate.parse("Completed Example ETD.docx")
    fp = open("Changes/requiredChanges.txt")
    firstLine = fp.readline()
    assert "All good" in firstLine



if __name__ == '__main__':  # Code to test fileParser independently
    testValidDocValidates()
