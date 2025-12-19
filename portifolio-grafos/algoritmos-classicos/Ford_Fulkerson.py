from collections import defaultdict
import networkx as nx

def ler_arq():
    arcos = []
    max_v = -1
    try:
        with open("arq.txt", "r") as arq:
            for linha in arq:
                if linha.strip():
                    u, v, c = map(int, linha.split())
                    arcos.append((u, v, c))
                    max_v = max(max_v, u, v)
        return arcos, max_v + 1
    except FileNotFoundError:
        print("Erro: 'arq.txt' não encontrado.")
        return [], 0
    except ValueError:
        print("Erro: Dados em 'arq.txt' inválidos.")
        return [], 0


class Grafo:
    def __init__(self, v):
        self.V = v
        self.g = defaultdict(dict)

    def add_arco(self, u, v, cap):
        self.g[u][v] = cap

    def bfs(self, s, t, pai):
        vis = [False] * self.V
        fila = [s]
        vis[s] = True
        
        while fila:
            u = fila.pop(0)
            
            for v, cap in self.g[u].items():
                if not vis[v] and cap > 0:
                    fila.append(v)
                    vis[v] = True
                    pai[v] = u
                    if v == t:
                        return True
        
        return vis[t]

    def ford_fulkerson(self, s, t):
        pai = [-1] * self.V
        fmax = 0

        while self.bfs(s, t, pai):
            cf = float("inf")
            v = t
            while v != s:
                u = pai[v]
                cf = min(cf, self.g[u][v])
                v = pai[v]
            
            v = t
            while v != s:
                u = pai[v]
                self.g[u][v] -= cf
                self.g[v][u] = self.g[v].get(u, 0) + cf
                v = pai[v]
            
            fmax += cf
            
        return fmax

def fluxo_networkx(arcos, s, t):
    G = nx.DiGraph()
    for u, v, c in arcos:
        G.add_edge(u, v, capacity=c)
    
    try:
        fmax, f_arcos = nx.maximum_flow(G, s, t)
        
        print("\n--- Resultado NetworkX ---")
        print("Fluxo Máximo:", fmax)
        print("Fluxo por Aresta:")
        
        for u in f_arcos:
            for v, f in f_arcos[u].items():
                if f > 0:
                    print(f"  {u} -> {v}: {f}")
        print("--------------------------")
        
    except nx.NetworkXNoPath:
        print("\nSem caminho. Fluxo Máximo = 0.")
    except nx.NetworkXUnfeasible:
         print("\nErro: Capacidade inválida.")


if __name__ == "__main__":
    arcos, n_v = ler_arq()
    
    if n_v == 0:
        exit()

    try:
        s = int(input("Origem (source): "))
        t = int(input("Destino (sink): "))

        if not (0 <= s < n_v and 0 <= t < n_v):
             print(f"Erro: Vértices devem ser entre 0 e {n_v-1}.")
             exit()

    except ValueError:
        print("Erro: Use apenas números inteiros.")
        exit()

    print("\nEscolha o método:")
    print("1 - Ford-Fulkerson")
    print("2 - NetworkX")
    op = input("Opção: ")

    if op == "1":
        g = Grafo(n_v)
        for u, v, c in arcos:
            g.add_arco(u, v, c)
            
        print("\n--- Resultado Ford-Fulkerson ---")
        fmax = g.ford_fulkerson(s, t)
        print("Fluxo Máximo:", fmax)
        print("--------------------------------")

    elif op == "2":
        fluxo_networkx(arcos, s, t)

    else:
        print("Opção inválida.")