# coding: utf-8

str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine.\
 New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

def f(x,y):
    return x[:y] 

words_list = str.split(" ")
dict={}
check_Num=[0, 4, 5, 6, 7, 8, 14, 15, 18]
prefix = map(lambda x: 1 if(x in check_Num) else 2 , range(len(words_list)))
element = map(f, words_list,prefix)
print element
