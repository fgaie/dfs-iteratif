"""L'algorithme principal"""

from dataclasses import dataclass

# On represente un graphe avec une list d'adjacence (ex: 1 -> 2 => [[2], []])
Sommet = int
Graphe = list[list[Sommet]]

@dataclass
class Counter:
    cur: int
    def __call__(self):
        self.cur += 1
        return self.cur

def explorer(
        G: Graphe,
        u: Sommet,
        marque: list[bool],
) -> list[Sommet]:
    result: list[Sommet] = []
    pile: list[Sommet] = [u]
    
    while pile: # not empty
        u = pile.pop()
        
        if not marque[u]:
            marque[u] = True
            result.append(u)
            pile.append(u)

        for v in sorted(G[u], reverse = True):
            if not marque[v]:
                pile.append(v)
        
    return result
            
def dfs(G: Graphe) -> list[Sommet]:
    marque = [False] * len(G)
    result: [Sommet] = []

    for u in range(len(G)):
        if not marque[u]:
            result += explorer(G, u, marque)

    return result

def main():
    
    G = [[4, 5], [1, 4, 6, 7], [3],    [2],
         [8, 9], [10],         [],     [3],
         [9],    [10],         [6, 8], [6, 7, 10]]

    result = dfs(G)
    intended_result = [0, 4, 8, 9, 10, 6, 5, 1, 7, 3, 2, 11]
    print(f'{result = }\n{result == intended_result = }')

if __name__ == '__main__':
    main()
