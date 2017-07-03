#UZQSOVUOHXMOPVGPOZPEVSGZWSZOPFPESXUDBMETSXAIZVUEPHZHMDZSHZOWSFPAPPDTSVPQUZWYMXUZUHSXEPYEPOPDZSZUFPOMBZWPFUPZHMDJUDTMOHMQ


def vignereCipher(message, keyword):
    cipherKey = [ord(symbol)%26 for symbol in keyword]
    
    translatedMessage = ''

    for i in range(len(message)):
        num = ord(message[i])+cipherKey[i%len(cipherKey)]
        if num > ord('z'):
            num -= 26

        translatedMessage += ord(num)

    print('Your translated message is: ', translatedMessage)