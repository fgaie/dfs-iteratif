"""L'algorithme principal"""

from dataclasses import dataclass

@dataclass(frozen=True)
class Sommet:
    name: int

    def __str__(self) -> str:
        return str(self.name)

# On represente un graphe avec une list d'adjacence (ex: 1 -> 2 => {1: [2], 2: []})
Graphe = dict[Sommet, list[Sommet]]

@dataclass
class _Counter:
    cur: int
    def next(self):
        tmp = self.cur
        self.cur += 1
        return tmp

def _explorer(
        G: Graphe,
        u: Sommet,
        marque: dict[Sommet, bool],
) -> list[Sommet]:
    result: list[Sommet] = []
    pile: list[Sommet] = [u]

    while pile: # not empty
        u = pile.pop()

        if not marque[u]:
            marque[u] = True
            pile.append(u)
            result.append(u)

        for v in sorted(G[u], key=lambda s: s.name, reverse=True):
            if not marque[v]:
                pile.append(v)

    return result

def dfs(G: Graphe) -> list[Sommet]:
    marque: dict[Sommet, bool] = {k: False for k in G.keys()}
    resultat: list[Sommet] = []

    for u in G.keys():
        if not marque[u]:
            resultat += _explorer(G, u, marque)

    return resultat
