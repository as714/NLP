# coding: utf-8

def stateGenerator(x,y,z):
    str = unicode(x) + u"時の" + unicode(y) + u"は" + unicode(z)
    return str

statement = stateGenerator("12",u"気温","22.4")

print statement
