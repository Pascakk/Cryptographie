from math import floor, ceil
from fractions import gcd
from functools import reduce
#from tqdm import tqdm, trange
from collections import Counter # Recherche de caract�re le plus fr�quent

def ouvrir_message(num):
    '''Ouvre le message correspondant au fichier donn� en entr�e'''
    with open("message" + str(num) + ".txt", encoding="utf8") as file:
        contenu = file.read()
    return contenu

def plusFrequent(D):
    '''prend un dictionnaire et renvoie la cl� dont l'indice est le plus grand'''
    maxi = 0
    car = ""
    for i in D:
        if D[i] > maxi:
            maxi = D[i]
            car = i
    return car

def find_gcd(list):
    '''renvoie le plus grand d�nominateur commun entre les nombres d'une liste'''
    x = reduce(gcd, list)
    return x

def taille_cle(length, nbRepetitions, nbSequences):
    '''d�termine la taille de la cl� par mesure de la distance entre des r�p�titions dans le texte. On cherche 'nbRepetitions' r�p�titions de 'length' caract�res nbSequences fois.'''
    distances = [] # Tableau contenant les distances entre deux r�p�titions
    sequences = [] # Contient les s�quences trouv�es v�rifiant les propri�t�s demand�es (utile pour le d�bug)
    taillesPossibles = [] # Contient les pgcd des distances entre les s�quences r�p�t�es
    for ref in range(tailleMessage-length):
        # Conditions d'arrêt
        if len(distances) > nbRepetitions: # Quand on a trouv� le bon nombre de r�p�titions
            sequences.append(pattern) # Ajout de la s�quence et du pgcd entre les distances de ses r�p�titions dans le tableau -> [sequence,pgcd]
            taillesPossibles.append(find_gcd(distances))
            if len(sequences) > nbSequences: # Quand on a trouv� le bon nombre de s�quences r�p�t�es nbRepetitions fois dans le texte
                print(sequences)
                break
        # Recherche des r�p�titions
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
    return Counter(taillesPossibles).most_common()[0][0] # Renvoie la taille de la cl� (valeur possible la plus fr�quente)

def find_cle(tailleCle):
    # S�paration du texte en n morceaux correspondants aux caract�res encod�s par le même indice de la cl�
    T = []
    for i in range(tailleCle):
        j = 0
        T.append([])
        for j in range(floor(tailleMessage/tailleCle)):
            T[i].append(message[i+j*tailleCle])
    
    #d�cryptage de la cl� par analyse fr�quentielle
    cle = []
    for i in range(tailleCle):
        occurences = {}
        for j in T[i]: #recherche du caract�re le plus fr�quent
            if j in occurences:
                occurences[j]+=1
            else :
                occurences[j] = 1
        cle.append(ord(plusFrequent(occurences))-ref)
    return cle
        
def decrypte(cle):
    # D�cryptage du message
    tailleCle = len(cle)
    clair = ""
    indice = 0
    for i in range(tailleMessage):
        clair += chr(ord(message[i]) - cle[i%tailleCle])
    return clair

'''partie interface : '''

# n� du message � ouvrir
message = ouvrir_message(6) # Variable globale contenant le message crypt�
tailleMessage = len(message) # Variable globale contenant la taille du message
ref = ord(" ") # caract�re suppos� le plus utilis� (e, a ou l'espace en francais)
# Affichage des r�sultats
cle = find_cle(taille_cle(4, 3, 4)) # taille de la s�quence, nombre de r�p�titions, nombre de s�quences v�rifiant ces crit�res
print(decrypte(cle)) # Message en clair
print(cle) # cle correcpondant au message