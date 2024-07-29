# Cinepédia

Cinepédia est un petit projet amusant, une sorte de mini wikipédia pour vous renseigner sur des films qui vous  interessent grâce à l'API __[ImDb](https://developer.imdb.com/)__ qui repertorie des milliers de films existant dans le monde.

# Installation

Pour installer (utiliser) Cinepédia en local, commencer par installer une version de l'interpreteur python 3.x, pour ma part ce code à été écrit sous python 3.11. Ensuite télécharger ce répértoire sur votre machine locale et executer les quelques instructions suivantes pour pouvoir utilisez le projet :

## Environnement virtuel

Pour pouvoir isoler ce projet de tous les autres (ce qui en passant est une chose que vous devriez faire pour tous vos projets python), nous allons créer un environnement virtuel avec l'outil `venv` suivant le système que vous utilisez.

```bash 
// Sur Linux
cd cinepedia-app
python3.x -m venv venv

// Sur Windows
cd cinepedia-app
python -m venv venv
```

Ensuite il va falloir activez cet environnement virtuel et y installez toutes les dépendances de notre projet

```bas
// Sur Linux
source venv/bin/activate
python -m pip install -r requirements.txt

// Sur Windows
cd venv/Scripts
activate
cd ..
python -m pip install -r requirements.txt
```

Votre environnement virtuel crée et prêt à l'emploi il ne vous reste plus qu'à lancer le programme avec une instruction `python main.py`



https://github.com/user-attachments/assets/68c54d2d-4705-4301-aaff-f0f5882d466b

