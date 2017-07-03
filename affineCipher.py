# Affine Cipher


def affineCipher(message, alpha, beta, strip=False):
    # If for some reason someone wants to shift backwards instead of forward, then we add successive multiples of 26 to it until it's between 0 and 26. 
    while shift < 0:
        shift += 26
    # If someone enters a number greater than 26, then we simply reduce by 26 until we get a number between 0 and 26.
    while shift > 26:
        shift -= 26

    # Initialise the output as an empty string. The plan is to iterate through each letter of the message, translate it, and then put the result into translatedMessage.
    translatedMessage = ''

    for symbol in message:
        if symbol.isupper():
            num = (alpha*(ord(symbol)-65)+beta)%26+65
        elif symbol.islower():
            num = (alpha*(ord(symbol)-97)+beta)%26+97
        translatedMessage += chr(num)
    else:
        if not strip:
            translatedMessage += symbol

    print('Your translated cipher is: ', translatedMessage)