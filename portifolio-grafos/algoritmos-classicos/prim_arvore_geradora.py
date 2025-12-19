import networkx as nx

def ler(arq):
    G = nx.Graph()
    with open(arq, "r") as f:
        for l in f:
            if l.strip():
                try:
                    u, v, w = l.split()
                    G.add_edge(int(u), int(v), weight=float(w))
                except ValueError:
                    pass 
    return G

def arvore_geradora_minima_prim(G):
    agm_arestas = list(nx.minimum_spanning_edges(G, algorithm="prim", data=True))
    
    AGM = nx.Graph()
    AGM.add_edges_from(agm_arestas)
    
    return agm_arestas, AGM

print("== Algoritmo de Prim (Árvore Geradora Mínima) ==")

arq = "arq.txt" 
try:
    G = ler(arq)
except FileNotFoundError:
    print(f"\nERRO: O arquivo '{arq}' não foi encontrado.")
    exit()

if not G.edges():
    print("\nERRO: O grafo não contém arestas.")
    exit()

print(f"\nGrafo Original (Lido de '{arq}'):")
peso_total_original = 0
for u, v, d in G.edges(data=True):
    peso = d['weight']
    peso_total_original += peso
    print(f"Aresta: {u} -- {v} (peso = {peso})")

try:
    c, AGM = arvore_geradora_minima_prim(G) 
except nx.NetworkXNoCycle:
    print("\nERRO: O grafo não está conectado.")
    exit()

print("\n" + "="*40)
print("Árvore Geradora Mínima (Algoritmo de Prim):")
print("="*40)

peso_total_agm = 0
for u, v, d in c:
    peso = d['weight']
    peso_total_agm += peso
    print(f"Aresta AGM: {u} -- {v} (peso = {peso})")

print(f"\nPeso total da Árvore Geradora Mínima (Mínimo): {peso_total_agm}")