import random 
import string
def generator_mot_de_passe(longueur):
    if longueur < 4:
        print("la longueur doit être d'au moins 4.")
        return ""
    minuscule = random.choice(string.ascii_lowercase)
    majuscule = random.choice(string.ascii_uppercase)
    chiffre = random.choice(string.digits)
    symbole = random.choice(string.punctuation)

    print([minuscule, majuscule, chiffre, symbole])

    tous_les_caracteres = string.ascii_letters + string.digits + string.punctuation 
    reste = [random.choice(tous_les_caracteres) for _ in range(longueur - 4)]
    mot_de_passe_liste = [minuscule, majuscule, chiffre, symbole] + reste
    random.shuffle(mot_de_passe_liste)

    return "".join(mot_de_passe_liste)


if __name__ == "__main__":
    longueur = int(input("Longueur du mot de passe : "))
    mot_de_passe = generator_mot_de_passe(longueur)

    if mot_de_passe !="":
        print("Mot de passe généré :", mot_de_passe)