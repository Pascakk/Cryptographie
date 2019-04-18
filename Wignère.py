#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import floor, ceil
from fractions import gcd
from functools import reduce
#from tqdm import tqdm, trange
from collections import Counter # Recherche de caractère le plus fréquent

def ouvrir_message(num):
    '''Ouvre le message correspondant au fichier donné en entrée'''
    with open("message" + str(num) + ".txt", encoding="utf8") as file:
        contenu = file.read()
    return contenu

def plusFrequent(D):
    '''prend un dictionnaire et renvoie la clé dont l'indice est le plus grand'''
    maxi = 0
    car = ""
    for i in D:
        if D[i] > maxi:
            maxi = D[i]
            car = i
    return car

def find_gcd(list):
    '''renvoie le plus grand dénominateur commun entre les nombres d'une liste'''
    x = reduce(gcd, list)
    return x

def taille_cle(length, nbRepetitions, nbSequences):
    '''détermine la taille de la clé par mesure de la distance entre des répétitions dans le texte. On cherche 'nbRepetitions' répétitions de 'length' caractères nbSequences fois.'''
    distances = [] # Tableau contenant les distances entre deux répétitions
    sequences = [] # Contient les séquences trouvées vérifiant les propriétés demandées (utile pour le débug)
    taillesPossibles = [] # Contient les pgcd des distances entre les séquences répétées
    for ref in range(tailleMessage-length):
        # Conditions d'arrêt
        if len(distances) > nbRepetitions: # Quand on a trouvé le bon nombre de répétitions
            sequences.append(pattern) # Ajout de la séquence et du pgcd entre les distances de ses répétitions dans le tableau -> [sequence,pgcd]
            taillesPossibles.append(find_gcd(distances))
            if len(sequences) > nbSequences: # Quand on a trouvé le bon nombre de séquences répétées nbRepetitions fois dans le texte
                print(sequences)
                break
        # Recherche des répétitions
        last = ref
        pattern = message[ref:ref+length]
        distances = []
        for i in range (ref+1, len(message)-length): 
                test = message[i:i+length]
                if test == pattern:
                    distances.append(i-last)
                    last = i
                    """
                    print(str(ref) + ' "' + pattern + '"' + " pareil que " + str(i) + ' "' + test + '"')
                    print(distances)
                    """
    return Counter(taillesPossibles).most_common()[0][0] # Renvoie la taille de la clé (valeur possible la plus fréquente)

def find_cle(tailleCle):
    # Séparation du texte en n morceaux correspondants aux caractères encodés par le mÃªme indice de la clé
    T = []
    for i in range(tailleCle):
        j = 0
        T.append([])
        for j in range(floor(tailleMessage/tailleCle)):
            T[i].append(message[i+j*tailleCle])
    
    #décryptage de la clé par analyse fréquentielle
    cle = []
    for i in range(tailleCle):
        occurences = {}
        for j in T[i]: #recherche du caractère le plus fréquent
            if j in occurences:
                occurences[j]+=1
            else :
                occurences[j] = 1
        cle.append(ord(plusFrequent(occurences))-ref)
    return cle
        
def decrypte(cle):
    # Décryptage du message
    tailleCle = len(cle)
    clair = ""
    indice = 0
    for i in range(tailleMessage):
        clair += chr(ord(message[i]) - cle[i%tailleCle])
    return clair

'''partie interface : '''

# n° du message à ouvrir
message = ouvrir_message(6) # Variable globale contenant le message crypté
tailleMessage = len(message) # Variable globale contenant la taille du message
ref = ord(" ") # caractère supposé le plus utilisé (e, a ou l'espace en francais)
# Affichage des résultats
cle = find_cle(taille_cle(4, 3, 4)) # taille de la séquence, nombre de répétitions, nombre de séquences vérifiant ces critères
print(decrypte(cle)) # Message en clair
print(cle) # cle correcpondant au message