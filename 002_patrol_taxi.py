# coding: utf-8

str1=u'タクシー'
str2=u'パトカー'
str3=u''

for a,b in zip(str2, str1):
    str3 = str3 + a + b

print str3
