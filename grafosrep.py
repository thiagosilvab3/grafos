class Grafo:
    def __init__(self, num_vertices, direcionado=False, ponderado=False):
        """
        Inicializa o grafo com as representações de matriz e lista de adjacência
        
        Args:
            num_vertices: Número de vértices do grafo
            direcionado: Booleano indicando se o grafo é direcionado (padrão: False)
            ponderado: Booleano indicando se o grafo é ponderado (padrão: False)
        """
        self.num_vertices = num_vertices
        self.direcionado = direcionado
        self.ponderado = ponderado
        
        # Matriz de adjacência (armazena 0/1 ou pesos)
        self.matriz_adj = [[0] * num_vertices for _ in range(num_vertices)]
        
        # Lista de adjacência (armazena pares (vértice, peso) se ponderado)
        self.lista_adj = [[] for _ in range(num_vertices)]

    def adicionar_aresta(self, u, v, peso=1):
        """
        Adiciona uma aresta entre os vértices u e v
        
        Args:
            u: Vértice de origem (0 a num_vertices-1)
            v: Vértice de destino (0 a num_vertices-1)
            peso: Peso da aresta (ignorado se grafo não ponderado)
        """
        if u >= self.num_vertices or v >= self.num_vertices:
            raise ValueError("Vértice inválido")
            
        if not self.ponderado:
            peso = 1  # Ignora peso se grafo não for ponderado
            
        # Atualiza matriz de adjacência
        self.matriz_adj[u][v] = peso
        if not self.direcionado and u != v:
            self.matriz_adj[v][u] = peso
        
        # Atualiza lista de adjacência
        self.lista_adj[u].append((v, peso))
        if not self.direcionado and u != v:
            self.lista_adj[v].append((u, peso))

    def remover_aresta(self, u, v):
        """
        Remove a aresta entre os vértices u e v
        """
        # Remove da matriz
        self.matriz_adj[u][v] = 0
        if not self.direcionado:
            self.matriz_adj[v][u] = 0
        
        # Remove da lista
        self.lista_adj[u] = [(vert, p) for vert, p in self.lista_adj[u] if vert != v]
        if not self.direcionado:
            self.lista_adj[v] = [(vert, p) for vert, p in self.lista_adj[v] if vert != u]

    def tem_aresta(self, u, v):
        """
        Verifica se existe aresta de u para v
        
        Returns:
            bool: True se existe aresta, False caso contrário
        """
        return self.matriz_adj[u][v] != 0

    def vizinhos(self, v):
        """
        Retorna os vizinhos do vértice v
        
        Returns:
            list: Lista de vértices vizinhos
        """
        return [vert for vert, _ in self.lista_adj[v]]

    def grau(self, v):
        """
        Calcula o grau do vértice v
        
        Returns:
            int: Grau do vértice
        """
        return len(self.lista_adj[v]) if self.direcionado else len(self.vizinhos(v))

    def mostrar_matriz(self):
        """Exibe a matriz de adjacência formatada"""
        print("🔹 Matriz de Adjacência:")
        print("   " + " ".join([str(i) for i in range(self.num_vertices)]))
        for i in range(self.num_vertices):
            print(f"{i}: {self.matriz_adj[i]}")

    def mostrar_lista(self):
        """Exibe a lista de adjacência formatada"""
        print("🔹 Lista de Adjacência:")
        for i in range(self.num_vertices):
            conexoes = []
            for vert, peso in self.lista_adj[i]:
                if self.ponderado:
                    conexoes.append(f"{vert}({peso})")
                else:
                    conexoes.append(str(vert))
            print(f"{i}: {conexoes}")

    def __str__(self):
        """Representação textual do grafo"""
        return f"Grafo({self.num_vertices} vértices, {'direcionado' if self.direcionado else 'não-direcionado'}, {'ponderado' if self.ponderado else 'não-ponderado'})"


# Exemplo de uso
if __name__ == "__main__":
    print("=== Grafo Não Direcionado e Não Ponderado ===")
    grafo1 = Grafo(5)
    grafo1.adicionar_aresta(0, 1)
    grafo1.adicionar_aresta(0, 2)
    grafo1.adicionar_aresta(1, 3)
    grafo1.adicionar_aresta(3, 4)
    
    grafo1.mostrar_matriz()
    print()
    grafo1.mostrar_lista()
    
    print("\n=== Grafo Direcionado e Ponderado ===")
    grafo2 = Grafo(4, direcionado=True, ponderado=True)
    grafo2.adicionar_aresta(0, 1, 5)
    grafo2.adicionar_aresta(0, 2, 3)
    grafo2.adicionar_aresta(1, 3, 2)
    grafo2.adicionar_aresta(2, 3, 7)
    
    grafo2.mostrar_matriz()
    print()
    grafo2.mostrar_lista()
    
    # Testando remoção de aresta
    print("\nRemovendo aresta 0 -> 2")
    grafo1.remover_aresta(0, 2)
    grafo1.mostrar_lista()
    
    # Testando métodos auxiliares
    print("\nTestando métodos auxiliares:")
    print(f"Vizinhos do vértice 1: {grafo1.vizinhos(1)}")
    print(f"Grau do vértice 1: {grafo1.grau(1)}")
    print(f"Existe aresta entre 1 e 3? {grafo1.tem_aresta(1, 3)}")