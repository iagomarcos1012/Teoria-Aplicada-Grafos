# 🔍 Applied Graph Theory & Urban Optimization

Este repositório reúne implementações avançadas de **Teoria dos Grafos** e **Inteligência Computacional** desenvolvidas durante a graduação em Ciência da Computação na Universidade Federal de São João del-Rei (UFSJ).

O foco principal é a aplicação de algoritmos clássicos e heurísticas para resolver problemas reais de otimização, logística e planejamento urbano.

---

## 🚀 Destaque: Otimização de Monitoramento Urbano (SJDR)

Este projeto utiliza a estrutura viária real da cidade de **São João del-Rei (MG)** para solucionar um problema de **Cobertura de Vértices** (Vertex Cover/Dominating Set) aplicado à segurança pública.

### 🎯 O Desafio
Determinar os pontos estratégicos ideais para instalação de câmeras de segurança, visando cobrir o maior número de ruas possível com o menor custo (menor número de câmeras).

### 🛠️ A Solução
* **Dados Reais:** Extração e modelagem da malha urbana a partir de arquivos `.gml`.
* **Algoritmo Guloso (Greedy):** Implementação de uma heurística de seleção baseada no grau dos vértices (esquinas) para maximizar a cobertura visual.
* **Visualização:** O sistema gera um relatório detalhado de quais ruas são monitoradas por cada câmera.

📂 **Localização:** [`Otimizacao-Urbana-SJDR/`](./Otimizacao-Urbana-SJDR)

---

## 📚 Algoritmos Implementados

O repositório está organizado em módulos temáticos:

### 1. Algoritmos Clássicos de Grafos
Implementações fundamentais para análise de redes e rotas.
* **Dijkstra:** Cálculo de caminho mínimo (Shortest Path).
* **Ford-Fulkerson:** Determinação de fluxo máximo em redes de transporte/dados.
* **Prim:** Árvore Geradora Mínima (MST) para otimização de cabeamento/conexões.
* **PERT/CPM:** Gestão de projetos, identificando caminhos críticos e folgas em cronogramas.

📂 **Localização:** [`Algoritmos-Classicos/`](./Algoritmos-Classicos)

### 2. Inteligência Computacional
* **Ant Colony Optimization (ACO):** Aplicação de meta-heurística baseada em colônia de formigas para resolver o **Problema do Caixeiro Viajante (TSP)**.

📂 **Localização:** [`Inteligencia-Computacional/`](./Inteligencia-Computacional)

---

## 💻 Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Bibliotecas:**
    * `NetworkX`: Manipulação e análise de grafos complexos.
    * `Matplotlib`: Visualização de dados (quando aplicável).
    * `Itertools/Collections`: Otimização de estruturas de dados.

---

## ⚙️ Como Executar

### Pré-requisitos
Certifique-se de ter o Python instalado e as dependências necessárias:

```bash
pip install -r requirements.txt
