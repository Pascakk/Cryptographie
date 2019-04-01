from math import floor, ceil
from fractions import gcd
from functools import reduce
from tqdm import tqdm, trange
num = 6
with open("message" + str(num) + ".txt", encoding="utf8") as file:
    message = file.read()

def find_gcd(list):
    x = reduce(gcd, list)
    return x

def taille_cle(length, number):
    distances = []
    for ref in range(len(message)-length):
        if len(distances) > number:
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
    return find_gcd(distances)

tailleCle = taille_cle(4,10)
print(tailleCle)

intervalleCle = []

'''
for i in range (6):
    intervalleCle.append("||")
    old = ord(message[i*tailleCle])
    for j in range (tailleCle):
        print(ord(message[i*tailleCle+j]))
        intervalleCle.append(ord(message[i*tailleCle+j])-old)
        old = ord(message[i*tailleCle+j])
print(intervalleCle)
'''

intervalle = []

for i in range (6):
    intervalle.append("||")
    for j in range (tailleCle):
        intervalle.append([message[i*tailleCle+j],ord(message[i*tailleCle+j])])
print(intervalle)