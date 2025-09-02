from main import classer_age, generer_infos


def test_classer_age():
    assert classer_age(17) == "Vous êtes presque majeur"
    assert classer_age(15) == "Vous êtes adolescent"
    assert classer_age(1) == "Vous êtes un bébé"
    assert classer_age(18).startswith("Tout juste majeur")
    assert classer_age(70) == "Vous êtes sénior"
    assert classer_age(5) == "Vous êtes enfant"
    assert classer_age(30) == "Vous êtes majeur"


def test_generer_infos():
    texte = generer_infos("Eren", 20, 1.80)
    assert "Eren" in texte
    assert "20 ans" in texte
    assert "21 ans" in texte
    assert "Votre taille : 1.8 m" in texte