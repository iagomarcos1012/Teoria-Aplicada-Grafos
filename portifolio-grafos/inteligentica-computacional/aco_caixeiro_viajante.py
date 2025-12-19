import networkx as nx
import random
import math

class AntColonyOptimization:
    def __init__(self, graph, num_ants, alpha=1, beta=5, rho=0.5, Q=100, max_iterations=100, initial_pheromone=1e-6):
        self.graph = graph
        self.num_ants = num_ants
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.Q = Q
        self.max_iterations = max_iterations
        self.initial_pheromone = initial_pheromone
        
        for u, v in self.graph.edges():
            self.graph[u][v]['pheromone'] = self.initial_pheromone

    def _heuristic(self, u, v):
        distance = self.graph[u][v]['weight']
        if distance == 0:
            return 1e10
        return 1.0 / distance

    def _select_next_node(self, current_node, visited):
        probabilities = []
        possible_nodes = []
        denominator = 0.0
        
        neighbors = list(self.graph.neighbors(current_node))
        unvisited_neighbors = [n for n in neighbors if n not in visited]

        if not unvisited_neighbors:
            return None

        for neighbor in unvisited_neighbors:
            pheromone = self.graph[current_node][neighbor]['pheromone']
            dist_heuristic = self._heuristic(current_node, neighbor)
            
            prob_value = (pheromone ** self.alpha) * (dist_heuristic ** self.beta)
            
            probabilities.append(prob_value)
            possible_nodes.append(neighbor)
            denominator += prob_value

        if denominator == 0:
            probabilities = [1.0 / len(possible_nodes)] * len(possible_nodes)
        else:
            probabilities = [p / denominator for p in probabilities]

        next_node = random.choices(possible_nodes, weights=probabilities, k=1)[0]
        return next_node

    def _construct_solution(self, ant_id):
        nodes = list(self.graph.nodes())
        start_node = random.choice(nodes)
        
        path = [start_node]
        visited = set(path)
        total_distance = 0.0
        
        current_node = start_node
        
        while len(visited) < len(nodes):
            next_node = self._select_next_node(current_node, visited)
            if next_node is None:
                break
            
            total_distance += self.graph[current_node][next_node]['weight']
            
            path.append(next_node)
            visited.add(next_node)
            current_node = next_node
            
        total_distance += self.graph[path[-1]][path[0]]['weight']
        path.append(path[0])
        
        return path, total_distance

    def _update_pheromones(self, all_solutions):
        for u, v in self.graph.edges():
            self.graph[u][v]['pheromone'] *= (1 - self.rho)
            if self.graph[u][v]['pheromone'] < 1e-10:
                self.graph[u][v]['pheromone'] = 1e-10

        for path, distance in all_solutions:
            delta_tau = self.Q / distance
            
            for i in range(len(path) - 1):
                u, v = path[i], path[i+1]
                if self.graph.has_edge(u, v):
                    self.graph[u][v]['pheromone'] += delta_tau

    def run(self):
        best_global_path = None
        best_global_distance = float('inf')
        
        print(f"Iniciando ACO com {self.max_iterations} iterações e {self.num_ants} formigas...")
        print("-" * 50)

        for iteration in range(self.max_iterations):
            all_solutions = []
            
            for k in range(self.num_ants):
                path, distance = self._construct_solution(k)
                all_solutions.append((path, distance))
                
                if distance < best_global_distance:
                    best_global_distance = distance
                    best_global_path = path
            
            self._update_pheromones(all_solutions)
            
            if (iteration + 1) % 10 == 0:
                 print(f"Iteração {iteration + 1}: Melhor Distância = {best_global_distance:.4f}")

        return best_global_path, best_global_distance

def create_random_graph(num_nodes=15):
    G = nx.Graph()
    nodes = range(num_nodes)
    G.add_nodes_from(nodes)
    
    import itertools
    for u, v in itertools.combinations(nodes, 2):
        weight = random.randint(10, 100)
        G.add_edge(u, v, weight=weight)
        
    return G

if __name__ == "__main__":
    NUM_CIDADES = 20
    G = create_random_graph(NUM_CIDADES)
    
    m = NUM_CIDADES 
    alpha = 1.0
    beta = 5.0
    rho = 0.5
    Q = 100.0
    max_iter = 50
    
    aco = AntColonyOptimization(G, num_ants=m, alpha=alpha, beta=beta, rho=rho, Q=Q, max_iterations=max_iter)
    best_path, best_dist = aco.run()
    
    print("-" * 50)
    print(f"Melhor Caminho Encontrado: {best_path}")
    print(f"Melhor Distância: {best_dist}")