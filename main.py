# defining translate and decode functions

# disc A
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "0"
        elif letter in "bB":
            translation = translation + "y"
        elif letter in "cC":
            translation = translation + "x"
        elif letter in "dD":
            translation = translation + "w"
        elif letter in "fF":
            translation = translation + "u"
        elif letter in "gG":
            translation = translation + "t"
        elif letter in "hH":
            translation = translation + "s"
        elif letter in "jJ":
            translation = translation + "q"
        elif letter in "kK":
            translation = translation + "p"
        elif letter in "lL":
            translation = translation + "o"
        elif letter in "mM":
            translation = translation + "n"
        elif letter in "nN":
            translation = translation + "m"
        elif letter in "pP":
            translation = translation + "k"
        elif letter in "qQ":
            translation = translation + "j"
        elif letter in "rR":
            translation = translation + "i"
        elif letter in "sS":
            translation = translation + "h"
        elif letter in "tT":
            translation = translation + "g"
        elif letter in "vV":
            translation = translation + "e"
        elif letter in "wW":
            translation = translation + "d"
        elif letter in "xX":
            translation = translation + "c"
        elif letter in "zZ":
            translation = translation + "a"
        elif letter in "~`!@#$%^&*()_-+={[}]:;<>,.?/\|ěščřžýáíé":
            translation = translation + " !Invalid input! "
        else:
            translation = translation + " "
    return translation

# disc B


def translate_2(phrase2):
    translation_2 = ""
    for letter2 in phrase2:
        if letter2 in "a":
            translation_2 = translation_2 + "1"
        elif letter2 in "b":
            translation_2 = translation_2 + "2"
        elif letter2 in "c":
            translation_2 = translation_2 + "3"
            
    return translation_2

# disc C


def translate_3(phrase3):
    translation_3 = ""
    for letter3 in phrase3:
        if letter3 in "a":
            translation_3 = translation_3 + "532"
    return translation_3

# disc D


def translate_4(phrase4):
    translation_4 = ""
    for letter4 in phrase4:
        if letter4 in "a":
            translation_4 = translation_4 + "ghj"
    return translation_4

# disc E


def decode(phrase5):
    decode = ""
    for letter in phrase5:
        if letter in "0":
            decode = decode + "."
        elif letter in "yY":
            decode = decode + "b"
        elif letter in "xX":
            decode = decode + "c"
        elif letter in "wW":
            decode = decode + "d"
        elif letter in "uU":
            decode = decode + "f"
        elif letter in "tT":
            decode = decode + "g"
        elif letter in "sS":
            decode = decode + "h"
        elif letter in "qQ":
            decode = decode + "j"
        elif letter in "pP":
            decode = decode + "k"
        elif letter in "oO":
            decode = decode + "l"
        elif letter in "nN":
            decode = decode + "m"
        elif letter in "mM":
            decode = decode + "n"
        elif letter in "lL":
            decode = decode + "o"
        elif letter in "kK":
            decode = decode + "p"
        elif letter in "jJ":
            decode = decode + "q"
        elif letter in "iI":
            decode = decode + "r"
        elif letter in "hH":
            decode = decode + "s"
        elif letter in "gG":
            decode = decode + "t"
        elif letter in "eE":
            decode = decode + "v"
        elif letter in "dD":
            decode = decode + "w"
        elif letter in "cC":
            decode = decode + "x"
        elif letter in "aA":
            decode = decode + "z"
        else:
            decode = decode + " "
    return decode

# disc F


def decode_6(phrase6):
    decode_6 = ""
    for letter5 in phrase6:
        if letter5 in "1":
            decode_6 = decode_6 + "a"
    return decode_6

# disc G


def decode_7(phrase7):
    decode_7 = ""
    for letter6 in phrase7:
        if letter6 in "532":
            decode_7 = decode_7 + "a"
    return decode_7

# disc H


def decode_8(phrase8):
    decode_8 = ""
    for letter7 in phrase8:
        if letter7 in "ghj":
            decode_8 = decode_8 + "a"
    return decode_8

###

# getting input and executing program
# choosing if user want to encode or decode

print("Enter an option (encode/decode): ")
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
