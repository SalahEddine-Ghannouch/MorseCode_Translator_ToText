import dictionary_finger_morse as dict

def encryptor(text):
    encrypted_text= ""
    for letter in text:
        if letter != " ":
            encrypted_text= encrypted_text + dict.MORSE_CODE_DICT.get(letter) + ""
        else:
            encrypted_text += " "
    print("The morse code from finger detection : ",encrypted_text)
    return(encrypted_text)
    
