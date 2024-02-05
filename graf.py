import heapq


def read_board(file_name):
    with open(file_name, 'r') as file:
        board = [list(line.strip()) for line in file]
    return board


def find_xs(board):
    xs = []
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == 'X':
                xs.append((i, j))
                if len(xs) == 2:
                    return xs
    return xs


def get_neighbors(position, board):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # right, down, up, left
    neighbors = []
    for dx, dy in directions:
        x, y = position[0] + dx, position[1] + dy
        if 0 <= x < len(board) and 0 <= y < len(board[0]):
            neighbors.append((x, y))
    return neighbors


def dijkstra(board, start, end):
    visited = set()
    queue = [(0, start)]  # (cost, position)
    paths = {start: None}

    while queue:
        cost, position = heapq.heappop(queue)
        if position in visited:
            continue
        visited.add(position)

        if position == end:
            return cost, paths

        for neighbor in get_neighbors(position, board):
            if neighbor not in visited:
                if board[position[0]][position[1]] == 'J':
                    # Koszt wyjścia z pola 'J' wynosi 0
                    next_cost = 0
                else:
                    # Koszt wejścia na pole 'J' lub 'X' wynosi 0, w przeciwnym przypadku jest to cyfra
                    next_cost = 0 if board[neighbor[0]][neighbor[1]] in ['J', 'X'] else int(board[neighbor[0]][neighbor[1]])
                new_cost = cost + next_cost
                if neighbor not in paths or new_cost < queue[0][0]:  # Sprawdza, czy znaleziono lepszą ścieżkę
                    heapq.heappush(queue, (new_cost, neighbor))
                    paths[neighbor] = position

    return float('inf'), paths


def reconstruct_path(paths, end):
    path = []
    while end is not None:
        path.append(end)
        end = paths[end]
    return path[::-1]


def display_result(board, path, cost):
    for i, row in enumerate(board):
        for j, _ in enumerate(row):
            if (i, j) not in path:
                board[i][j] = ' '
    for row in board:
        print(''.join(row))
    print("\nKoszt:", cost)
