class Node:
    """
    Class used to define the node structure, used in search-tree problems
    """

    def __init__(self, state=None):
        """

        :param state: puzzle grid
        """
        self.state = state
        self.parent_node = None
        self.children_nodes = []
        self.action = ""
        self.path_cost = 0
        self.depth = 0
        self.h = None


class Problem:
    """
    Class used to define different search-tree solvable problems
    """

    def __init__(self):
        self.initial_state = None
        self.goal_test = None
        self.successor_fn = None
        self.step_cost = None
        self.heuristic_fn = None


class SearchStrategies:
    """
    Class that defines the search strategies algorithms along with the expand method
    """

    @staticmethod
    def breadthFirstSearch(problem):
        """
        Implementation of the Breadth-First search
        :param problem: problem to solve
        :return: If a solutions is found goal node, number of expanded nodes and total nodes otherwise None
        """
        fringe = []
        expanded_nodes = 1
        total_nodes = 1
        fringe.append(Node(problem.initial_state))
        while fringe:
            node = fringe.pop(0)
            expanded_nodes += 1
            if problem.goal_test(node):
                print("Expanded nodes:", expanded_nodes)
                print("Total nodes:", total_nodes)
                return node, expanded_nodes, total_nodes
            for n in SearchStrategies.expand(node, problem):
                total_nodes += 1
                fringe.append(n)
        return None

    @staticmethod
    def depthFirstSearch(problem, depth=None):
        """
        Implementation of the Depth-First search
        :param problem: problem to solve
        :param depth: max_depth value, used only with Iterative Depth-First search
        :return: If a solutions is found goal node, number of expanded nodes and total nodes otherwise None,None,None
        """
        fringe = []
        expanded_nodes = 1
        total_nodes = 1
        explored_states = []
        fringe.append(Node(problem.initial_state))
        while fringe:
            node = fringe.pop()
            expanded_nodes += 1
            if problem.goal_test(node):
                print("Expanded nodes:", expanded_nodes)
                print("Total nodes:", total_nodes)
                return node, expanded_nodes, total_nodes
            new_nodes = SearchStrategies.expand(node, problem)
            if (depth is not None and node.depth <= depth) or depth is None:
                explored_states.append(node.state.grid)
                if not new_nodes:
                    for i in range(node.depth):
                        delete = True
                        for n in fringe:
                            if node == n.parent_node:
                                delete = False
                                break
                        if delete:
                            print("delete")
                            tmp = node.parent_node
                            tmp.children_nodes.remove(node)
                            total_nodes -= 1
                            node = tmp
                for n in new_nodes:
                    if n.state.grid not in explored_states:
                        total_nodes += 1
                        fringe.append(n)
        return None, None, None

    @staticmethod
    def iterativeDepthFirstSearch(problem):
        """
        Implementation of the Iterative Depth-First search
        This reuses the depth-first algorithm
        :param problem: problem to solve
        :return: If a solutions is found goal node, number of expanded nodes and total nodes otherwise None,None,None
        """
        depth = 1
        max_depth = 10000
        res = None
        expanded_nodes = 0
        total_nodes = 0
        while depth < max_depth:
            res, expanded_nodes, total_nodes = SearchStrategies.depthFirstSearch(
                problem, depth
            )
            if res is None:
                depth += 1
            else:
                break
        return res, expanded_nodes, total_nodes

    @staticmethod
    def aStarSearch(problem):
        """
        Implementation of the A* algorithm
        :param problem: problem to solve
        :return: If a solutions is found goal node, number of expanded nodes and total nodes otherwise None
        """
        fringe = []
        expanded_nodes = 1
        total_nodes = 1
        if problem.heuristic_fn is None:
            raise AttributeError("missing heuristic function")
        fringe.append(Node(problem.initial_state))
        fringe[0].h = fringe[0].path_cost + problem.heuristic_fn(fringe[0].state)
        while fringe:
            fringe.sort(key=SearchStrategies.h)
            # min_node = fringe[0]
            # min_val = min_node.path_cost + problem.heuristic_fn(min_node.state)
            # for n in fringe[1:]:
            #     cur = n.path_cost + problem.heuristic_fn(n.state)
            #     if cur < min_val:
            #         min_node = n
            #         min_val = cur
            node = fringe.pop(0)
            # fringe.remove(node)
            expanded_nodes += 1
            if problem.goal_test(node):
                print("Expanded nodes:", expanded_nodes)
                print("Total nodes:", total_nodes)
                return node, expanded_nodes, total_nodes

            for n in SearchStrategies.expand(node, problem):
                total_nodes += 1
                fringe.append(n)
        return None

    @staticmethod
    def expand(node, problem):
        """
        Method to expand a given node and find the successors
        :param node: node to expand
        :param problem: problem definition, in order to call the correct successor function
        :return: Eventual successors of node
        """
        successors = []
        for (action, result) in problem.successor_fn(node.state):
            if node.parent_node is not None and result == node.parent_node.state:
                continue
            n = Node()
            n.state = result
            n.parent_node = node
            n.action = action
            n.path_cost = node.path_cost + 1
            n.depth = node.depth + 1
            if problem.heuristic_fn is not None:
                n.h = n.path_cost + problem.heuristic_fn(n.state)
            n.children_nodes = []
            node.children_nodes.append(n)
            successors.append(n)
        return successors

    @staticmethod
    def h(e):
        """
        sorter function that returns the heuristic value
        :param e: element
        :return: heuristic field
        """
        return e.h
