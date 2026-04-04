## *This project has been created as part of the 42 curriculum by nilinott, jbenhass*

---

## 📌 Description

**A-Maze-ing** est un projet centré sur la génération et la résolution de labyrinthes.

Le programme prend en entrée un fichier de configuration permettant de définir :
- la taille du labyrinthe (largeur et hauteur),
- la position de l’entrée et de la sortie,
- le nom du fichier de sortie (généré en hexadécimal),
- ainsi que le type de labyrinthe (parfait ou non).

À partir de ces paramètres, le programme génère un labyrinthe de manière aléatoire, puis peut le résoudre en trouvant un chemin entre l’entrée et la sortie.

Ce projet permet de travailler :
- la génération procédurale,
- les structures de données en 2D,
- les algorithmes de parcours (pathfinding),
- la gestion de configuration et le parsing.

## ⚙️ Instructions

### Compilation
``` bash
make
```

### Execution

``` bash
python3 a_maze_ing.py <fichier de configuration>
```

## 🧩  Structure du fichier de configuration

``` bash
WIDTH=15
HEIGHT=20
OUTPUT_FILE=maze.txt
ENTRY=0,5
EXIT=0,4
PERFECT=True
```

### Détails des paramètres

 - **width** / **height** : dimensions du labyrinthe
 - **start** : position de depart (x, y)
 - **end** : position de sort (x, y)
 - **output** : nom du fichier de sortie (format hexadecimal)
 - **perfect** :
    - **true** -> Labyrinthe parfait (un seul chemin possible)
    - **false** -> Labyrinthe avec plusieurs chemins possibles

## 🧠 Algorithme de génération

Le labyrinthe est généré de manière aléatoire en utilisant DFS.

Fonctionnement :
- On initialise une grille remplie de murs
- On choisit une cellule de départ
- On visite aléatoirement un voisin non exploré
- On casse le mur entre les deux cellules
- On continue jusqu’à blocage
- On revient en arrière (backtracking) pour explorer d’autres chemins

## ❓ Pourquoi cet algorithme

- Génère facilement des labyrinthes aléatoires
- Permet de créer des labyrinthes parfaits
- Simple à implémenter
- Bon compromis entre performance et complexité

## 🧠 Algorithme de résolution
➤ Breadth-First Search (BFS)

Le solver utilise BFS pour trouver le plus court chemin entre l’entrée et la sortie.

Étapes :
- Exploration des cases voisines
- Marquage des cases visitées
- Arrêt à la découverte de la sortie
- Reconstruction du chemin













