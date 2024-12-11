# calcula quanto cada peça numerada está distante de sua posição correta no estado
def manhattan_distance(state, goal_state):
    distance = 0
    for i in range(1, 9):  # Peças numeradas de 1 a 8
        x1, y1 = divmod(state.index(i), 3)
        x2, y2 = divmod(goal_state.index(i), 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    print("Manhattan Distance for ")
    return distance

# conta quantas peças numeradas estão fora de suas posições corretas
def inversion_pairs(state):
    inversions = 0
    flat_state = [tile for tile in state if tile != 0]
    for i in range(len(flat_state)):
        for j in range(i + 1, len(flat_state)):
            if flat_state[i] > flat_state[j]:
                inversions += 1
    print("Inversion Pairs")
    return inversions

# avalia quantas inversões existem no tabuleiro
def misplaced_tiles(state, goal_state):
    print("misplaced_tiles")
    return sum(1 for i in range(len(state)) if state[i] != 0 and state[i] != goal_state[i])
