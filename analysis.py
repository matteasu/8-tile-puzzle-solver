import json
import statistics


def analysis():
    with open("output.json", "r") as f:
        parsed = json.load(f)
    averages = {
        "BFS": {},
        "DFS": {},
        "IDFS": {},
        "A*_misplaced": {},
        "A*_manhattan": {},
    }
    sums = {"BFS": {}, "DFS": {}, "IDFS": {}, "A*_misplaced": {}, "A*_manhattan": {}}
    algorithms = parsed["0"]["times"].keys()
    for algo in algorithms:
        sums[algo]["times"] = []
        sums[algo]["generated_nodes"] = []
        sums[algo]["expanded_nodes"] = []
        sums[algo]["depth"] = []

    for puzzle in parsed.keys():
        for algo in algorithms:
            sums[algo]["times"].append(parsed[puzzle]["times"][algo])
            sums[algo]["generated_nodes"].append(
                parsed[puzzle]["nodes_count"]["total_nodes"][algo]
            )
            sums[algo]["expanded_nodes"].append(
                parsed[puzzle]["nodes_count"]["expanded_nodes"][algo]
            )
            sums[algo]["depth"].append(parsed[puzzle]["solutions_cost"]["depth"][algo])

    for algo in algorithms:
        averages[algo]["time"] = statistics.mean(sums[algo]["times"])
        averages[algo]["generated_nodes"] = statistics.mean(
            sums[algo]["generated_nodes"]
        )
        averages[algo]["expanded_nodes"] = statistics.mean(sums[algo]["expanded_nodes"])
        averages[algo]["depth"] = statistics.mean(sums[algo]["depth"])
    with open("averages.json", "w") as avg:
        json.dump(averages, avg)


if __name__ == "__main__":
    analysis()
