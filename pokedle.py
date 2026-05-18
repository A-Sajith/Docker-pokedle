from flask import Flask, render_template, request, jsonify, session
import json
import random

app = Flask(__name__)
app.secret_key = "pokedle-secret"

with open("pokemons.json", "r", encoding="utf-8") as f:
    pokemons = json.load(f)


@app.route("/")
def accueil():
    if "pokemon_secret" not in session:
        session["pokemon_secret"] = random.choice(pokemons)

    return render_template("index.html")


@app.route("/deviner", methods=["POST"])
def deviner():

    data = request.get_json()
    nom_devine = data["nom"].strip().lower()

    pokemon_devine = next(
        (p for p in pokemons if p["nom"].lower() == nom_devine),
        None
    )

    if not pokemon_devine:
        return jsonify({"erreur": "Pokemon introuvable"})

    secret = session["pokemon_secret"]

    # Résultat des comparaisons
    resultat = {
        "nom": pokemon_devine["nom"],

        "type1": comparer_type(
            pokemon_devine["type1"],
            pokemon_devine["type2"],
            secret["type1"],
            secret["type2"],
            "type1"
        ),

        "type2": comparer_type(
            pokemon_devine["type1"],
            pokemon_devine["type2"],
            secret["type1"],
            secret["type2"],
            "type2"
        ),

        "evolution": comparer_nombre(
            pokemon_devine["evolution"],
            secret["evolution"]
        ),

        "poids": comparer_nombre(
            pokemon_devine["poids"],
            secret["poids"]
        ),

        "taille": comparer_nombre(
            pokemon_devine["taille"],
            secret["taille"]
        ),

        "generation": comparer(
            str(pokemon_devine["generation"]),
            str(secret["generation"])
        ),

        "gagne": pokemon_devine["nom"].lower() == secret["nom"].lower(),

        "valeurs": {
            "type1": pokemon_devine["type1"],
            "type2": pokemon_devine["type2"],
            "evolution": pokemon_devine["evolution"],
            "poids": pokemon_devine["poids"],
            "taille": pokemon_devine["taille"],
            "generation": pokemon_devine["generation"]
        }
    }

    return jsonify(resultat)


@app.route("/nouveau", methods=["POST"])
def nouveau():

    session["pokemon_secret"] = random.choice(pokemons)

    return jsonify({"ok": True})


def comparer(val1, val2):

    if val1 == val2:
        return "vert"

    return "rouge"


# Comparaison des types
def comparer_type(devine1, devine2, secret1, secret2, type_actuel):

    # TYPE 1
    if type_actuel == "type1":

        if devine1 == secret1:
            return "vert"

        elif devine1 == secret2 and secret2 not in ["", None]:
            return "orange"

        else:
            return "rouge"

    # TYPE 2
    elif type_actuel == "type2":

        if devine2 == secret2:
            return "vert"

        elif devine2 == secret1 and secret1 not in ["", None]:
            return "orange"

        else:
            return "rouge"


def comparer_nombre(val1, val2):

    # Exact
    if val1 == val2:
        return "vert"

    # Proche (20%)
    elif abs(val1 - val2) <= val2 * 0.2:
        return "orange"

    # Faux
    return "rouge"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)