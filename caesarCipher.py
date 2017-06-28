


# caesarCipher
# message: the message you want to encrypt or decrypt
# shift: the number of spaces you want to shift each letter
# strip: optional argument to indicate whether you want to strip out non-alphanumeric characters. Default option is to leave symbols as is.

def caesarCipher(message, shift, strip=False):
    # If for some reason someone wants to shift backwards instead of forward, then we add successive multiples of 26 to it until it's between 0 and 26. 
    while shift < 0:
        shift += 26
    # If someone enters a number greater than 26, then we simply reduce by 26 until we get a number between 0 and 26.
    while shift > 26:
        shift -= 26
    translatedMessage = ''
    
    for symbol in message:
        if symbol.isalpha():
            unicodeNum = ord(symbol)
            unicodeNum += shift
            
            if symbol.isupper():
                if unicodeNum > ord('Z'):
                    unicodeNum -= 26
                elif unicodeNum <= ord('A'):
                    unicodeNum += 26
            elif symbol.islower():
                if unicodeNum > ord('z'):
                    unicodeNum -= 26
                elif unicodeNum < ord('a'):
                    unicodeNum += 26

            translatedMessage += chr(unicodeNum)
        else:
            if not strip:
                translatedMessage += symbol

    print('Your translated cipher is: ', translatedMessage)

