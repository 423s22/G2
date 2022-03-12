class paragraph:
    def __init__(self,paraId):
        self.paraId = paraId
        self.textId = ""
        self.fonts = ""
        self.caps = False
        self.text = ""
    def processContent(self):
        if self.caps == True:
            self.text = self.text.upper()


