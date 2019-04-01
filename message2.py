with open("message5.txt", encoding="utf8") as file:
    message = file.read()
    signature = "Joël"
    tailleCle = 3
    cle = []
    for i in range(1, tailleCle+1):
        cle.append(ord(message[-i]) - ord(signature[-i]))
    print(cle)
    decrypte = ""
    posCle = 0
    for i in range (1,len(message)):
        if message[-i] != "\n":
            try:
                caractere = ord(message[-i]) - cle[posCle]
                assert caractere >= 0, f"Caractere {caractere} est négatif. {ord(message[i])}, {cle[posCle]}"
            except AssertionError:
                caractere = 0
            decrypte = chr(caractere) + decrypte
        else : decrypte = "\n" + decrypte
        posCle = (posCle+1)%tailleCle

print(decrypte)