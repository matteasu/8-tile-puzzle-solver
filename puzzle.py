from copy import deepcopy


class Puzzle:
    def __init__(self, grid=None):
        if grid is None:
            grid = []
        self.grid = grid

    def __eq__(self, other):
        return self.grid == other.grid


class Utils:
    @staticmethod
    def successor_fn(state):
        """
        Given a state it returns the possible reachable states
        :param state: current state
        :return: list of successors
        """
        grid = state.grid
        res = []
        coord = [-1, -1]  # first element holds row, second the column
        # looking for -1 coordinates
        for row, col in enumerate(grid):
            if -1 in grid[row]:
                coord = [row, grid[row].index(-1)]
        if coord != [-1, -1]:
            if coord[0] + 1 < len(grid[0]):
                tmp = deepcopy(grid)
                row = coord[0]
                col = coord[1]
                tmp[row][col] = tmp[row + 1][col]
                tmp[row + 1][col] = -1
                res.append(("down", Puzzle(tmp)))

            if coord[0] - 1 >= 0:
                tmp = deepcopy(grid)
                row = coord[0]
                col = coord[1]
                tmp[row][col] = tmp[row - 1][col]
                tmp[row - 1][col] = -1
                res.append(("up", Puzzle(tmp)))

            if coord[1] + 1 < len(grid[0]):
                tmp = deepcopy(grid)
                row = coord[0]
                col = coord[1]
                tmp[row][col] = tmp[row][col + 1]
                tmp[row][col + 1] = -1
                res.append(("right", Puzzle(tmp)))

            if coord[1] - 1 >= 0:
                tmp = deepcopy(grid)
                row = coord[0]
                col = coord[1]
                tmp[row][col] = tmp[row][col - 1]
                tmp[row][col - 1] = -1
                res.append(("left", Puzzle(tmp)))
        return res

    @staticmethod
    def manhattan_heuristic(state):
        """
        Implementation of the Manhattan Heuristic
        :param state: current state
        :return: heuristic value
        """
        grid = state.grid
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, -1]]
        manhattan = 0
        for i in range(1, 9):
            grid_coord = [
                (index, row.index(i)) for index, row in enumerate(grid) if i in row
            ]
            goal_coord = [
                (index, row.index(i)) for index, row in enumerate(goal) if i in row
            ]
            manhattan += abs(goal_coord[0][0] - grid_coord[0][0]) + abs(
                goal_coord[0][1] - grid_coord[0][1]
            )
        return manhattan

    @staticmethod
    def misplaced_heuristic(state):
        """
        Implementation of the misplaced heuristic
        :param state:current state
        :return: number of misplaced tiles
        """
        grid = state.grid
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, -1]]
        misplaced = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != goal[i][j]:
                    misplaced += 1

        return misplaced

    @staticmethod
    def is_solvable(puzzle):
        """
        Method used to determine werther a puzzle is solvable or not
        :param puzzle: puzzle to check
        :return: Ture if solvable else False
        """
        return Utils.getInvCount([j for sub in puzzle.grid for j in sub]) % 2 == 0

    @staticmethod
    def getInvCount(grid):
        """
        method used to count the number of inversions inside a puzzle
        :param grid:  grid to check
        :return: number of inversions
        """
        inv_count = 0
        for i in range(0, 9):
            for j in range(i + 1, 9):
                if grid[j] != -1 and grid[i] != -1 and grid[i] > grid[j]:
                    inv_count += 1
        return inv_count

    @staticmethod
    def reverseTraversal(final_node):
        """
        method that returns the list of actions needed to reach the goal state
        :param final_node: node given in return from the execution of one of the search algorithms
        :return: list of actions needed to reach the goal state
        """
        solution = []
        cur = final_node
        while cur.parent_node is not None:
            solution.append(cur.action)
            cur = cur.parent_node

        solution.reverse()
        return solution
