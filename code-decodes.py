from math import floor, ceil

c_diametre = 3
"""
message = "Bonjour, J'ai bien reçu votre candidature à Télécom ParisTech. Dans le cadre du processus de recrutement, vous allez passer deux entretiens de motivation qui sont prévus mardi 29 janvier après midi, dans les locaux de Télécom ParisTech : un entretien avec Olivier Hudry (enseignant chercheur au département Informatique et Réseaux) et un entretien avec Bertrand David (directeur de la formation initiale). Je vous envoie demain matin les heures de passage pour chacun de vous. Bonne après-midi, Bien cordialement, "
"""
message = "abcdefghijkl"

def encode(message):
    code = ""
    taille = len(message)
    ID = 0
    ligne = 0
    for i in range(taille):
        code += message[ID]
        if ID + c_diametre < taille:
            ID += c_diametre
        else:
            ligne += 1
            ID = ligne
    return code

def decode(c_message):
    decrypte = ""
    taille = len(c_message)
    dist = floor(taille/c_diametre)
    lignes = floor(taille/dist)
    for i in range(dist):
        for j in range(i,taille,dist):
            decrypte += message[j]
    return decrypte

print(encode(message))
print(encode(decode(message)))
    