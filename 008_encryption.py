# coding: utf-8

str ="Today is the first day lest of my LIFE."

def cipher(input):
    ciphered_str = ""
    for char in input:
        ciphered_str  += chr(219-ord(char)) if char.islower() else char
    return ciphered_str

str = cipher(str)
print str
str = cipher(str)
print str
