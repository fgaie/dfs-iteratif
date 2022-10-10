from sys import argv
from algorithme import dfs, Sommet, Graphe

def lire_sommet(ligne: str) -> tuple[Sommet, list[Sommet]]:
    tokens = ligne.split(" ")
    tokens = list(map(int, filter((lambda x: x != " "), tokens)))

    if len(tokens) < 1:
        exit(1)

    return Sommet(tokens[0]), list(map(Sommet, tokens[1:]))

def lire_graphe(fichier: str) -> Graphe:
    G: Graphe = {}
    with open(fichier, encoding='utf-8') as f:
        for ligne in f:
            l = ligne.strip()
            if l: # On ignore les lignes vides
                k, v = lire_sommet(ligne)
                G[k] = v

    return G

def main(argv: list[str]):
    if len(argv) == 1:
        print("\n".join(['utilisation:',
                         '\tpython3 {argv[0]} [fichier1] [fichier2] ...']))
        exit(0)

    for arg in argv[1:]:
        G = lire_graphe(arg)

        print("\n".join(map(str, dfs(G))))

if __name__ == '__main__':
    main(argv)
