#Homophonic Cipher

import random
numbers_value = [8,2,3,4,12,2,6,6,1,1,4,2,6,7,2,1,6,6,9,3,1,2,1,2,1,2]

alphabets= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def createTable():
    table= {}
    values = []
    for i in range(26):
        cipher_values = []
        while len(cipher_values)!= numbers_value[i]:
            value = random.randint(1,101)
            if value not in values:
                cipher_values.append(value)
                values.append(value)
        table[alphabets[i]] = cipher_values
    return table

table = createTable()

text = input("Enter Text:")
def encode(text):
    cipher = ""
    for i in range(len(text)):
        if text[i] != " ":
            alpha_cipher = table[text[i].upper()]
            cipher+= str(alpha_cipher[random.randint(0,len(alpha_cipher)-1)])+ " "
        else:
            cipher+="- "
    return cipher


def decrypt(cipher):
    cipher_text = cipher.split(" ")
    original_text_again= ""
    for i in range(len(text)):
        if cipher_text[i]=='-':
            original_text_again+=" "
        else:
            for j in range(26):
                values = table[alphabets[j]]
                for k in values:
                    if k ==int(cipher_text[i]):
                        original_text_again+=alphabets[j]
                        break
    return original_text_again

encodedText = encode(text)
print("PT: ",text)
print("CT: ",encodedText)
dercyptedText = decrypt(encodedText)
print("Decrypted text: ",dercyptedText)
        
