# defining translate and decode functions

# disc A
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation += "0"
        elif letter in "bB":
            translation += "y"
        elif letter in "cC":
            translation += "x"
        elif letter in "dD":
            translation += "w"
        elif letter in "fF":
            translation += "u"
        elif letter in "gG":
            translation += "t"
        elif letter in "hH":
            translation += "s"
        elif letter in "jJ":
            translation += "q"
        elif letter in "kK":
            translation += "p"
        elif letter in "lL":
            translation += "o"
        elif letter in "mM":
            translation += "n"
        elif letter in "nN":
            translation += "m"
        elif letter in "pP":
            translation += "k"
        elif letter in "qQ":
            translation += "j"
        elif letter in "rR":
            translation += "i"
        elif letter in "sS":
            translation += "h"
        elif letter in "tT":
            translation += "g"
        elif letter in "vV":
            translation += "e"
        elif letter in "wW":
            translation += "d"
        elif letter in "xX":
            translation += "c"
        elif letter in "zZ":
            translation += "a"
        elif letter in "~`!@#%$^&*()_-+={[}]:;<>,.?ěščřžýáíé":
            translation += " !Invalid input! "
        else:
            translation += " "
    return translation

# disc B


def translate_2(phrase2):
    translation_2 = ""
    for letter2 in phrase2:
        if letter2 in "aA":
            translation_2 += "1"
        elif letter2 in "bB":
            translation_2 += "2"
        elif letter2 in "cC":
            translation_2 += "3"
        elif letter2 in "dD":
            translation_2 += "4"
        elif letter2 in "eE":
            translation_2 += "5"
        elif letter2 in "fF":
            translation_2 += "6"
        elif letter2 in "gG":
            translation_2 += "7"
        elif letter2 in "hH":
            translation_2 += "8"
        elif letter2 in "iI":
            translation_2 += "9"
        elif letter2 in "jJ":
            translation_2 += "10"
        elif letter2 in "kK":
            translation_2 += "11"
        elif letter2 in "lL":
            translation_2 += "12"
        elif letter2 in "mM":
            translation_2 += "13"
        elif letter2 in "nN":
            translation_2 += "14"
        elif letter2 in "oO":
            translation_2 += "15"
        elif letter2 in "pP":
            translation_2 += "16"
        elif letter2 in "qQ":
            translation_2 += "17"
        elif letter2 in "rR":
            translation_2 += "18"
        elif letter2 in "sS":
            translation_2 += "19"
        elif letter2 in "tT":
            translation_2 += "20"
        elif letter2 in "uU":
            translation_2 += "21"
        elif letter2 in "vV":
            translation_2 += "22"
        elif letter2 in "wW":
            translation_2 += "23"
        elif letter2 in "xX":
            translation_2 += "24"
        elif letter2 in "yY":
            translation_2 += "25"
        elif letter2 in "zZ":
            translation_2 += "26"
        elif letter2 in "~`!@#%$^&*()_-+={[}]:;<>,.?ěščřžýáíé":
            translation_2 += " !Invalid input! "
        else:
            translation_2 += " "
    return translation_2

    
# disc C


def translate_3(phrase3):
    translation_3 = ""
    for letter3 in phrase3:
        if letter3 in "a":
            translation_3 += "532"
    return translation_3

# disc D


def translate_4(phrase4):
    translation_4 = ""
    for letter4 in phrase4:
        if letter4 in "a":
            translation_4 += "ghj"
    return translation_4

# disc E


