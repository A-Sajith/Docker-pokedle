# Pokédle

Jeu de devinette Pokémon inspiré du Wordle, containerisé avec
Docker et déployé via un pipeline CI/CD GitHub Actions.

## Pourquoi ce projet ?

Pokémon a marqué mon enfance, alors quand j'ai cherché un projet
pour apprendre le DevOps je me suis dit : autant apprendre avec
quelque chose qui me passionne vraiment. L'idée c'était simple,
faire un Pokédle maison pour pratiquer Flask, Docker et les APIs
tout en construisant quelque chose de fun. La partie qui m'a le
plus donné du fil à retordre c'est la gestion des réponses en
JavaScript — afficher les bonnes couleurs selon les comparaisons
de stats, ça m'a bien occupé. Mais voir le jeu fonctionner pour
la première fois c'était satisfaisant.

## Technologies utilisées

- Python 3.11
- Flask (backend web)
- Docker & Docker Compose
- GitHub Actions (CI/CD)
- Docker Hub (registry d'images)
- JavaScript (frontend interactif)
- HTML / CSS

## Fonctionnement

1. Un Pokémon est choisi aléatoirement au démarrage
2. Le joueur tape un nom de Pokémon
3. Le jeu compare les stats et affiche les indices :
   - 🟢 Vert = correct
   - 🟠 Orange = proche (±20%)
   - 🔴 Rouge = faux
4. Le bouton permet de changer de Pokémon à tout moment

## Pipeline CI/CD

A chaque push sur la branche main :
1. GitHub Actions se déclenche automatiquement
2. L'image Docker est buildée
3. L'image est pushée sur Docker Hub

## Lancer le projet avec Docker

### 1. Cloner le repo
```bash
git clone https://github.com/A-Sajith/Docker-pokedle.git
```
```bash
cd Docker-pokedle
```

### 2. Lancer avec Docker Compose
```bash
docker-compose up
```

### 3. Ouvrir dans le navigateur
http://localhost:5000

### Ou directement depuis Docker Hub
docker pull ton-username/pokedle:latest
docker run -p 5000:5000 ton-username/pokedle:latest

## Structure du projet
```bash
pokedle/
├── .github/
│   └── workflows/
│       └── docker.yml    
├── templates/
│   └── index.html        
├── pokedle.py            
├── pokemons.json         
├── Dockerfile            
└── docker-compose.yml    
```
## Ce que j'ai appris

- Gérer des sessions utilisateur avec Flask
- Construire une interface interactive en JavaScript
- Comparer des données et renvoyer des résultats colorés
- Orchestrer une app avec Docker Compose
- Mettre en place un pipeline CI/CD avec GitHub Actions
