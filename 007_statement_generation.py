# coding: utf-8

def stateGenerator(x,y,z):
    str = x + "時の" + y + "は" + z
    return str

statement = stateGenerator("12","気温","22.4")

print statement
