#-*- coding: utf-8 -*-
# Projet de programmation Python - Virus killer
# JUNG Frédéric
# DOURTHE Cyril
# THOUVENIN Arthur
import sys
import os

#Create Grid

def create_grid(grid):
    for i in range(10):
        list=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        grid.append(list)

def print_grid(grid):
    print "\n\n\n"
    print "------------ VIRUS KILLER ---------------"
    print "-----------------------------------------"
    y=0
    while y<=9:
        x=0
        for h in range(9):
            print "|",grid[x][y], 
            x=x+1
        print "|",grid[x][y],"|"
        print"-----------------------------------------"
        y=y+1

#Localisation du joueur
#vraiment nécessaire ? car initialisation coordonnées connus 
def location(G,P):
    x=0
    y=0
    for j in range(len(G)): #chercher la position du joueur
        for i in G[j]: #mettre aussi dans une boucle for pour le G[j]
            if i == 0:
                y = G[j].index(0) # coordonées en y
                x = j #coordonées en x
                P.append(x)
                P.append(y)
                
#Movment Player
#Régler le probleme out of range quand sort de la grille -> Ok
#code dupliqué pour la gestion d'erreur out of range
            
def move(G,P):
    movement = raw_input("où voulez-vous aller ?")
    x=P[0]
    y=P[1]
    G[x][y]=" " #remplacer son ancienne position par une case vide
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
        foreward=input("de combien de cases voulez-vous vous déplacer ?")
        if y-foreward <= 0 :
            print "Vous ne pouvez-pas sortir de l'espace cellulaire!"
        else:    
            y = y-foreward
    G[x][y]=0 # 0=le symbole qui matérialise le personnage dans la grille
    P[0]=x
    P[1]=y

def drugs_inventory(I):#médicament=bombe
    print "\n"
    print "Medicament       Portée"
    for w in I :
        print w[1], "   ", w[0], "---------->" ,"[" ,w[2], "]"
    print "\n"
    tmp=input("Quelle médicament voulez vous utiliser ?")
    I[tmp][1]=(I[tmp][1])-1
    #rajouter un return des dégats
    if I[tmp][1] == 0:
        del I[tmp] #supprime un élément de l'inventaire
       
######## MENU ########

def menu(lol):
    print "====================================== Virus Killer ======================================="
    print "\n"
    print "taper [1] pour commencer"
    print "taper [2] pour vous déplacer"
    print "taper [3] pour déposer un médicament"
    print "taper [0] pour quitter"
    print "\n"
    print "==========================================================================================="
 
def commandes(nb): 
    while nb != 0:
        menu(0)
        nb=raw_input() 
        if nb == "1":
            os.system("clear")
            print_grid(grid)
        elif nb == "2": #player movement
            location(grid,position)
            move(grid,position)
            print_grid(grid)
        elif nb == "3":
            os.system("clear")
            print_grid(grid)
            drugs_inventory(inventory)
        elif nb == "0":
            print "Bye"
            sys.exit()
        else:
            print "ERREUR : mauvaise valeur"
    

######## MAIN ########

Items={"Bombe_nucleaire":8,"Grande_bombe":6,"Moyenne_bombe":4,"Petite_bombe":2}

inventory=[]
Bombe_nucleaire=["A",1,Items["Bombe_nucleaire"]]
Grande_bombe =["B",1,Items["Grande_bombe"]]
Moyenne_bombe=["C",1,Items["Moyenne_bombe"]]
Petite_bombe=["D",1,Items["Petite_bombe"]]

#initialisation 4 bombes
inventory.append(Bombe_nucleaire)
inventory.append(Grande_bombe)
inventory.append(Moyenne_bombe)
inventory.append(Petite_bombe)

grid=[]

position=[]

create_grid(grid)

#Initialisation  
#le joueur est matérialisé par un 0 sur la grille
grid[4][4]=0 #position initiale définie x=0 ;y=0 

print "start ------>", 1 #faire la boucle avec la sortie
print "stop  ------>", 0

rep=input()
commandes(rep)

