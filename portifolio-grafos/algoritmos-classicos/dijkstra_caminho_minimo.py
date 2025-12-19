import networkx as nx
import heapq

G = nx.DiGraph()
arestas = []

try:
    with open("atv.txt", "r") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            dados = linha.split()
            if len(dados) == 3:
                u, v, w = int(dados[0]), int(dados[1]), float(dados[2])
                G.add_edge(u, v, weight=w)
                arestas.append((u, v, w))
except FileNotFoundError:
    print("Arquivo 'atv.txt' não encontrado.")
    exit()

print("Arestas do grafo (origem -> destino, peso):")
for u, v, w in arestas:
    print(f"{u} -> {v}, peso = {w}")


def dijkstra(grafo, inicio):
    dist = {n: float('inf') for n in grafo.nodes()}
    prev = {n: None for n in grafo.nodes()}
    dist[inicio] = 0
    fila = [(0, inicio)]

    while fila:
        d, n = heapq.heappop(fila)
        if d > dist[n]:
            continue
        for viz, dados in grafo[n].items():
            peso = dados['weight']
            nova = dist[n] + peso
            if nova < dist[viz]:
                dist[viz] = nova
                prev[viz] = n
                heapq.heappush(fila, (nova, viz))

    caminhos = {}
    for n in grafo.nodes():
        if dist[n] < float('inf'):
            rota = []
            passo = n
            while passo is not None:
                rota.append(passo)
                passo = prev[passo]
            caminhos[n] = rota[::-1]
        else:
            caminhos[n] = []
    return dist, caminhos

try:
    inicio = int(input("\nDigite o vértice de origem: "))
    if inicio not in G:
        print(f"Erro: vértice {inicio} não existe.")
        exit()
except ValueError:
    print("Erro: digite um número inteiro válido.")
    exit()

distancias, caminhos = dijkstra(G, inicio)

print(f"\nDistâncias mínimas a partir do vértice {inicio}:")
for n, d in sorted(distancias.items()):
    if d == float('inf'):
        print(f"→ Até {n}: imposivel de se alcançar")
    else:
        print(f"→ Até {n}: distância = {d}")

print(f"\nCaminhos mínimos a partir do vértice {inicio}:")
for n, rota in sorted(caminhos.items()):
    if rota:
        print(f"→ Até {n}: caminho = {' -> '.join(map(str, rota))}")
