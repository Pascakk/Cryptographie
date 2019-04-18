#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Fonctionne pour les messages 2 Ã  5
# erreur d'execution avec le 4

# Parametres :
fichier = "message2.txt"
signature = "Joël"
tailleCle = 1
cle = []

with open(fichier, encoding="utf8") as file:
    # Ouverture du message
    message = file.read()

    # Création de la clé à  partir des derniers caractères du message
    for i in range(1, tailleCle + 1):
        cle.append(ord(message[-i]) - ord(signature[-i]))
    print(cle)
    decrypte = ""
    posCle = 0
    # Reconstitution du message
    for i in range(1, len(message)):
        if message[-i] != "\n":
            decrypte = chr(caractere) + decrypte
        else:
            decrypte = "\n" + decrypte
        posCle = (posCle + 1) % tailleCle

print(decrypte)
