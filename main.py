def classer_age(age: int) -> str:
    if age == 17:
        return "Vous êtes presque majeur"
    elif 12 <= age < 18:
        return "Vous êtes adolescent"
    elif age in (1, 2):
        return "Vous êtes un bébé"
    elif age == 18:
        return "Tout juste majeur : Félicitations"
    elif age > 60:
        return "Vous êtes sénior"
    elif age < 10:
        return "Vous êtes enfant"
    elif age >= 18:
        return "Vous êtes majeur"
    else:
        return "Vous êtes mineur"


def generer_infos(nom: str, age: int, taille: float = 0) -> str:
    infos = [
        f"Vous vous appelez {nom}, vous avez {age} ans.",
        f"L'an prochain vous aurez {age + 1} ans.",
        classer_age(age),
    ]
    if taille > 0:
        infos.append(f"Votre taille : {taille} m")
    return "\n".join(infos)


def demander_nom() -> str:
    nom = ""
    while nom == "":
        nom = input("Quel est votre nom ? ").strip()
    return nom


def demander_age(nom: str) -> int:
    while True:
        age_str = input(f"{nom}, quel est ton âge ? ")
        try:
            return int(age_str)
        except ValueError:
            print("Erreur : entre un nombre valide.")


def main():
    nom = demander_nom()
    age = demander_age(nom)
    print(generer_infos(nom, age, 1.70))


if __name__ == "__main__":
    main()