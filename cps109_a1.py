''' -------------The Vigenere Cypher, Imad Zia -------------------------------------
My intended profession, which I have since learned is a small minority of computer science, is Cybersecurity.
In a world which is rapidly expanding technologically, we place our trust more and more on the internet and online systems.
Our private messages, passwords, and communications all share a footprint, and so long as it is out there, it can be traced.
As such, we need to find a way to mitigate the numerous issues that arise from nosy people viewing our information. Therefore,
It is for such a reason that we have ciphers. Ciphers are a way of taking information, and seemingly translating it to a new language.
Using clever formulas or even simple methods, anyone can make a cypher. Cyphers and the study of them (cryptography), have had a
long history. One of the most popular cyphers is called a Caesar Cipher, in which each alphabetical values are shifted
down a fixed position. A variant of the Caesar Cipher is the Vigenere Cipher. Firstly, I don't know why each name sounds like a kind of salad,
both Vigenere (Vinegar), and Caesar (Caesar Salad), but I digress. It uses a clever formula, along with a key to scramble the words into a ciphertext.
My code, (assuming it works correctly) should be able to encode, or decode a string using a requested key, and output it to a file.
The following code below is my foray into the world of cybersecurity and my first decent project, I hope you enjoy!



P.S You might not want to put your password in here, it'll save it to the .txt file, but if you do so make sure to send me the file :) 
'''


#creates a dictionairy which stores a value for each letter
alphaIndex = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
    'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15,
    'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
    'Y': 24, 'Z': 25}

#creates a dict to store a letter for each value
numIndex = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H',
    8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P',
    16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X',
    24: 'Y', 25: 'Z'}

#this is the menu screen which asks the user if they want to decipher or cipher a string
def menu():
    global encryptOrDecrypt
    encryptOrDecrypt = input('Hello! Would you like to:\n A) decrypt \n B) encrypt \n using the Vigenere Cypher?: ')
    encryptOrDecrypt = encryptOrDecrypt.upper()
    if encryptOrDecrypt == 'A':
        print('Decrypting String...\n\n')
        decryptString()
    elif encryptOrDecrypt == 'B':
        print('Encrypting String...\n\n')
        encryptString()
    else:
        print('\nSorry, you have entered an invalid input, please try again.\n')
        menu()
        
#Vigenere Cypher decoding requires two inputs, 1) a key, 2) a cyphertext
def askKey():
    key = input('Please enter an alphabetical key: ')
    if not key.isalpha():
        print('Invalid Input, You may have entered a number or special character, please try again: ')
        askKey()
    return key
        
#assuming we're encrypting, it acquires the plaintext, only called if we're encrypting
def getPlaintext():
    plaintext = input('Please enter an alphabetical plaintext: ')
    if not plaintext.isalpha():
        print('Invalid Input, You may have entered a number or special character, please try again: ')
        getPlaintext()
    return plaintext

#gets the text that needs to be decoded
def getCiphertext():
    ciphertext = input('Please enter an alphabetical ciphertext: ')
    if not ciphertext.isalpha():
        print('Invalid Input, You may have entered a number or special character, please try again: ')
        getCiphertext()
    return ciphertext

