"""Point d'entree du programme"""

from sys import argv
from algorithme import dfs, Sommet, Graphe

def lire_sommet(ligne: str, nom_literal: bool) -> tuple[Sommet, list[Sommet]]:
    tokens = list(filter((lambda x: x != ' '), ligne.split(' ')))
    if not nom_literal:
        tokens = list(map(int, tokens))

    if len(tokens) < 1:
        exit(1)

    return Sommet(tokens[0]), list(map(Sommet, tokens[1:]))

def lire_graphe(fichier: str, nom_literal: bool = False) -> Graphe:
    G: Graphe = {}
    with open(fichier, encoding='utf-8') as f:
        for ligne in f:
            l = ligne.strip()
            if l: # On ignore les lignes vides
                k, v = lire_sommet(ligne, nom_literal)
                G[k] = v

    return G

def main(argv: list[str]):

    if len(argv) == 1:
        print("\n".join(['utilisation:',
                         '\tpython3 {argv[0]} [fichier1] [fichier2] ...']))
        exit(0)

    for i, fichier in enumerate(argv[1:]):
        titre = f'{i}) {fichier}'
        print(f'{titre}\n{"="*len(titre)}\n')
        G = lire_graphe(fichier)

        ordre, prepost = dfs(G)
        for u in ordre:
            pre, post = prepost[u]
            print(f'{u} [{pre}/{post}]')
        print()
            
if __name__ == '__main__':
    main(argv)
