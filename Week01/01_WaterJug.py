"""# Artificial Intelligence Laboratory 2025 CS 4271
## Raksha Pahariya | 2021CSB029

## 01_WaterJug

In the realm of Artificial Intelligence, contemplate a problem involving two containers  of indeterminate capacity, referred to as jugs. One jug has a capacity of 3 units, while  the other holds up to 4 units. There is no markings or additional measuring instruments,  the objective is to develop a strategic approach to precisely fill the 4-unit jug with 2  units of water. The restriction stipulates the use of solely the aforementioned jugs,  excluding any supplementary tools. Both jugs initiate the scenario in an empty state.  The aim is to attain the desired water quantity in the 4-unit jug by executing a sequence  of permissible operations, including filling, emptying, and pouring water between the  jugs.

The challenge in this scenario involves crafting an algorithm:


a. Define the permissible operations carefully that includes filling, emptying, and  pouring water between the jugs.


b. Use both Depth First Search and Breadth First Search to systematically explore and determine the optimal sequence of moves for accomplishing the task while  adhering to the defined constraints. Also determine the total path count to reach  to the goal state.


c. The initial and the goal state of the jugs may be varied.
"""

from collections import deque

def is_valid_state(state, capacity1, capacity2):
    """
    Check if the given state is valid within the jug capacities.
    """
    x, y = state
    return 0 <= x <= capacity1 and 0 <= y <= capacity2

def generate_next_states(state, capacity1, capacity2):
    """
    Generate all possible next states from the current state.
    """
    x, y = state
    return [
        (capacity1, y),  # Fill jug1 completely
        (x, capacity2),  # Fill jug2 completely
        (0, y),          # Empty jug1
        (x, 0),          # Empty jug2
        (max(0, x - (capacity2 - y)), min(capacity2, x + y)),  # Pour jug1 -> jug2
        (min(capacity1, x + y), max(0, y - (capacity1 - x)))   # Pour jug2 -> jug1
    ]

def water_jug_solver(capacity1, capacity2, initial_state, goal_state, method="BFS"):
    """
    Solve the water jug problem using the specified method (BFS or DFS).

    Args:
        capacity1 (int): Capacity of the first jug.
        capacity2 (int): Capacity of the second jug.
        initial_state (tuple): Starting state, e.g., (0, 0).
        goal_state (tuple): Target state to reach, e.g., (0, 2).
        method (str): Method to use ("BFS" or "DFS").

    Returns:
        path (list): Sequence of states to reach the target.
        steps (int): Total number of steps to reach the target.
        total_paths (int): Total paths explored during the search.
    """
    visited = set()
    total_paths = 0

    if method == "BFS":
        queue = deque([(initial_state, [])])
        while queue:
            current_state, path = queue.popleft()

            if current_state in visited:
                continue
            visited.add(current_state)

            path = path + [current_state]

            # Check if the goal state is reached
            if current_state == goal_state:
                total_paths += 1
                return path, len(path) - 1, total_paths

            # Generate and explore next states
            for next_state in generate_next_states(current_state, capacity1, capacity2):
                if is_valid_state(next_state, capacity1, capacity2) and next_state not in visited:
                    queue.append((next_state, path))

    elif method == "DFS":
        stack = [(initial_state, [])]
        while stack:
            current_state, path = stack.pop()

            if current_state in visited:
                continue
            visited.add(current_state)

            path = path + [current_state]

            # Check if the goal state is reached
            if current_state == goal_state:
                total_paths += 1
                return path, len(path) - 1, total_paths

            # Generate and explore next states
            for next_state in generate_next_states(current_state, capacity1, capacity2):
                if is_valid_state(next_state, capacity1, capacity2) and next_state not in visited:
                    stack.append((next_state, path))

    return None, -1, 0

def print_solution(path, steps, total_paths, goal_state):
    """
    Print the solution details, including the path, total steps, and paths explored.
    """
    if path:
        print(f"Steps to achieve goal state {goal_state}:")
        for i, step in enumerate(path):
            print(f"Step {i}: Jug1 = {step[0]}, Jug2 = {step[1]}")
        print(f"Total steps: {steps}")
        print(f"Total paths explored: {total_paths}")
    else:
        print("No solution found.")

# Example Usage
if __name__ == "__main__":
    capacity1 = 3
    capacity2 = 4
    initial_state = (0, 0)
    goal_state = (0, 2)

    method = "BFS"  # or "DFS"
    path, steps, total_paths = water_jug_solver(capacity1, capacity2, initial_state, goal_state, method)
    print_solution(path, steps, total_paths, goal_state)

# Example Usage
if __name__ == "__main__":
    capacity1 = 3
    capacity2 = 4
    initial_state = (0, 0)
    goal_state = (0, 2)

    method = "DFS"
    path, steps, total_paths = water_jug_solver(capacity1, capacity2, initial_state, goal_state, method)
    print_solution(path, steps, total_paths, goal_state)

# Example Usage
if __name__ == "__main__":
    capacity1 = 3
    capacity2 = 4
    initial_state = (1, 0)
    goal_state = (0, 2)

    method = "DFS"
    path, steps, total_paths = water_jug_solver(capacity1, capacity2, initial_state, goal_state, method)
    print_solution(path, steps, total_paths, goal_state)