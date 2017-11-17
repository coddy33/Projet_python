#-*- coding: utf-8 -*-
# Projet de programmation Python - Virus killer
# JUNG Frédéric
# DOURTHE Cyril
# THOUVENIN Arthur

import os

def create_grid(grid):
    for i in range(10):
        list=[1,2,3,4,5,6,7,8,9,10]
        grid.append(list)

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
    

######## MENU ########

import sys

def menu(lol):
    print "====================================== Virus Killer ======================================="
    print "\n"
    print "taper 1 pour commencer"
    print "taper 2 pour vous déplacer"
    print "taper 0 pour quitter"
    print "\n"
    print "==========================================================================================="
 
def commandes(nb): 
    while nb != 0:
        menu(0)
        nb=raw_input() 
        if nb == "1":
            os.system("clear")
            for i in range(10):
                print grid[i]
        if nb == "2":
            player(x,y)
            for i in range(10):
                print grid[i]
        elif nb == "0":
            print "Bye"
            sys.exit()
        else:
            print "ERREUR : mauvaise valeur"
    

######## MAIN ########


grid=[]

x=5
y=4

create_grid(grid)

grid[x][y]=0





print "start ------>", 1 #faire la boucle avec la sortie
print "stop  ------>", 0

rep=input()
commandes(rep)


