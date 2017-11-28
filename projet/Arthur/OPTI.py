#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Projet de programmation Python - Virus killer
# JUNG Frédéric
# DOURTHE Cyril
# THOUVENIN Arthur

import sys
import os
import random
import codecs


def commandes():#is+else#input
    '''
    This function is one of the main it control course of the game
    '''
    a=0
    os.system("clear")
    while a == 0:
        print_grid(grid,inventory)
        menu()
        nb= error()
        if nb == 1:
            power_less(inventory)
            move_player(grid,location_player,inventory,location_virus)
            move_virus(grid,location_player,inventory,location_virus)
        elif nb == 2:
            drugs_inventory(inventory,grid,location_player,location_virus)
            print_grid(grid,inventory)
            os.system("clear")
        elif nb == 0:
            exit()
        else:
            os.system("clear")
            print "You make a mistake, retry please..."

def create_grid(G):
    '''
    This function make a two dimension grid , it make 10 list (length of 10values) in the list grid[] ==> grid[][](10x10)

    Args:
        G --> the grid []
    '''
    for i in range(10):
        list=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        G.append(list)

def depop_virus(x,y,P_V):
    '''
    This function is used to suppress a virus when a medicine explosion hit him, We suppress him from list of virus position

    Args: x,y(current position choosein explode),P_V -> virus position
    '''
    index = P_V.index([x,y])
    del P_V[index]

def difficulty():#input#if+else
    '''
    This function allow player to choose his difficulty level
    '''
    lvl=error()
    if lvl==0:
        exit()
    elif lvl==1:
        new_game(easy)#easy
    elif lvl==2:
        new_game(normal)#normal
    elif lvl==3:
        new_game(hardcore)#hardcore
    elif lvl==4:
        Load()
        commandes()
    else:
        print "You make a mistake, retry please..." ###### voir si ça fonctionne et qu'on revient pas au menu

def drugs_inventory(I,G,P_J,P_V):#input#if+else
    '''
    This function is used when we have to use a medicine

    Args:
        I->inventory,G->grid,P_J->player position,P_V->virus position
    '''
    print("Choose a medicine")
    tmp=error()
    if tmp != 0 :
        explode(G,I,P_J,P_V,tmp-1)
        pop = random.randint(0,3)
        inventory[tmp-1] = dinventory[pop]
    if tmp == "0":
        exit

def easy(G):
    '''
    This function establish the position of walls for easy mode

    Arguments:
        G->grid
    '''
    listx=[2,7,4,0,4,1,6,3,8,2]
    listy=[0,1,2,3,4,5,6,7,8,9]
    for i in range(len(listx)):
        G[listx[i]][listy[i]]=wall

def error(): # error management for input
    i=1
    while i !=0:
        try :
            nb=input()
            return nb
        except NameError: # if input = string
            print "Wrong value..."
        except SyntaxError: # for special character
            print "Wrong value..."

def explode(G,I,P_J,P_V,C):#if+else
    '''
    This function make the "explosion" of medicine when player use it
    First we choose to randomly determine where go the explosion if the power is uneven
    Then we "scan" the down of the column where player set medicine and if we go over a wall or range of the grid we stop the scan
    In this scan if we meet a virus we delete him
    Then we do the same thing up the player

    Args:
        G->grid, I->inventory , P_J->player position , P_V->virus position , C->selected medicine
    '''
    x= P_J[0]
    y= P_J[1]
    size_foreward = I[C][1]//2
    size_backward = I[C][1]-size_foreward
    S=[size_foreward,size_backward]
    rand1=random.randint(0,1)
    rand2=inventory[C][1]-S[rand1]
    step_foreward = 1
    step_backward = -1
    for i in range(size_foreward):#down
        y=y+step_foreward
        if  test_grid(x,y,G) == False or G[x][y] == wall: # pas sortir de la grille ou un mur
            break
        if G[x][y] == virus:
            #G[x][y]='B'
            depop_virus(x,y,P_V)
            G[x][y] = " "
    for i in range(size_backward):#up
        y=y+step_backward
        if  test_grid(x,y,G) == False or G[x][y] == wall: # pas sortir de la grille ou un mur
            break
        if G[x][y] == virus :
            #G[x][y]='F'
            depop_virus(x,y,P_V)
            G[x][y] = " "

