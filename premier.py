import random
caractere = "abcdefghijklmnopqrstuvwxyz"
nombre = "0123456789"
caractere_special = ",?;.:/!§"
longueur = int(input("longueur = "))
nombre = int(input("nombre = "))
special = int(input("special = "))
mot_de_passe = ""
for i in range(longueur):
    mot_de_passe+= random.choice(caractere)
for i in range(nombre):
    mot_de_passe+= random.choice(nombre)
for i in range(special):
    mot_de_passe+= random.choice(special)
print(mot_de_passe)