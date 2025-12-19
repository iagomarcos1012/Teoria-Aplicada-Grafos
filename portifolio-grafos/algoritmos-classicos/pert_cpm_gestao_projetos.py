import networkx as nx

def ler(arq):
    G = nx.DiGraph()
    with open(arq, "r") as f:
        for l in f:
            if l.strip():
                u, v, w = l.split()
                G.add_edge(int(u), int(v), weight=float(w))
    return G

def ordem(G):
    g = {v: 0 for v in G.nodes()}
    for u, v in G.edges():
        g[v] += 1
    f = [v for v in G.nodes() if g[v] == 0]
    o = []
    while f:
        a = f.pop(0)
        o.append(a)
        for viz in G.successors(a):
            g[viz] -= 1
            if g[viz] == 0:
                f.append(viz)
    if len(o) != len(G.nodes()):
        print("Erro: o grafo contém ciclos.")
        exit()
    return o

def cedo(G, o):
    t = {v: 0 for v in G.nodes()}
    for u in o:
        for v in G.successors(u):
            d = G[u][v]['weight']
            t[v] = max(t[v], t[u] + d)
    return t

def tarde(G, o, t):
    fim = max(t.values())
    tt = {v: fim for v in G.nodes()}
    for u in reversed(o):
        for v in G.successors(u):
            d = G[u][v]['weight']
            tt[u] = min(tt[u], tt[v] - d)
    return tt, fim

def caminho(G, tc, tt):
    f = {}
    c = []
    for u, v in G.edges():
        d = G[u][v]['weight']
        fg = (tt[v] - d) - tc[u]
        f[(u, v)] = fg
        if fg == 0:
            c.append((u, v))
    return f, c

print("== Caminho Crítico ==")
arq = "atv.txt"
G = ler(arq)

print("\nArestas:")
for u, v, w in G.edges(data="weight"):
    print(f"{u} -> {v} (duração = {w})")

o = ordem(G)
tc = cedo(G, o)
tt, fim = tarde(G, o, tc)
f, c = caminho(G, tc, tt)

print("\nOrdem:", o)
print("\nCedo:")
for v in o:
    print(f"{v}: {tc[v]}")

print("\nTarde:")
for v in o:
    print(f"{v}: {tt[v]}")

print("\nFolgas:")
for (u, v), fg in f.items():
    print(f"{u} -> {v}: {fg}")

print("\nCaminho crítico:")
for u, v in c:
    print(f"{u} -> {v}")

print(f"\nDuração total: {fim}")
