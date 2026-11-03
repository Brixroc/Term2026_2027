import random
caractere = "abcdefghijklmnopqrstuvwxyz"
longueur = int(input("longueur = "))
mot_de_passe = ""
for i in range(longueur):
    mot_de_passe+= random.choice(caractere)
print(mot_de_passe)