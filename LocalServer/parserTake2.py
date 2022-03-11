import xml.sax

class XMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.price = ""
        self.qty = ""
        self.company = ""

   # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if(tag == "model"):
            print("*****Model*****")
            title = attributes["number"]
            print("Model number:", title)

   # Call when an elements ends
    def endElement(self, tag):
        if(self.CurrentData == "price"):
            print("Price:", self.price)
        elif(self.CurrentData == "qty"):
            print("Quantity:", self.qty)
        elif(self.CurrentData == "company"):
            print("Company:", self.company)
        self.CurrentData = ""

   # Call when a character is read
    def characters(self, content):
        if(self.CurrentData == "price"):
            self.price = content
        elif(self.CurrentData == "qty"):
            self.qty = content
        elif(self.CurrentData == "company"):
            self.company = content

# create an XMLReader
parser = xml.sax.make_parser()

# turn off namepsaces
parser.setFeature(xml.sax.handler.feature_namespaces, 0)

# override the default ContextHandler
Handler = XMLHandler()
parser.setContentHandler( Handler )
parser.parse("document.xml")