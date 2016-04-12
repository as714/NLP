# coding: utf-8

str1 = "paraparaparadise"
str2 = "paragraph"

# #単語bi-gram
#
# words = str.split(" ")
# word_bi_gram = []
# for i in range(len(words)-1):
#     word_bi_gram.append(words[i] + words[i+1])
#
# print word_bi_gram


#文字bi-gram
def calcBiGram(string):
    char = string.replace(" ","")
    char_bi_gram = []
    for i in range(len(char)-1):
        char_bi_gram.append(char[i] + char[i+1])

    return char_bi_gram

X = set(calcBiGram(str1))
Y = set(calcBiGram(str2))

print X.union(Y)  #和集合
print X.difference(Y)  #差集合
print X.intersection(Y) #積集合 (共通部分）
