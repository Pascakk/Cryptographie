#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import floor, ceil

with open("message1.txt","r") as file:
    # Ouverture du message
    message = file.read()
    c_diametre = 2
    taille = len(message)
    dist = floor(taille/c_diametre)
    lignes = floor(taille/dist)
    
    def scytale(cle, message):
        """ Prend en argument un entier (la clï¿½) et une chaine de caractï¿½res (le message ï¿½ dï¿½coder) et renvoie un chaine de caractï¿½res (le message dï¿½codï¿½)"""
        nbLignes = cle
        nbColonnes = int(ceil(len(message) / float(cle)))
        reste = (nbColonnes*nbLignes) - len(message)
        tabClair = [''] * nbColonnes # Tableau contenant les fragments de message dï¿½codes
        col = 0
        ligne = 0
        for car in message:
            tabClair[col] += car
            col += 1
            if (col == nbColonnes) or (col == nbColonnes - 1 and ligne >= nbLignes - reste):
                ligne += 1
                col = 0
        clair = ""
        for bout in tabClair:
            clair+= bout # Recollement des morceaux de message
        return clair

print(scytale(3, message))