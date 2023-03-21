import encryption as cipher
import dictionary_finger_morse as dict

print("\t\t\t\t***************************************")
print("\t\t\t\t     FINGERS NUMBER CODE TRANSLATOR ")
print("\t\t\t\t***************************************")

def get_code_fingerN(plain_Text):

    text_morse_code = cipher.encryptor(plain_Text.upper())

    key_list= list(dict.MORSE_CODE_DICT.keys())
    val_list= list(dict.MORSE_CODE_DICT.values())

    morse_code=""
    code_number_fingers=""


    for letters in text_morse_code:
        code_number_fingers= code_number_fingers + key_list[val_list.index(letters)]
        # morse_code= ""    
        
    print("FINGERS NUMBER CODE : "+code_number_fingers)
    result = ''
    cur_digit = code_number_fingers[0]
    cur_sum = 0

    for digit in code_number_fingers:
        if digit != cur_digit:
            result += str(cur_sum)
            cur_digit = digit
            cur_sum = int(digit)
        else:
            cur_sum += int(digit)

    result += str(cur_sum)

    print("FINGERS NUMBER CODE FINAL : "+result[:-1])
    return result[:-1]
