#-*- coding: utf-8 -*-

def interface():
    ligne = "+----"
    colonne = "|    "
    for i in range(21):
        if i % 2 ==0:
            print ligne
        else:
            print colonne 


"SALUT"
interface()