def exit():
    '''
    This function ask if player want to leave the game
    '''
    os.system("clear")
    print "Are you sure?"
    print "[1] YES"
    print "[0] NO"
    choice=error()
    if choice==1:
        print "Goodbye warrior!"
        Save(grid,location_virus,inventory,location_player)
        sys.exit()
    if choice == 0:
        exit
    else :
        print "Wrong value" ####### vérifier si ça fonctionne

def hardcore(G):
    '''
    This function establish the position of walls for hardcore mode

    Args:
        G->grid
        '''
    listx=[2,8,3,6,7,1,4,7,0,2,9,0,4,5,7,1,3,9,1,6,7,3,4,5,6,0,8,9,2,6]
    listy=[0,0,1,1,1,2,2,2,3,3,3,4,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9]
    for i in range(len(listx)):
        G[listx[i]][listy[i]]=wall

def lose(I):#if+else
    '''
    This function is used to know if player lose the game and then print lose

    Args:
        I->inventory
    '''
    x=0
    for i in I:
        if i[1]==0:
            x=x+1
    if x==4:
        print """
                                    __
                               ,-~¨^  ^¨-,           _,
                              /          / ;^-._...,¨/
                             /          / /         /
                            /          / /         /
                           /          / /         /
                          /,.-:''-,_ / /         /
                         _,.-:--._ ^ ^:-._ __../
                        /^         / /¨:.._¨__.;
                       /          / /      ^  /
                      /          / /         /
                     /          / /         /
                    /_,.--:^-._/ /         /
                    ^            ^¨¨-.___.:^
                    """
        os.system("clear")
        print "    __    __  _____   _   _        _       _____   _____   _____  "
        print "    \ \  / / /  _  \ | | | |      | |     /  _  \ /  ___/ | ____| "
        print "     \ \/ /  | | | | | | | |      | |     | | | | | |___  | |__   "
        print "      \  /   | | | | | | | |      | |     | | | | \___  \ |  __|  "
        print "      / /    | |_| | | |_| |      | |___  | |_| |  ___| | | |___  "
        print "     /_/     \_____/ \_____/      |_____| \_____/ /_____/ |_____| "

def menu():
    '''
    This function print the in-game menu
    '''
    print "\x1b[30;1m============\x1b[37;0m Virus Killer \x1b[30;1m===============\x1b[37;0m"
    print "\n"
    print "[1] Move."
    print "[2] Use medication."
    print "\n[0] Leave"
    print "\n"
    print "\x1b[30;1m=========================================\x1b[37;0m"

def move(G,P,I,movement,nbr_case,x,y,P_V):#P?#if+else#description
    '''
    This function is the movement properly where virus and player move step by step,
    ####a compléter#####

    Args:
        G->grid, P->player position, I->inventory, movement->function movement, nbr_case ->number of case,x ,y(current position), P_V->location virus
    '''
    loc=0
    if G[x][y] == virus:
        pos = 1
    else:
        pos = 2
    G[x][y]=" "
    x_step=0
    y_step=0
    if movement == "s":
        y_step=1
    elif movement == "z":
        y_step = -1
    elif  movement == "q":
        x_step = -1
    elif  movement == "d":
        x_step = 1
    for i in range(nbr_case):
        y=y+(y_step)
        x=x+(x_step)
        if  test_grid(x,y,G) == False or G[x][y] == wall:
            x,y = turn_back(x,y,x_step,y_step)
            break
        elif G[x][y] == ATP:
            if pos == 2 :
                power_up(I)
                pop(1,ATP,loc,G)
                G[x][y] = " "
    while G[x][y] == virus or G[x][y] == perso or G[x][y] == ATP:
        x,y = turn_back(x,y,x_step,y_step)
    return x,y

def move_player(G,P,I,P_V):#input#P?
    '''
    This function ask player where did he want to go and call a function to move player

    Args:
        G->grid, P->location player, I->inventory, P_V->location virus
    '''
    movement = raw_input("Où voulez-vous aller ?")
    print ("De combien de cases voulez-vous vous déplacer ?")
    nbr_case=error()
    x=P[0]
    y=P[1]
    x,y = move(G,P,I,movement,nbr_case,x,y,P_V)
    os.system("clear")
    G[x][y]= perso
    P[0]=x
    P[1]=y

