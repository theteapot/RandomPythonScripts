import urllib

def readTextFromFile():
    file = open("")     # put your file path inbetween the quotation marks.
    contentsOfFile = file.read()
    print(contentsOfFile)
    file.close()
    checkForCurseWords(contentsOfFile)
    
def checkForCurseWords(textInput):
    url = urllib.urlopen("http://www.wdyl.com/profanity?q=" + textInput) # Uses Googles what do you love website to test for profantiy
    result = url.read()
    print(result)
    url.close()

readTextFromFile()
