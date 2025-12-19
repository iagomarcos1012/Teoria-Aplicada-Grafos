import networkx as nx
import sys



def ler_grafo(arq):
    try:
        G = nx.read_gml(arq)
        print(f"Grafo carregado: {len(G.nodes())} vértices e {len(G.edges())} arestas.\n")
        return G
    except Exception as e:
        print("Erro ao ler arquivo GML:", e)
        sys.exit(1)


def limpar_nome(nome):
    """Converte o nome para string, mesmo se for lista ou None."""
    if nome is None:
        return "Sem nome"
    if isinstance(nome, list):
        return ", ".join([str(x) for x in nome])
    return str(nome)


def obter_ruas(G):
    ruas = {}
    for u, v, data in G.edges(data=True):
        nome = limpar_nome(data.get("name"))
        ruas[(u, v)] = nome
        ruas[(v, u)] = nome
    return ruas


def maior_grau(G, arestas_restantes):
    """
    Retorna o vértice que cobre o maior número de arestas 
    que AINDA estão no conjunto arestas_restantes.
    """
    melhor = None
    melhor_qtd = -1

    for v in G.nodes():
        qtd = 0
        for viz in G.neighbors(v):
            
            aresta = tuple(sorted((v, viz)))
            if aresta in arestas_restantes:
                qtd += 1
        
        if qtd > melhor_qtd:
            melhor_qtd = qtd
            melhor = v

    return melhor


def cobertura_gulosa(G):
    
    arestas_restantes = set()
    for u, v in G.edges():
        arestas_restantes.add(tuple(sorted((u, v))))

    cameras = []

   
    while arestas_restantes:
        v = maior_grau(G, arestas_restantes)
        
       
        if v is None:
            break

        cameras.append(v)

    
        for viz in G.neighbors(v):
            aresta = tuple(sorted((v, viz)))
            if aresta in arestas_restantes:
                arestas_restantes.remove(aresta)

    return cameras


def listar_ruas_camera(G, ruas_dict, camera):
    nomes = set()
    for viz in G.neighbors(camera):
        
        nome = ruas_dict.get((camera, viz))
      
        if nome is None:
            nome = ruas_dict.get((viz, camera), "Rua Desconhecida")
        
        nomes.add(limpar_nome(nome))
    return list(nomes)


def main():
    if len(sys.argv) < 2:
        print("Uso: python3 sistema_monitoramento_cameras.py mapa_sjdr.gml")
        return

    arq = sys.argv[1]
    G = ler_grafo(arq)
    ruas_dict = obter_ruas(G)

    print("Calculando cobertura mínima aproximada...\n")
    cameras = cobertura_gulosa(G)

    print("========== RESULTADO ==========\n")
    print(f"Total de câmeras instaladas: {len(cameras)}\n")

    
    for c in sorted(cameras): 
        ruas = listar_ruas_camera(G, ruas_dict, c)
        print(f"Câmera na esquina {c}:")
        for rua in sorted(ruas): 
            print(f"  - {rua}") 
        print()

    print("================================\n")


if __name__ == "__main__":
    main()