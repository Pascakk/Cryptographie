from math import floor, ceil
from fractions import gcd
from functools import reduce
from tqdm import tqdm, trange
num = 6 #n° du fichier à décoder
ref = ord(" ") #caractère supposé le plus utilisé


with open("message" + str(num) + ".txt", encoding="utf8") as file:
    message = file.read()

tailleMessage = len(message)

def plusFrequent(D):
    '''prend un dictionnaire et renvoie la clé dont l'indice est le plus grand'''
    maxi = 0
    car = ""
    for i in D:
        if D[i] > maxi:
            maxi = D[i]
            car = i
    print (car)
    return car

def find_gcd(list):
    '''renvoie le plus grand dénominateur commun entre les nombres d'une liste'''
    x = reduce(gcd, list)
    return x

def taille_cle(length, number):
    '''détermine la taille de la clé par mesure de la distance entre des répétitions dans le texte. On cherche 'number' répétitions de 'length' caractères'''
    distances = [] #tableau contenant les distances entre deux répétitions
    sequences = [] #contient des tuples : les séquences répétées et le gcd entre les distances
    for ref in range(tailleMessage-length):
        if len(distances) > number:
            sequences.append([pattern, find_gcd(distances)])
            if len(sequences) > 4:
                print(sequences)
                break
        last = ref
        pattern = message[ref:ref+length]
        distances = []
        for i in range (ref+1, len(message)-length):
                test = message[i:i+length]
                if test == pattern:
                    distances.append(i-last)
                    last = i
                    print(str(ref) + ' "' + pattern + '"' + " pareil que " + str(i) + ' "' + test + '"')
                    print(distances)
    return sequences[0][1] #il faudrait prendre le pgcd le plus fréquent pour plus de précision

tailleCle = taille_cle(4,3)
print(tailleCle)

#Séparation du texte en n morceaux correspondants aux caractères encodés par le même indice de la clé
T = []
for i in range(tailleCle):
    j = 0
    T.append([])
    for j in range(floor(tailleMessage/tailleCle)):
        T[i].append(message[i+j*tailleCle])
print(T)

#décryptage de la clé par analyse fréquentielle
cle = []
for i in range(tailleCle):
    occurences = {}
    for j in T[i]: #recherche du caractère le plus fréquent
        if j in occurences:
            occurences[j]+=1
        else :
            occurences[j] = 1
    print(occurences)
    cle.append(ord(plusFrequent(occurences))-ref)

#décryptage du message
clair = ""
indice = 0
for i in range(tailleMessage):
    clair += chr(ord(message[i]) - cle[i%tailleCle])
print(clair)
print(cle)