"""# Artificial Intelligence Laboratory 2025 CS 4271
## Raksha Pahariya | 2021CSB029

##03_A*_Grid
In a spatial context defined by a square grid featuring numerous obstacles, a task is presented wherein a starting cell, and a target cell are specified. The objective is to efficiently traverse from the starting cell to the target cell, optimizing for expeditious navigation. In this scenario, the A* Search algorithm proves instrumental.

 The A* Search algorithm operates by meticulously selecting nodes within the grid, employing a parameter denoted as 'f.' This parameter, critical to the decision-making process, is the summation of two distinct parameters – 'g' and 'h.' At each iterative step, the algorithm strategically identifies the node with the lowest 'f' value and progresses the exploration accordingly. The allowed actions are: left, right, top, bottom, and diagonal.

The parameters 'g' and 'h' are delineated as follows:

- 'g': Represents the cumulative movement cost incurred in traversing the path from the designated starting point to the current square on the grid.
- 'h': Constitutes the estimated movement cost anticipated for the traversal from the current square on the grid to the specified destination, by using either Manhattan or Euclidean distance.

This element, often denoted as the heuristic, embodies an intelligent estimation. The A* Search algorithm, distinguished by its ability to efficiently find optimal or near optimal paths amidst obstacles, holds significant applicability in diverse domains such as robotics, gaming, and route planning.

![image.png](data:image/png;base64,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)

###input in the form of a matrix where:

'S' represents the starting point.

'G' represents the goal.

1 represents a path (walkable).

0 represents an obstacle (not walkable).
"""

import math
import heapq

def find_start_and_goal(matrix):
    """
    Find the start ('S') and goal ('G') positions in the matrix.
    """
    start = None
    goal = None
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'S':
                start = (i, j)
            elif matrix[i][j] == 'G':
                goal = (i, j)
    if start is None or goal is None:
        raise ValueError("Matrix must contain both 'S' (start) and 'G' (goal).")
    return start, goal

def calculate_heuristic(current, target, heuristic_type):
    """
    Calculate the heuristic value (h) for the A* algorithm.
    """
    if heuristic_type == "manhattan":
        return abs(current[0] - target[0]) + abs(current[1] - target[1])
    elif heuristic_type == "euclidean":
        return math.sqrt((current[0] - target[0])**2 + (current[1] - target[1])**2)
    else:
        raise ValueError("Invalid heuristic type. Use 'manhattan' or 'euclidean'.")

def get_neighbors(node, grid):
    """
    Get valid neighbors of the current node.
    """
    neighbors = []
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),  # Left, Right, Up, Down
        (-1, -1), (1, 1), (-1, 1), (1, -1)  # Diagonal directions
    ]
    for dx, dy in directions:
        x, y = node[0] + dx, node[1] + dy
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != -1:
            neighbors.append((x, y))
    return neighbors

def a_star_search(matrix, heuristic_type):
    """
    A* Search Algorithm to find the optimal path.
    """
    start, goal = find_start_and_goal(matrix)
    open_set = []  # Priority queue for nodes to explore
    heapq.heappush(open_set, (0, start))

    g_cost = {start: 0}  # Cost from start to a node
    f_cost = {start: calculate_heuristic(start, goal, heuristic_type)}  # Total cost
    parents = {start: None}  # Track the path

    while open_set:
        current = heapq.heappop(open_set)[1]  # Node with lowest f-cost

        # If goal is reached, reconstruct the path
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1]  # Return reversed path

        # Explore neighbors
        for neighbor in get_neighbors(current, matrix):
            tentative_g = g_cost[current] + 1  # Assume uniform cost for all moves

            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                h = calculate_heuristic(neighbor, goal, heuristic_type)
                f_cost[neighbor] = g_cost[neighbor] + h
                parents[neighbor] = current

                # Add to open set
                heapq.heappush(open_set, (f_cost[neighbor], neighbor))

    return None  # No path found

def visualize_path(matrix, path):
    """
    Visualize the matrix with the path.
    """
    for x, y in path:
        if matrix[x][y] not in ('S', 'G'):  # Don't overwrite start/goal
            matrix[x][y] = '*'
    for row in matrix:
        print(" ".join(str(cell) for cell in row))

if __name__ == "__main__":
    matrix = [
        ['S', 1, 1, 0, 0],
        [1, 0, 1, 1, 0],
        [1, 1, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 1, 1, 'G']
    ]

    # Display input grid
    print("\n--- Input Grid ---")
    for row in matrix:
        print(" ".join(str(cell) for cell in row))

    # Run A* Search for both heuristics
    for heuristic_type in ["manhattan", "euclidean"]:
        path = a_star_search(matrix, heuristic_type)

        # Display heuristic used
        print(f"\nHeuristic Used: {heuristic_type.capitalize()}")

        # Display output
        if path:
            print("\n--- Output Grid with Path ---")
            visualize_path(matrix, path)
        else:
            print("\nNo path found.")

if __name__ == "__main__":
    matrix = [
        ['S', 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 'G']
    ]

    # Display input grid
    print("\n--- Input Grid ---")
    for row in matrix:
        print(" ".join(str(cell) for cell in row))

    # Run A* Search for both heuristics
    for heuristic_type in ["manhattan", "euclidean"]:
        path = a_star_search(matrix, heuristic_type)

        # Display heuristic used
        print(f"\nHeuristic Used: {heuristic_type.capitalize()}")

        # Display output
        if path:
            print("\n--- Output Grid with Path ---")
            visualize_path(matrix, path)
        else:
            print("\nNo path found.")