# scraper
Générateur de mot de passe 


# 🔐 Générateur de Mot de Passe en Python

Ce projet est un petit script Python qui permet de **générer automatiquement des mots de passe sécurisés** en utilisant des lettres, des chiffres et des symboles.

## 📌 Fonctionnalités

* Génère un mot de passe aléatoire
* Contient au minimum :

  * une lettre minuscule
  * une lettre majuscule
  * un chiffre
  * un symbole
* Longueur du mot de passe personnalisable
* Mélange aléatoire des caractères pour plus de sécurité

## 🛠️ Technologies utilisées

* Python 3
* Module `random`
* Module `string`

## 📂 Structure du code

Le programme fonctionne en plusieurs étapes :

1. Vérification de la longueur du mot de passe
2. Génération des caractères obligatoires
3. Génération des caractères restants aléatoires
4. Mélange des caractères
5. Construction et affichage du mot de passe final

## ▶️ Utilisation

1. Cloner le projet ou télécharger le fichier.

```bash
git clone https://github.com/votre-utilisateur/password-generator.git
```

2. Aller dans le dossier du projet :

```bash
cd password-generator
```

3. Lancer le script Python :

```bash
python password_generator.py
```

4. Entrer la longueur du mot de passe souhaitée.

Exemple :

```
Longueur du mot de passe : 10
Mot de passe généré : A7#kP2!xQz
```

## 📜 Exemple de code

Le script utilise les bibliothèques Python pour générer un mot de passe sécurisé :

```python
minuscule = random.choice(string.ascii_lowercase)
majuscule = random.choice(string.ascii_uppercase)
chiffre = random.choice(string.digits)
symbole = random.choice(string.punctuation)
```

Ces caractères sont ensuite mélangés pour produire un mot de passe aléatoire.

## 📈 Améliorations possibles

* Ajouter une interface graphique
* Permettre de choisir les types de caractères
* Sauvegarder les mots de passe générés
* Ajouter un générateur de plusieurs mots de passe

## 👨‍💻 Auteur

Projet réalisé pour apprendre la programmation en **Python** et comprendre la génération aléatoire de données.

## 📄 Licence

Ce projet est libre d'utilisation pour l'apprentissage et les projets personnels.

