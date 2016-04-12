# coding: utf-8

str = "I am an NLPer"

#単語bi-gram

words = str.split(" ")
word_bi_gram = []
for i in range(len(words)-1):
    word_bi_gram.append(words[i] + words[i+1])

print word_bi_gram


#文字bi-gram

char = str.replace(" ","")
char_bi_gram = []
for i in range(len(char)-1):
    char_bi_gram.append(char[i] + char[i+1])

print char_bi_gram
