def isPhoneNumber(text):
    if len(text) != 10:
        return False
    for i in range(0, 10):
        if not text[i].isdecimal():
            return False
    if text[0] != '8' and text[0] != '7':
        return False
    
    return True

print(isPhoneNumber('8060916345'))