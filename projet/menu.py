#-*- coding: utf-8 -*-
# Projet de programmation Python - Virus killer
# JUNG Frédéric
# DOURTHE Cyril
# THOUVENIN Arthur

import os

#Create Grid

def create_grid(G):
    for i in range(10):
        list=[1,2,3,4,5,6,7,8,9,10]
        G.append(list)

#Movment Player

def player(x,y,G):
    for i in G:
        if i == 0:
            print x
            print y            
    movement = raw_input("où voulez-vous aller ?")
    if movement == "s":#backward
        x = x+1
    if movement == "z":#foreward
        x = x-1
    if movement == "d":#righ
        y = y+1
    if movement == "q":#left
        y = y-1
    G[x][y]=0
    
    
    
    
    
    t
    

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
            player(x,y,grid)
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


