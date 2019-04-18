#!/usr/bin/env python
# -*- coding: utf-8 -*-

roues = [[1,3,4],[3,6,4],[5,8,6]]

def ouvrir_message(num):
    '''Ouvre le message correspondant au fichier donné en entrée'''
    with open("message" + str(num) + ".txt", encoding="utf8") as file:
        contenu = file.read()
    return contenu

def enigma(roues, posRoues, message, ordre):
    '''Décode le message en connaissant le nombre de roues et les chiffres présents sur chacune (roues) et en prenant une position de départ pour chaque roue (posRoues)'''
    clair = ""
    roueActuelle = 0
    for i in range(len(message)):
        print(posRoues[roueActuelle])
        clair += chr(ord(message[i])-(roues[roueActuelle][posRoues[roueActuelle]]*ordre)) # encrypte si ordre = -1, décrypte si ordre = 1
        posRoues[roueActuelle] += 1
        if posRoues[roueActuelle] == len(roues[0]):
            posRoues[roueActuelle] = 0
            roueActuelle += 1
            if roueActuelle == len(roues):
                roueActuelle = 0            
    return clair

'''partie interface : '''
# Position d'origine des roues

# n° du message à ouvrir
message = ouvrir_message(6) # Variable globale contenant le message crypté
print(enigma(roues, [0,0,0], message, 1))