def move_virus(G,P,I,P_V):#P?
    '''
    This function is base on move_player function and allow virus to move randomly
    Here we choose a random direction then a random number of cases to move

    Args:
        G->grid, P->location player, I->inventory, P_V->location virus
    '''
    for i in range(len(P_V)):
        nbr_case=random.randint(1,9) #nb de cases entre 1 et 9
        listdirect=["z","q","s","d"]
        pos=random.randint(0,3)
        movement=listdirect[pos]
        x=P_V[i][0]
        y=P_V[i][1]
        x,y = move(G,P,I,movement,nbr_case,x,y,P_V)
        G[x][y]= virus
        P_V[i][0]=x
        P_V[i][1]=y

def new_game(level):
    level(grid)
    pop(nb_ATP,ATP,location_virus,grid)
    pop(nb_vir,virus,location_virus,grid)
    commandes()

def normal(grid):
    '''
    This function establish the position of walls for normal mode

    Args:
        G->grid
    '''
    listx=[2,8,7,3,7,4,0,2,0,4,9,1,6,1,6,3,0,8,2,6]
    listy=[0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
    for i in range(len(listx)):
        grid[listx[i]][listy[i]]=wall

def pop(nb,mol,loc,G):#if+else
    '''
    In this function we add a number of molecule randomly and for virus we save their positions

    Args:
        nb->nombre of molecule, mol->which molecule we use, loc->location, G->grid
    '''
    for i in range(nb):
        r=0
        loc_virus=[]
        while r==0:
            x=random.randint(0,9)
            y=random.randint(0,9)
            if test_grid_empty(x,y,G)==True:
                G[x][y]=mol
                if mol == virus:
                    loc_virus.append(x)
                    loc_virus.append(y)
                    loc.append(loc_virus)
                break
            if test_grid_empty(x,y,G)==False:
                continue

def power_less(I):
    '''
    This function make power -1 on each medecine and call lose(I) to know if all of medicine power are to 0 if they are = LOSE

    Args:
        I->inventory
    '''
    i = 0
    while i < 4:
        I[i][1]=I[i][1]-1
        if I[i][1] < 0 :
            I[i][1] = 0
        i = i + 1
    lose(I)

def power_up(I):
    '''
    This function give +2 to power of two random medicine

    Args:
        I->inventory
    '''
    i = 0
    while i<2:
        tmp=random.randint(0,3)
        I[tmp][1]=I[tmp][1]+1
        if I[tmp][1]>8:
            I[tmp][1]=8
        i = i + 1

def print_grid(G,I):
    '''
    This function allow to print in correct position and in a more graphical way, values in the grid then call the function print_inventory(I) to print inventory just after the grid

    Args:
        G->grid, I->inventory
    '''
    print "\n"
    print "----------- ","\x1b[33;1mVIRUS KILLER","\x1b[37;0m --------------"
    print "\x1b[30;1m+---+---+---+---+---+---+---+---+---+---+\x1b[37;1m"
    y=0
    while y<=9:
        x=0
        for h in range(9):
            print "\x1b[30;1m|\x1b[37;1m",G[x][y],
            x=x+1
        print "\x1b[30;1m|\x1b[37;1m",G[x][y],"\x1b[30;1m|\x1b[37;1m"
        print"\x1b[30;1m+---+---+---+---+---+---+---+---+---+---+\x1b[37;1m"
        y=y+1
    print_inventory(I)

def print_inventory(I):
    '''
    This function allow to print inventory wherever we want to

    Args:
        I->inventory
    '''
    i=0
    print "\x1b[30;1m\n=========== \x1b[32;1m"u"\u2624""  \x1b[37;0mInventory  \x1b[32;1m"u"\u2624"" \x1b[30;1m=============\n"
    print "        \x1b[33;1mMedicine\x1b[37;0m          \x1b[33;1mPower\x1b[37;0m"
    while i<4:
        print  "[",i+1,"]"," ",I[i][0]," -->    ",I[i][1]
        i=i+1
    print "\x1b[37;0m\n"

def print_title():
    '''
    This function is usefull to print screen title of the game
    '''
    print """\x1b[32;1m     _     _   _   _____    _   _   _____        _   _    _   _       _       _____   _____
    | |   / / | | |  _  \  | | | | /  ___/      | | / /  | | | |     | |     | ____| |  _  \\
    | |  / /  | | | |_| |  | | | | | |___       | |/ /   | | | |     | |     | |__   | |_| |
    | | / /   | | |  _  /  | | | | \___  \      | |\ \   | | | |     | |     |  __|  |  _  /
    | |/ /    | | | | \ \  | |_| |  ___| |      | | \ \  | | | |___  | |___  | |___  | | \ \\
    |___/     |_| |_|  \_\ \_____/ /_____/      |_|  \_\ |_| |_____| |_____| |_____| |_|  \_\ \x1b[37;1m"""
    print """\x1b[31;1m                 _                      _________                    _
               _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_
              dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb
              V      ~"Mb          dOOOOOOOOOOOOOOOOOb          dM"~      V
                       `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'
                        `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'
                   __     `YMMM| OP'~"YOOOOOOOOOOOP"~`YO |MMMP'     __
                 ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb.
              _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._
            <MMP'     `~YMMa_    YOOo   \x1b[37;1m@\x1b[31;1m  OOO  \x1b[37;1m@\x1b[31;1m   oOOP   _adMP~'      `YMM>
                          `YMMMM\`OOOo     OOO     oOOO'/MMMMP'
                  ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa.
                ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.
               ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.
               MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM
               YMb           ~YMMMM\`OOOOI`````IOOOOO'/MMMMP~           dMP
                `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM'
                  `'                  `OObNNNNNdOO'                   `'
                                        `~OOOOO~'
    \x1b[37;1m"""
    print """
                                             ^
                                _______     ^^^
                               |xxxxxxx|  _^^^^^_
                               |xxxxxxx| | [][]  |
                            ______xxxxx| |[][][] |
                           |++++++|xxxx| | [][][]|      METROPOLIS
                           |++++++|xxxx| |[][][] |
                           |++++++|_________ [][]|
                           |++++++|=|=|=|=|=| [] |
                           |++++++|=|=|=|=|=|[][]|
                ___________|++HH++|  _HHHH__|   _________   _________  _________
                         _______________   ______________      ______________
                __________________  ___________    __________________    ____________"""
    print "\x1b[32;1m =============================================================================================\x1b[37;1m"
    print "\n"
    print "\n"
    print "[1] START"
    print "[0] EXIT"

def speech():
    '''
    This function is a little speech that introduce some kind of context for player
    '''
    os.system('clear')
    star="\x1b[33;1m"u"\u2605""\x1b[37;1m"
    print """
=====================================================================================
|                                                                                   |
|                                ╓▄ª▀╙▀╙▀▀%w▄;                                      |
|                             ▄A▀             └▀▀v▄                                 |
|                          ╓A▀                     └█                               |    Welcome warrior,
|                         █                          ▌                              |
|                         ▌                          █                              |    You are in 2594, Humanity is in danger, recent advances in genetics,
|                        ▐                           ▐⌐                             |    robotics, and technology are driving the world to extinction.
|                        █`└└""*"*ⁿⁿⁿ══════ⁿⁿª*ff**"?└▌                             |
|                        █                            ▌                             |    A new virus appeared from nowhere, is name \x1b[31;1mSOVEREIGN!\x1b[37;1m""",virus,"""
|                       ,█¥═▄▄▄;,                 ,,;▄▌                             |
|                    ,═Γ█│\╙╕ ▀    ,▄⌠╙└└└└└└└└v▄ ,▄Ω<▌                             |    We detected 4 powerfull strains, if you succeed in destroying them, maybe humanity will have \x1b[33;1mHOPE!\x1b[37;1m
|                 ╓A▀ ,⌐▌,V╘▐▌       Q▀▀▀▄▄  .  ▄▀╙   ▌▄▄                           |
|              ,═▀  ,A  ▌Γ\ ▐▌       .│:       ▐     ▐└*w█▀▄▄                       |    For this mission you will have 4 anti-virus with different power to start.
|            ╓▀`   ╓┘   ▀▄╕ ▐= v                ▌≈=═Φ     ²Y▄▀¥▄                    |
|           ▄▌     ▌      ¥▄,▌   *      Γ       ╙¥  █         "w▀▀▄                 |    But on the field you will have \x1b[32;1mPower enhancer\x1b[37;1m : """,ATP,"""
|          ▐▌▌     ▌     ╓▀▌ █    =     [x==l, ,Ü/ ╓▀            *▄▀W,              |    they will increase two of your anti-virus by 1.
|          ║ ╙▄    █    ▄¬█  └▌   ⌐ ,⌐`  ,-~ç  ,. '█               ╙╕╙█,            |
|          ║   ╕    █  A ▐⌐   ▀⌐  ⌐/   ç▄═¬═w╓=▄¬└ █                 ╙w▀▄           |    BUT above all, pay attention at the power of your anti-virus ,
|          ▐⌐   ╙▄   ▀█ ,▌     '▀ç"   ⌐'""ⁿ¬══─*  k█                   █┘           |    if they all fall to 0 we are all dead, nothing will stop him!
|           ▌     "w   ╙▀▄        ▀▄  ╞`¬ç   ,,╓┘ █▐Ö╗               ╓█╙▀W▄         |
|        ╓▄▀█       `\ç    ▀▀≡▄ç    ▀▄╘           ▌ █ ▀▄            ▄▀ "%, ▀▄       |
|      ▄▀   ▐▌         "═ç      `╙▀   "█▄        ,▌ ▐∩  █          █`     ▀  ▀█▄▄   |
|    ▄▀     █▀             "═w,   █     "▀▄▄▄▄▄≤▀▀   ▌   ▀       ,█ ▄▄≡Φ█▀▀▀└`      |
|  ▄█═"╙╙'" ▌ █                ⌐  ▌*≈¡      ,«"      █    █     ╓▀,▀     ▀▄ ┐       |
| ▄┘        ⌐  ▀▄             ▐  ▐=     -""¬         █     █   ╓▀ █        █ ╕      |
|▄¬        ▐     '▀▄,         ▐  ▐=                  ▌     █  ╓█  ▌         ▌ ⌐     |
|▌         ▐        `▀W▄      ▐  ▐▌▄                ▀     ▄  ,▌ ╙▄█         █ ▌     |
|         1**f▄      ╓¬═▀Φ▄    ▄  ▌ └ª═▄,        ╓A└    ╓▀   █    ▀▄        █ ▀     |
|         █   ▌      ▐   ▐⌐ ▀▄ ╙  █      └-""**"-     ▄▀¬   ▐ⁿ╩"│Ö▐^▌▄.ÜΩ╣]ó▄╫╫▄▄   |
|         ▀   *      └   '    ▀ * ╙                 ^┘               ▀▀*"╙▀▀└¬      |
|                                                                                   |
|                                  \x1b[33;1mGeneral Mike Hertz\x1b[37;1m                               |
|                                                                                   |
=====================================================================================
"""
    print """
Choose your level of difficulty :

[1] Easy     : better to begin againt \x1b[31;1mSOVEREIGN!\x1b[37;1m.
[2] Normal   : you may have guts...
[3] Hardcore : finally a real warrior, let me see your true nature as a hero!""",star,"""\n
[4] Load previous game.
[0] Leave."""

def start():#input#if+else
    '''
    This function start the game and call all other functions
    '''
    os.system('clear')
    r=0
    while r == 0:
        print_title()
        rep=error()
        if rep == 1:
            speech()
            difficulty()
        if rep == 0:
            exit()
        else:
            os.system('clear')
            print "You make a mistake, retry please..."

def test_grid(x,y,G):
    '''
    This function is a test where we try to know if we are in the grid or not

    Args:
        x,y(current position), G->grid

    Return:
        True or False
    '''
    if y > len(G)-1 or y < 0 or x > len(G)-1 or x < 0:
        return False
    return True

def test_grid_empty(x,y,G):
    '''
    This function use the precedent function test_grid(x,y,G) to know if here we are in a "empty" position

    Args:
        x,y(current position), G->grid

    Return:
        True or False
    '''
    if test_grid(x,y,G)==True and G[x][y]==' ' :
        return True
    return False

def turn_back(x,y,x_step,y_step):
    '''
    This function allow the choice of direction to move player or virus

    Args:
        x,y(current position), x_step->step of x, y_step->step of y

    Return:
        x,y
    '''
    y=y-(y_step)
    x=x-(x_step)
    return x,y

def win(loc_virus):#if+else
    '''
    This function determine when player win

    Args:
        loc_virus->list of virus location
    '''
    if len(loc_virus)==0:
        os.system("clear")
        print """"
                                                            |@@@@|     |####|
                                                            |@@@@|     |####|
__    __  _____   _   _        _          __  _   __   _    |@@@@|     |####|
\ \  / / /  _  \ | | | |      | |        / / | | |  \ | |   \@@@@|     |####/
 \ \/ /  | | | | | | | |      | |  __   / /  | | |   \| |    \@@@|     |###/
  \  /   | | | | | | | |      | | /  | / /   | | | |\   |     `@@|_____|##'
  / /    | |_| | | |_| |      | |/   |/ /    | | | | \  |          (O)
 /_/     \_____/ \_____/      |___/|___/     |_| |_|  \_|       .-'''''-.
                                                              .'  * * *  `.
                                                             :  *       *  :
                                                            : ~ \x1b[33;1mW O R L D\x1b[37;1m ~ :
                                                            : ~  \x1b[33;1mH E R O\x1b[37;1m  ~ :
                                                             :  *       *  :
                                                              `.  * * *  .'
                                                                `-.....-'

"""
        print '''
                                 .''.
       .''.             *''*    :_\/_:     .
      :_\/_:   .    .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ : _\(/_  ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::. /)\*''*  .|.* '.\'/.'_\(/_'.':'.'
 : /\ : :::::  '*_\/_* | |  -= o =- /)\    '  *
  '..'  ':::'   * /\ * |'|  .'/.\'.  '._____
      *        __*..* |  |     :      |.   |' .---"|
       _*   .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''


def Save(G,P_V,I,P_J):
    file=codecs.open("save","w",encoding="utf-8")
    file.write('######### GRID ##########\n')
    for i in G:
        file.write(':,')
        for j in i:#save grid
            file.write(j)
            file.write(',')
        file.write('\n')
    file.write('\n======================================================================================\n')
    file.write('######### VIRUS LOCATION ##########\n')
    for k in P_V:#location virus
        file.write('v;')
        for t in k:
            file.write(str(t))
            file.write(';')
        file.write('\n')
    file.write('\n======================================================================================\n')
    file.write('######### INVENTORY ##########\n')
    for l in I:#inventory
        file.write('i;')
        for h in l:
            file.write(str(h))
            file.write(';')
        file.write('\n')
    file.write('\n======================================================================================\n')
    file.write('######### PLAYER POSITION ##########\n')
    file.write('p;')
    for m in P_J:#player position
        file.write(str(m))
        file.write(';')
    file.write('\n======================================================================================\n')
    file.close()

def Load():
    file=codecs.open('save',"r",encoding="utf-8")
    global grid
    global location_virus
    global inventory
    global location_player
    grid=[]
    inventory=[]
    location_player=[]
    for line in file.readlines():
        if not line:
            break
        if line.startswith(':,'):
            y=line.split(',')
            y.pop(0)
            y.pop(-1)
            grid.append(y)
        if line.startswith('v;'):
            v=line.split(';')
            v.pop(0)
            v.pop(-1)
            vir1=int(v[0])
            vir2=int(v[1])
            vir=[vir1,vir2]
            location_virus.append(vir)
        if line.startswith('i;'):
            i=line.split(';')
            i.pop(0)
            i.pop(-1)
            inv1=i[0]
            inv2=int(i[1])
            inv=[inv1,inv2]
            inventory.append(inv)
        if line.startswith('p;'):
            p=line.split(';')
            p.pop(0)
            p.pop(-1)
            print p
            p1=int(p[0])
            p2=int(p[1])
            location_player.append(p1)
            location_player.append(p2)
        else:
            continue



######################
######## MAIN ########
######################

#####Initialisation grid#####

grid=[]
create_grid(grid)
#give the initial number of ATP and Virus
nb_ATP=8
nb_vir=4

location_virus=[] #all x,y virus position will be stored here (2D list)

#####Initialisation inventory#####

dinventory=[["Immunity  ",8],["Vaccine   ",6],["Antibiotic",4],["Homeopathy",2]]
inventory=[["Immunity  ",8],["Vaccine   ",6],["Antibiotic",4],["Homeopathy",2]]

#####Define objects######

wall="\x1b[30;1m"u"\u25a9\x1b[37;1m"
perso="\x1b[33;1m"u"\u263b\x1b[37;1m"
virus="\x1b[31;1m"u"\u2620\x1b[37;1m"
ATP="\x1b[32;1m"u"\u2622\x1b[37;1m"

#####Initialisation player#####

location_player=[] #x,y of player position stored in a list
location_player.append(0)
location_player.append(0)

grid[location_player[0]][location_player[1]]= perso #position initiale définie x=0 ;y=0


start()