#figures out if it is encrypting or decrypting and based on that it gets the length of the key
def getKey():
    
    if encryptOrDecrypt == 'A':
        key = askKey()
        key = key.upper()
        global ciphertext
        ciphertext = getCiphertext()
        ciphertext = ciphertext.upper()
    
        i = 0
        fullKey = ''
    
    
        if len(key) < len(ciphertext):
            fullRepeat = (len(ciphertext) // len(key))
            remainder = (len(ciphertext) % len(key))
            while i < fullRepeat:
                fullKey = fullKey + key
                print(fullKey)
                i += 1
            fullKey = fullKey + key[:remainder]
            return (fullKey)
        
        else:
            fullRepeat = len(key) // len(ciphertext)
            remainder = len(key) % len(ciphertext)
            for i in range(fullRepeat):
                fullKey = fullKey + key
                print(fullKey)
            fullKey = fullKey + key[:remainder]
            return fullKey
        
    elif encryptOrDecrypt == 'B':
        key = askKey()
        key = key.upper()
        global plaintext
        plaintext = getPlaintext()
        plaintext = plaintext.upper()
    
        i = 0
        fullKey = ''
    
    
        if len(key) < len(plaintext):
            fullRepeat = (len(plaintext) // len(key))
            remainder = (len(plaintext) % len(key))
            while i < fullRepeat:
                fullKey = fullKey + key
                print(fullKey)
                i += 1
            fullKey = fullKey + key[:remainder]
            return (fullKey)
        
        else:
            fullRepeat = len(key) // len(plaintext)
            remainder = len(key) % len(plaintext)
            for i in range(fullRepeat):
                fullKey = fullKey + key
                print(fullKey)
            fullKey = fullKey + key[:remainder]
            return fullKey
            

# this function is only called if we selected B) at the start
def encryptString():

    #firstly, it makes sure its in uppercase to avoid errors when referring to the ciphertext
    key = getKey()
    key = key.upper()

    #same applies here, it makes sure its in uppercase to avoid errors when referring to the dict
    decrypted = plaintext
    decrypted = decrypted.upper()

    #initilizes i to index through the words, and creates an empty string where we will store our plaintext
    i = 0
    convertedPlaintext = ''

    #whilst i is less than the total size of the string, we'll get the value of the key and the ciphertext from the dict 
    while i < len(decrypted):
        decryptedVal = (alphaIndex.get(decrypted[i]))
        keyVal = alphaIndex.get(key[i])

        # this is the actual decryption formula used
        encryptVal =  (decryptedVal + keyVal + 26)%26

        #for each value we get the corresponding letter value based on number from the number dict
        encryptChar = numIndex.get(encryptVal)

        # we concatenate each letter to the final decrypted string
        convertedPlaintext += encryptChar

        # prints the change through time, indexes by 1
        print(f"Decrypted: {decrypted[i]} | Key: {key[i]} | Encrypted: {encryptChar}")
        print(f'Therefore, the final decrypted string is {convertedPlaintext}')

        i += 1
    
    # puts the resultant encryption into a file where we can easily read our result
    output = open('output_file.txt', 'w')
    output.write(f'Decrypted: {decrypted} → Encrypted: {convertedPlaintext}, KEY: {key}') 

# the code that actually decrypts the string, only called if we selected A) at the start
def decryptString():

    #firstly, it makes sure its in uppercase to avoid errors when referring to the ciphertext
    key = getKey()
    key = key.upper()

    #same applies here, it makes sure its in uppercase to avoid errors when referring to the dict
    encrypted = ciphertext
    encrypted = encrypted.upper()

    #initilizes i to index through the words, and creates an empty string where we will store our plaintext
    i = 0
    convertedPlaintext = ''

    #whilst i is less than the total size of the string, we'll get the value of the key and the ciphertext from the dict 
    while i < len(encrypted):
        encryptedVal = (alphaIndex.get(encrypted[i]))
        keyVal = alphaIndex.get(key[i])

        # this is the actual decryption formula used, notice how it is SUBTRACTION rather than addition
        decryptVal =  (encryptedVal - keyVal + 26)%26

        #for each value we get the corresponding letter value based on number from the number dict
        decryptChar = numIndex.get(decryptVal)

        # we concatenate each letter to the final decrypted string
        convertedPlaintext += decryptChar

        # prints the change through time, again, index
        print(f"Encrypted: {encrypted[i]} | Key: {key[i]} | Decrypted: {decryptChar}")
        print(f'Therefore, the final decrypted string is {convertedPlaintext}')

        i += 1
        
    #again, outputs it to the file for easy reading with a detailed description of the process
    output = open('output_file.txt', 'w')
    output.write(f'Encrypted: {encrypted} → Decrypted: {convertedPlaintext}, KEY = {key}')    
    

        
menu()