def decode(phrase5):
    decode = ""
    for letter in phrase5:
        if letter in "0":
            decode += "."
        elif letter in "yY":
            decode += "b"
        elif letter in "xX":
            decode += "c"
        elif letter in "wW":
            decode += "d"
        elif letter in "uU":
            decode += "f"
        elif letter in "tT":
            decode += "g"
        elif letter in "sS":
            decode += "h"
        elif letter in "qQ":
            decode += "j"
        elif letter in "pP":
            decode += "k"
        elif letter in "oO":
            decode += "l"
        elif letter in "nN":
            decode += "m"
        elif letter in "mM":
            decode += "n"
        elif letter in "lL":
            decode += "o"
        elif letter in "kK":
            decode += "p"
        elif letter in "jJ":
            decode += "q"
        elif letter in "iI":
            decode += "r"
        elif letter in "hH":
            decode += "s"
        elif letter in "gG":
            decode += "t"
        elif letter in "eE":
            decode += "v"
        elif letter in "dD":
            decode += "w"
        elif letter in "cC":
            decode += "x"
        elif letter in "aA":
            decode += "z"
        else:
            decode += " "
    return decode

# disc F


def decode_6(phrase6):
    decode_6 = ""
    for letter5 in phrase6:
        if letter5 in "1":
            decode_6 += "a"
        elif letter5 in "2":
            decode_6 += "b"
        elif letter5 in "3":
            decode_6 += "c"
        elif letter5 in "4":
            decode_6 += "d"
        elif letter5 in "5":
            decode_6 += "e"
        elif letter5 in "6":
            decode_6 += "f"
        elif letter5 in "7":
            decode_6 += "g"
        elif letter5 in "8":
            decode_6 += "h"
        elif letter5 in "9":
            decode_6 += "i"
        elif letter5 in "10":
            decode_6 += "j"
        elif letter5 in "11":
            decode_6 += "k"
        elif letter5 in "12":
            decode_6 += "l"
        elif letter5 in "13":
            decode_6 += "m"
        elif letter5 in "14":
            decode_6 += "n"
        elif letter5 in "15":
            decode_6 += "o"
        elif letter5 in "16":
            decode_6 += "p"
        elif letter5 in "17":
            decode_6 += "q"
        elif letter5 in "18":
            decode_6 += "r"
        elif letter5 in "19":
            decode_6 += "s"
        elif letter5 in "20":
            decode_6 += "t"
        elif letter5 in "21":
            decode_6 += "u"
        elif letter5 in "22":
            decode_6 += "v"
        elif letter5 in "23":
            decode_6 += "w"
        elif letter5 in "24":
            decode_6 += "x"
        elif letter5 in "25":
            decode_6 += "y"
        elif letter5 in "26":
            decode_6 += "z"
    return decode_6

# disc G


def decode_7(phrase7):
    decode_7 = ""
    for letter6 in phrase7:
        if letter6 in "532":
            decode_7 += "a"
    return decode_7

# disc H


def decode_8(phrase8):
    decode_8 = ""
    for letter7 in phrase8:
        if letter7 in "ghj":
            decode_8 += "a"
    return decode_8


###

# getting input and executing program
# choosing if user want to encode or decode


def enc_machine():
    print("Enter an option (encode/decode/cancel): ")
    option1 = input("")

    # choosing encoding disk
    if option1 == "encode":
        print("Enter an option (1/2/3/4): ")
        option2 = int(input(""))
        if option2 == 1:
            print(translate(input("Enter a phrase to encode using encryption disc 1: ")))
        elif option2 == 2:
            print(translate_2(input("Enter a phrase to encode using encryption disc 2: ")))
        elif option2 == 3:
            print(translate_3(input("Enter a phrase to encode using encryption disc 3: ")))
        elif option2 == 4:
            print(translate_4(input("Enter a phrase to encode using encryption disc 4: ")))
    # choosing decoding disk
    else:
        print("Enter an option (5/6/7/8): ")
        option3 = int(input(""))
        if option3 == 5:
            print(decode(input("Enter a phrase to decode using encryption disc 5: ")))
        elif option3 == 6:
            print(decode_6(input("Enter a phrase to decode using encryption disc 6: ")))
        elif option3 == 7:
            print(decode_7(input("Enter a phrase to decode using encryption disc 7: ")))
        elif option3 == 8:
            print(decode_8(input("Enter a phrase to decode using encryption disc 8: ")))

while True:
    
    enc_machine()  
    if 

