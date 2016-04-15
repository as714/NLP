
# coding: utf-8
import random
str ="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

words = str.split()

for word in words:
    print word
    if len(word) <= 4:
        print word
        continue
    chars = list(word[1:-1])
    random.shuffle(chars)
    print word[0] + "".join(chars) + word[-1]
