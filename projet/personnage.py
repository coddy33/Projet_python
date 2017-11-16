#-*- coding: utf-8 -*-

def player(x,y):
    movement = raw_input("où voulez-vous aller ?")
    if movement == "z":
        x = x+1
    if movement == "s":
        x = x-1
    if movement == "d":
        y = y+1
    if movement == "q":
        y = y-1
    return x, y
    #foreward
    #backward
    #left
    #right
    
