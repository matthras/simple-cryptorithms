from collections import OrderedDict
import numpy as np

def preparePlaintext(message):
    encodedPlaintext = []
    letterPair = ''
    for letter in message:
        # Convert all 'i's to 'j's for easier conversion and matrix construction.
        # Randomising between i/j comes later.
        if letter == 'i':
            letter = 'j'
        letterPair += letter
        if len(letterPair) == 2:
            encodedPlaintext.append(letterPair)
            letterPair = ''
    if len(letterPair) == 1:
        letterPair += 'x'
        encodedPlaintext += letterPair
    return encodedPlaintext

def constructMatrix(key):
    # Checks that the key has any repeated letters and strips them out.
    if(len(key) != len(set(key))):
        print('Your key has duplicate letters. All duplicate letters will be stripped out.')
        key = "".join(OrderedDict.fromkeys(key))

    # Constructing the 5x5 matrix
    matrix = []
    row = []
    alphabet = list(range(97,123))
    alphabet.remove(105) # Remove 'i' from alphabet easier conversion.
    for letter in key:
        alphabet.remove(ord(letter))
        row.append(letter)
        
        if len(row) == 5:
            matrix.append(row)
            row = []
        
    for a in alphabet:
        row.append(chr(a))
        if len(row) == 5:
            matrix.append(row)
            row = []

    return matrix

def playfairCipher(message, key):
    # Checks that both message and key contain only alphanumeric characters.
    #if(key.isalnum() and message.isalnum()):
    # TODO: Include randomisation for i/j
    # TODO: That comment up there
    encodedText = preparePlaintext(message)
    print('Encoded Text: ', encodedText)
    matrix = np.matrix(constructMatrix(key))
    print('Matrix: ', matrix)
    cipheredText = []

    for pair in encodedText:
        print('Current Pair:', pair)
        transformedPair = ''
        firstLetterCoords = np.where(matrix == pair[0])
        print('First Letter Coords: ', firstLetterCoords)
        secondLetterCoords = np.where(matrix == pair[1])
        print('Second Letter Coords: ', secondLetterCoords)
        if firstLetterCoords[0] == secondLetterCoords[0]:
            transformedPair += matrix.item((firstLetterCoords[0],(firstLetterCoords[1]+1) % 5))
            transformedPair += matrix.item((secondLetterCoords[0],(secondLetterCoords[1]+1) % 5))
        elif firstLetterCoords[1] == secondLetterCoords[1]:
            transformedPair += matrix.item(((firstLetterCoords[0]+1) % 5,firstLetterCoords[1]))
            transformedPair += matrix.item(((secondLetterCoords[0]+1) % 5,secondLetterCoords[1]))
        else:
            transformedPair += matrix.item((secondLetterCoords[0],firstLetterCoords[1]))
            transformedPair += matrix.item((firstLetterCoords[0],secondLetterCoords[1]))
        cipheredText.append(transformedPair)

    return cipheredText        

print(playfairCipher("thequickbrownfoxjumpedoverthelazydog", "derp"))
    