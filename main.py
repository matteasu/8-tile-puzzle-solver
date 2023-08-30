import time
import json
from puzzle import Puzzle, Utils
from tree import Problem, SearchStrategies
from analysis import analysis

# Problem initialization
problem = Problem()

# array of puzzles to be solved using the different algorithms
puzzles = [
    Puzzle([[7, 2, 4], [5, -1, 6], [8, 3, 1]]),
    Puzzle([[5, 4, -1], [6, 1, 8], [7, 3, 2]]),
    Puzzle([[-1, 1, 2], [3, 4, 5], [6, 7, 8]]),
    Puzzle([[2, 1, 3], [8, -1, 4], [7, 6, 5]]),
    Puzzle([[1, 3, 5], [8, -1, 2], [6, 4, 7]]),
    Puzzle([[6, 5, 2], [7, 1, 4], [-1, 3, 8]]),
    Puzzle([[2, 8, 3], [4, 6, 1], [7, -1, 5]]),
    Puzzle([[-1, 1, 2], [4, 6, 8], [5, 7, 3]]),
    Puzzle([[1, 4, 6], [8, 7, 5], [2, 3, -1]]),
    Puzzle([[1, 2, 3], [5, 6, -1], [7, 8, 4]]),
]

# output dictionary that contains the analysis results, this will be then salved into a JSON file
output = dict()
# lambda functions that checks if goal state has been reached
problem.goal_test = lambda n: n.state.grid == [[1, 2, 3], [4, 5, 6], [7, 8, -1]]
# loading the successor function for the puzzle problem
problem.successor_fn = Utils.successor_fn
# defining step cost
problem.step_cost = 1

for puzzle in puzzles:
    # checking if the puzzle is solvable or not, useful in case of random puzzle generation or different test set
    if Utils.is_solvable(puzzle) is False:
        print("non solvable")
        # if a puzzle is not solvable the program moves to the next one
        continue
    # dictionary that will hold all the information and result of the current puzzle
    log = dict()
    # dictionary used to store the execution times for each algorithm
    times = dict()
    # dictionary used to store the cost and the depth of the solution for each algorithm
    solution = {"cost": {}, "depth": {}}
    # dictionary used to store the number of expanded nodes and total nodes for each algorithm
    nodes_count = {"expanded_nodes": {}, "total_nodes": {}}
    # dictionary used to store the actions needed to reach the goal state
    solution_actions = dict()
    # storing the puzzle grid for visualization purposes
    log["puzzle"] = puzzle.grid
    # index used to later refer at a specific puzzle in the output file
    index = puzzles.index(puzzle)
    # updating the problem to use the current puzzle
    problem.initial_state = puzzle
    print(puzzle.grid)

    # print("Starting BFS search...")
    # # start time
    # start_time = time.process_time()
    # (
    #     res,
    #     nodes_count["expanded_nodes"]["BFS"],
    #     nodes_count["total_nodes"]["BFS"],
    # ) = SearchStrategies.breadthFirstSearch(problem)
    # # total execution time
    # total_time = time.process_time() - start_time
    # # storing execution time for BFS
    # times["BFS"] = total_time
    # print("solution found")
    # print("{} seconds for solving with Breadth First".format(total_time))
    # # storing the solution path for BFS
    # solution_actions["BFS"] = Utils.reverseTraversal(res)
    #
    # print("Path cost of the solution:", res.path_cost)
    # print("Depth of the solution:", res.depth)
    # # storing total path cost and depth of the solution
    # solution["cost"]["BFS"] = res.path_cost
    # solution["depth"]["BFS"] = res.depth
    # print("\n")
    #
    # print("Starting with DFS...")
    # start_time = time.process_time()
    # (
    #     res,
    #     nodes_count["expanded_nodes"]["DFS"],
    #     nodes_count["total_nodes"]["DFS"],
    # ) = SearchStrategies.depthFirstSearch(problem)
    # total_time = time.process_time() - start_time
    # times["DFS"] = total_time
    # print("solution found")
    # print("{} seconds for solving with Depth First".format(total_time))
    # solution_actions["DFS"] = Utils.reverseTraversal(res)
    # print("Path cost of the solution:", res.path_cost)
    # print("Depth of the solution:", res.depth)
    # solution["cost"]["DFS"] = res.path_cost
    # solution["depth"]["DFS"] = res.depth
    # print("\n")
    # print("Starting with IDFS...")
    # start_time = time.process_time()
    # (
    #     res,
    #     nodes_count["expanded_nodes"]["IDFS"],
    #     nodes_count["total_nodes"]["IDFS"],
    # ) = SearchStrategies.iterativeDepthFirstSearch(problem)
    # total_time = time.process_time() - start_time
    # times["IDFS"] = total_time
    # print("solution found")
    # print("{} seconds for solving with Iterative Depth First".format(total_time))
    # solution_actions["IDFS"] = Utils.reverseTraversal(res)
    # print("Path cost of the solution:", res.path_cost)
    # print("Depth of the solution:", res.depth)
    # solution["cost"]["IDFS"] = res.path_cost
    # solution["depth"]["IDFS"] = res.depth
    print("\n")
    print("Starting with A* using the misplaced heuristic")
    problem.heuristic_fn = Utils.misplaced_heuristic
    start_time = time.process_time()
    (
        res,
        nodes_count["expanded_nodes"]["A*_misplaced"],
        nodes_count["total_nodes"]["A*_misplaced"],
    ) = SearchStrategies.aStarSearch(problem)
    total_time = time.process_time() - start_time
    times["A*_misplaced"] = total_time
    print("solution found")
    print(
        "{} seconds for solving with A* using the misplaced heuristic".format(
            total_time
        )
    )
    solution_actions["A*_misplaced"] = Utils.reverseTraversal(res)
    print("Path cost of the solution:", res.path_cost)
    print("Depth of the solution:", res.depth)
    solution["cost"]["A*_misplaced"] = res.path_cost
    solution["depth"]["A*_misplaced"] = res.depth
    print("\n")
    print("Startin with A* using the manhattan heuristic")
    problem.heuristic_fn = Utils.manhattan_heuristic
    start_time = time.process_time()
    (
        res,
        nodes_count["expanded_nodes"]["A*_manhattan"],
        nodes_count["total_nodes"]["A*_manhattan"],
    ) = SearchStrategies.aStarSearch(problem)
    total_time = time.process_time() - start_time
    times["A*_manhattan"] = total_time
    print("solution found")
    print(
        "{} seconds for solving with A* using the Manhattan heuristic".format(
            total_time
        )
    )
    solution_actions["A*_manhattan"] = Utils.reverseTraversal(res)
    print("Path cost of the solution:", res.path_cost)
    print("Depth of the solution:", res.depth)
    solution["cost"]["A*_manhattan"] = res.path_cost
    solution["depth"]["A*_manhattan"] = res.depth

    # storing all the metrics in a single dictionary
    log["nodes_count"] = nodes_count
    log["times"] = times
    log["solutions_actions"] = solution_actions
    log["solutions_cost"] = solution
    # storing the metrics for the current puzzle in the main dictionary
    output[index.__str__()] = log
    print("\n")

# output file creation
f = open("output.json", "w")
# saving the contents of the output dictionary in the JSON file just created
json.dump(output, f)
f.close()
analysis()
print("Average values saved in averages.json")
