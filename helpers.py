
# Source: http://www.unicode.org/charts/
def isAlphabet(word):
    if len(word) == 0:
        return False
    for char in word:
        if ord(char) >= 97 and ord(char) <= 122: # English
            return True
        if ord(char) >= 2304 and ord(char) <= 2403: # Devanagiri
            return True
        
    return False

def isNum(word):
    if len(word) == 0:
        return False
    for char in word:
        if ord(char) >= 97 and ord(char) <= 122: # English
            return False
        if ord(char) >= 2304 and ord(char) <= 2403: # Devanagiri
            return False
        
    return True

def isAlphaNum(word):
    return isAlphabet(word) or isNum(word)
