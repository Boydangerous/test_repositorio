def getFirstUpperChar(text):
    for char in text:
        if char.isupper():
            return char
    return "NA"