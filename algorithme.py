"""L'algorithme principal"""

from dataclasses import dataclass
from typing import Union

@dataclass(frozen=True)
class Sommet:
    name: Union[int, str]

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
        prepost_ctr: _Counter,
        prepost: dict[Sommet, tuple[int, int]]
) -> list[Sommet]:
    pre: dict[Sommet, int] = {}
    result: list[Sommet] = []
    pile: list[Sommet] = [u]

    while pile: # not empty
        u = pile.pop()

        if marque[u] and u not in prepost:
            prepost[u] = pre[u], prepost_ctr.next()
            continue

        elif marque[u]:
            continue

        pre[u] = prepost_ctr.next()
        marque[u] = True
        pile.append(u)
        result.append(u)

        for v in sorted(G[u], key=lambda s: s.name, reverse=True):
            if not marque[v]:
                pile.append(v)

    return result

def dfs(G: Graphe) -> tuple[list[Sommet], dict[Sommet, tuple[int, int]]]:
    marque: dict[Sommet, bool] = {k: False for k in G.keys()}
    resultat: list[Sommet] = []
    prepost_ctr: _Counter = _Counter(1)
    prepost: dict[Sommet, tuple[int, int]] = {}

    for u in G.keys():
        if not marque[u]:
            resultat += _explorer(G, u, marque, prepost_ctr, prepost)

    return resultat, prepost
