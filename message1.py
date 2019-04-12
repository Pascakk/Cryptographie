from math import floor, ceil

with open("message1.txt","r") as file:
    message = file.read()
    c_diametre = 2
    taille = len(message)
    dist = floor(taille/c_diametre)
    lignes = floor(taille/dist)
    
    def scytale(cle, message):
        """ Prend en argument un entier (la clé) et une chaine de caractères (le message à décoder) et renvoie un chaine de caractères (le message décodé)"""
        nbLignes = cle
        nbColonnes = int(ceil(len(message) / float(cle)))
        reste = (nbColonnes*nbLignes) - len(message)
        tabClair = [''] * nbColonnes # Tableau contenant les fragments de message décodés
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