# Fonctionne pour les messages 2 à 5
# erreur d'execution avec le 4

# Parametres :
fichier = "message5.txt"
signature = "Joël"
tailleCle = 3
cle = []

with open(fichier, encoding="utf8") as file:
    # Ouverture du message
    message = file.read()

    # Création de la clé à partir des derniers caractères du message
    for i in range(1, tailleCle + 1):
        cle.append(ord(message[-i]) - ord(signature[-i]))
    print(cle)
    decrypte = ""
    posCle = 0
    # Reconstitution du message
    for i in range(1, len(message)):
        if message[-i] != "\n":
            try:
                caractere = ord(message[-i]) - cle[posCle]
                assert caractere >= 0, f"Caractere {caractere} est négatif. {ord(message[-i])}, {cle[posCle]}"
            except AssertionError:
                caractere = 0
            decrypte = chr(caractere) + decrypte
        else:
            decrypte = "\n" + decrypte
        posCle = (posCle + 1) % tailleCle

print(decrypte)
