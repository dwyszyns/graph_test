import graf
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py filename")
        sys.exit(1)

    file_name = sys.argv[1]  # Załóżmy, że plik o tej nazwie istnieje i zawiera planszę
    board = graf.read_board(file_name)
    start, end = graf.find_xs(board)
    cost, paths = graf.dijkstra(board, start, end)
    path = graf.reconstruct_path(paths, end)
    graf.display_result(board, path, cost)
