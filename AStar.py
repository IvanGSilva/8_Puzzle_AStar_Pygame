from queue import PriorityQueue

# recebe o tabuleiro inicial, o estado desejado, e a heurística a ser usada
def a_star(start_state, goal_state, heuristic):
    # organiza os estados com base no custo estimado (f_score)
    open_set = PriorityQueue()
    # adiciona o estado inicial à fila de prioridades com f_score inicial de 0
    open_set.put((0, start_state, [])) 
    # conjunto para rastrear os estados já visitados, evitando loops
    visited = set()
    visited_count = 0
    
    while not open_set.empty():
        # remove o estado com menor custo da fila
        _, current_state, path = open_set.get()
        
        visited_count += 1
        
        # se o estado atual for o estado objetivo, retorna o caminho até ele
        if current_state == goal_state:
            return path, visited_count
        
        # marca o estado atual como visitado
        visited.add(tuple(current_state))
        
        # acha a posição do espaço vazio (0) no tabuleiro
        # pega os estados vizinhos possíveis (movimentos válidos do espaço vazio)
        zero_index = current_state.index(0)
        neighbors = get_neighbors(current_state, zero_index)
        
        for neighbor in neighbors:
            # garante que o estado vizinho ainda não foi visitado
            if tuple(neighbor) not in visited:
                # atualiza o caminho ao adicionar o estado vizinho
                new_path = path + [neighbor]
                # calcula o custo g
                g_score = len(new_path)
                
                # verifica se a heuristica recebe um argumento (inversão de pares)
                if heuristic.__code__.co_argcount == 1:
                    h_score = heuristic(neighbor)
                else:
                    h_score = heuristic(neighbor, goal_state)
                
                # calcula o custo total f = g + h
                f_score = g_score + h_score
                # adiciona o estado vizinho na fila com o custo e o caminho atualizado
                open_set.put((f_score, neighbor, new_path))
    
    # se a fila não tiver solução, retorna vazio
    return [], visited_count


# função para saber os movimentos válidos 
def get_neighbors(state, zero_index):
    neighbors = []
    row, col = divmod(zero_index, 3)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero_index = new_row * 3 + new_col
            new_state = state[:]
            new_state[zero_index], new_state[new_zero_index] = new_state[new_zero_index], new_state[zero_index]
            neighbors.append(new_state)
    
    # retorna todos os estados vizinhos possíveis
    return neighbors
