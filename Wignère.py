from math import floor, ceil
from fractions import gcd
from functools import reduce
from tqdm import tqdm, trange
num = 6
with open("message" + str(num) + ".txt", encoding="utf8") as file:
    message = file.read()

tailleMessage = len(message)

def find_gcd(list):
    x = reduce(gcd, list)
    return x


def taille_cle(length, number):
    distances = []
    sequences = []
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
    return sequences[0][1] #il faudrait prendre le pgcd le plus fréquent

tailleCle = taille_cle(4,6)
print(tailleCle)


T = []
for i in range(tailleCle):
    j = 0
    T.append([])
    for j in range(floor(tailleMessage/tailleCle)):
        T[i].append(message[i+j*tailleCle])

print(T)
print(len(T))
    