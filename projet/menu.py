#-*- coding: utf-8 -*-
# Projet de programmation Python - Virus killer
# JUNG Frédéric
# DOURTHE Cyril
# THOUVENIN Arthur
import sys
import os

#Create Grid
"""
def create_grid(G):
    for i in range(10):
        list=[1,2,3,4,5,6,7,8,9,10]
        G.append(list)
"""
def create_grid(grid):
    for i in range(10):
        list=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        grid.append(list)

def print_grid(grid):
    print "\n\n\n"
    print "------------ VIRUS KILLER ---------------"
    print "-----------------------------------------"
    y=0
    while y<9:
        x=0
        for h in range(9):
            print "|",grid[x][y], 
            x=x+1
        print "|",grid[x][y],"|"
        print"-----------------------------------------"
        y=y+1

#Movment Player
#Régler le probleme out of range quand sort de la grille

def player(G):
    x=0
    y=0
    for j in range(len(G)): #chercher la position du joueur
        for i in G[j]: #mettre aussi dans une boucle for pour le G[j]
            if i == 0:
                y = G[j].index(0) # coordonées en y
                x = j #coordonées en x
                G[x][y]=" "
    movement = raw_input("où voulez-vous aller ?")
    if movement == "d":#right
        right=input("de combien de cases voulez-vous vous déplacer ?")
        if x+right >=10 :
            print "Vous ne pouvez-pas sortir de l'espace cellulaire!"
        else:
            x = x+right
    if movement == "q":#left
        left=input("de combien de cases voulez-vous vous déplacer ?")
        if x-left <= 0 :
            print "Vous ne pouvez-pas sortir de l'espace cellulaire!"
        else:    
            x = x-left
    if movement == "s":#backward
        backward=input("de combien de cases voulez-vous vous déplacer ?")
        if y+backward <= 0 :
            print "Vous ne pouvez-pas sortir de l'espace cellulaire!"
        else:    
            y = y+backward
    if movement == "z":#foreward
        if y-foreward <= 0 :
            print "Vous ne pouvez-pas sortir de l'espace cellulaire!"
        else:    
            y = y-foreward
        
    G[x][y]=0 # 0=le symbole qui matérialise le personnage dans la grille
    

######## MENU ########



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
            print_grid(grid)
        elif nb == "2":
            player(grid)
            print_grid(grid)
        elif nb == "0":
            print "Bye"
            sys.exit()
        else:
            print "ERREUR : mauvaise valeur"
    

######## MAIN ########


grid=[]

x=8
y=8

create_grid(grid)

grid[x][y]=0



print "start ------>", 1 #faire la boucle avec la sortie
print "stop  ------>", 0

rep=input()
commandes(rep)


