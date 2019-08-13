markup = "<!DOCTYPE html>\n"+
             "<html>\n"+
             " <head>\n"+
             "   <title>Example Input Markup</title>\n"+
             " </head>\n"+
             " <body>\n"+
             "   <p id=\"msg\">\n"+
             "     Hello World!\n"+
             "   </p>\n"+
             " </body>\n"+
             "</html>"

parseHtmlDocument(markup);

# Function definitions

def parseHtmlDocument(markup):
	print("BEGIN DOCUMENT")
	markup = parseDoctypeDeclaration(markup)
	markup = parseElement(markup)
	print("END DOCUMENT")

def parseDoctypeDeclaration(markup):
	regEx = /^(\<!DOCTYPE .*\>\s*)/i
	print("DOCTYPE DECLARATION")
	matches = regEx.exec(markup)
	doctypeDeclaration = matches[1]
	markup = markup.substring(doctypeDeclaration.length)
	return markup

def parseElement(markup);
	regEx = /^\<(\w*)/i
	matches = regEx.exec(markup)
	tagName = matches[1]
	print("BEGIN ELEMENT: "+tagName)
	markup = markup.substring(matches[0].length)
	markup = parseAttributeList(markup)
	regEx = /^\>/i
	matches = regEx.exec(markup)
	markup = markup.substring(matches[0].length)
	markup = parseNodeList(markup)
	regEx = new RegExp("^\<\/"+tagName+"\>")
	matches = regEx.exec(markup)
	markup = markup.substring(matches[0].length)
	print("END ELEMENT: "+tagName)
	return markup

def parseAttributeList(markup):
	regEx = /^\s+(\w+)\=\"([^\"]*)\"/i
	matches
	while matches = regEx.exec(markup):
		attrName = matches[1]
		attrValue = matches[2]
		print("ATTRIBUTE: "+attrName)
		markup = markup.substring(matches[0].length)
	return markup

def parseNodeList(markup):
	while markup:
		markup = parseTextNode(markup)
		regEx = /^\<(.)/i
		matches = regEx.exec(markup)
	if(matches[1] !== '/'):
		markup = parseElement(markup)
        else:
		return markup

def parseTextNode(markup)
	regEx = /([^\<]*)\</i
	matches = regEx.exec(markup)
	markup = markup.substring(matches[1].length)
	return markup

