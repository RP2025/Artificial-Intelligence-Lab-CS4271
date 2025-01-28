"""# Artificial Intelligence Laboratory 2025 CS 4271
## Raksha Pahariya | 2021CSB029

##04_AO*_PathFinder

In a spatial context defined by a square matrix of order N * N, a rat is situated at the starting point (0,0), aiming to reach the destination at (N-1, N-1).
The task at hand is to enumerate all feasible paths that the rat can undertake to traverse from the source to the destination.

The permissible directions for the rat's movement are denoted as 'U' (up), 'D' (down), 'L' (left), and 'R' (right).

Within this matrix, a cell assigned the value 0 signifies an obstruction, rendering it impassable for the rat, while a value of 1 indicates a traversable cell. The objective is to furnish a list of paths in lexicographically increasing order, with the constraint that no cell can be revisited along the path. Moreover, if the source cell is assigned a value of 0, the rat is precluded from moving to any other cell.

To accomplish this, the AO* Search algorithm is employed to systematically explore the AND-OR graph and evaluate all conceivable paths from source to destination (with path cost = 1, and heuristic values given in the diagram).

The algorithm dynamically adapts its heuristic function during the search, optimizing the exploration process. The resultant list of paths reflects a meticulous exploration of the matrix, ensuring lexicographical order and adherence to the specified constraints.
"""

import heapq

def is_valid(x, y, visited, matrix):
    """Check if a cell is valid for movement."""
    rows, cols = len(matrix), len(matrix[0])
    return (
        0 <= x < rows and 0 <= y < cols and
        matrix[x][y] is not None and matrix[x][y][1] != 0 and
        (x, y) not in visited
    )

def explore_paths(matrix, x, y, path, cost, visited, results):
    """Recursive function to explore all paths."""
    rows, cols = len(matrix), len(matrix[0])

    # If destination is reached, add the path and cost to results
    if x == rows - 1 and y == cols - 1:
        results.append((path, cost))
        return

    # Mark the current cell as visited
    visited.add((x, y))

    # Define movement directions
    directions = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }

    # Explore all valid moves
    for direction, (dx, dy) in sorted(directions.items()):
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, visited, matrix):
            next_cell = matrix[nx][ny]
            explore_paths(
                matrix, nx, ny, path + f" → {next_cell[0]}", cost + next_cell[1], visited, results
            )

    # Backtrack: unmark the current cell as visited
    visited.remove((x, y))

def find_all_paths(matrix):
    """Find all paths from the top-left to the bottom-right of the matrix."""
    if matrix[0][0] is None or matrix[0][0][1] == 0:
        return []  # If the start cell is not traversable

    results = []
    start_cell = matrix[0][0]
    explore_paths(matrix, 0, 0, start_cell[0], start_cell[1], set(), results)

    # Sort results lexicographically by path
    results.sort(key=lambda x: x[0])
    return results

def print_paths(results):
    """Print the paths and their costs."""
    for path, cost in results:
        print(f"Path: {path}, Total Cost: {cost}")

def main():
    """Main function to execute the program."""
    # Input: Matrix with tuples (alphabet, cost)
    matrix = [
        [('A', 1), ('B', 1), ('C', 1), (None, 0)],
        [('D', 1), ('E', 2), ('F', 1), ('G', 3)],
        [('H', 1), ('I', 2), (None, 0), ('J', 1)],
        [(None, 0), ('K', 1), ('L', 2), ('M', 1)]
    ]

    # Find all paths
    results = find_all_paths(matrix)



    # Print the results
    print_paths(results)

    # Find and print the shortest path
    shortest_path = min(results, key=lambda x: x[1])
    print(f"\nShortest Path: {shortest_path[0]}, Total Cost: {shortest_path[1]}")

if __name__ == "__main__":
    main()

def main():
    """Main function to execute the program."""
    # Input: Matrix with tuples (alphabet, cost)
    matrix = [
    [('A', 1), ('B', 4), (None, 0)],  # First row
    [('D', 10), ('E', 3), (None, 0)], # Second row
    [(None, 0), ('H', 2), ('I', 8)],  # Third row
    [(None, 0), ('K', 3), ('L', 5)]   # Fourth row (Destination: L)
]

    # Find all paths
    results = find_all_paths(matrix)

    # Print the results
    print_paths(results)

if __name__ == "__main__":
    main()