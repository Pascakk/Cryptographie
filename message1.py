from math import floor, ceil

with open("message1.txt","r") as file:
    message = file.read()
    c_diametre = 2
    taille = len(message)
    dist = floor(taille/c_diametre)
    lignes = floor(taille/dist)
    
def decode(c_message):
    decrypte = ""
    taille = len(c_message)
    dist = floor(taille/c_diametre)
    lignes = floor(taille/dist)
    for i in range(dist):
        for j in range(i,taille,dist):
            decrypte += message[j]
    return decrypte

print(decode(message))