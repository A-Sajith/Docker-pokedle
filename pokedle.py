from flask import Flask, render_template, request, jsonify, session
import json
import random

app = Flask(__name__)
app.secret_key = "pokedle-secret"

# Chargement des pokemons
with open("pokemons.json", "r", encoding="utf-8") as f:
    pokemons = json.load(f)

@app.route("/")
def accueil():
    # On choisit un pokemon secret au démarrage de la session
    if "pokemon_secret" not in session:
        session["pokemon_secret"] = random.choice(pokemons)
    return render_template("index.html")

@app.route("/deviner", methods=["POST"])
def deviner():
    data = request.get_json()
    nom_devine = data["nom"].strip().lower()
    
    # On cherche le pokemon deviné dans la liste
    pokemon_devine = next((p for p in pokemons if p["nom"].lower() == nom_devine), None)
    
    if not pokemon_devine:
        return jsonify({"erreur": "Pokemon introuvable"})
    
    secret = session["pokemon_secret"]
    
    # Comparaison de chaque attribut
    resultat = {
    "nom": pokemon_devine["nom"],
    "type1": comparer(pokemon_devine["type1"], secret["type1"]),
    "type2": comparer(pokemon_devine["type2"], secret["type2"]),
    "evolution": comparer_nombre(pokemon_devine["evolution"], secret["evolution"]),
    "poids": comparer_nombre(pokemon_devine["poids"], secret["poids"]),
    "taille": comparer_nombre(pokemon_devine["taille"], secret["taille"]),
    "generation": comparer(str(pokemon_devine["generation"]), str(secret["generation"])),
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

def comparer_nombre(val1, val2):
    if val1 == val2:
        return "vert"
    elif abs(val1 - val2) <= val2 * 0.2: 
        return "orange"
    return "rouge"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
from flask import Flask, render_template, request, jsonify, session
import json
import random

app = Flask(__name__)
app.secret_key = "pokedle-secret"

# Chargement des pokemons
with open("pokemons.json", "r", encoding="utf-8") as f:
    pokemons = json.load(f)

@app.route("/")
def accueil():
    # On choisit un pokemon secret au démarrage de la session
    if "pokemon_secret" not in session:
        session["pokemon_secret"] = random.choice(pokemons)
    return render_template("index.html")

@app.route("/deviner", methods=["POST"])
def deviner():
    data = request.get_json()
    nom_devine = data["nom"].strip().lower()
    
    # On cherche le pokemon deviné dans la liste
    pokemon_devine = next((p for p in pokemons if p["nom"].lower() == nom_devine), None)
    
    if not pokemon_devine:
        return jsonify({"erreur": "Pokemon introuvable"})
    
    secret = session["pokemon_secret"]
    
    # Comparaison de chaque attribut
    resultat = {
    "nom": pokemon_devine["nom"],
    "type1": comparer(pokemon_devine["type1"], secret["type1"]),
    "type2": comparer(pokemon_devine["type2"], secret["type2"]),
    "evolution": comparer_nombre(pokemon_devine["evolution"], secret["evolution"]),
    "poids": comparer_nombre(pokemon_devine["poids"], secret["poids"]),
    "taille": comparer_nombre(pokemon_devine["taille"], secret["taille"]),
    "generation": comparer(str(pokemon_devine["generation"]), str(secret["generation"])),
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

def comparer_nombre(val1, val2):
    if val1 == val2:
        return "vert"
    elif abs(val1 - val2) <= val2 * 0.2: 
        return "orange"
    return "rouge"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)