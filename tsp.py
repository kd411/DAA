n = int(input('Enter the number of vertices (> 2): '))
print('Enter the cost matrix (-1 if no edge exists):')
c = []
for _ in range(n):
    c.append(list(map(int, input().split())))
bound = 0  # lower bound
smallest = []  # store the smallest two values for easier access
solution = 1  # current best solution = sum of max cost outgoing edges + 1
for i in c:
    # Remove all -1's as they indicate the edge not being present.
    i = sorted(filter(lambda x: x != -1, i))
    smallest.append(i[0])
    bound += i[0]
    solution += i[-1]
# Covering all vertices => can start with any. Choosing 0 for simplicity
visited = {0}
current_path = [0]
best_path = []
def tsp(cost, bound, path_cost, path):
    if len(path) == n:  # If round trip complete,
        if cost[path[-1]][path[0]] != -1:  # And there exists a closing edge
            path_cost += cost[path[-1]][path[0]]  # Overwriting path_cost as it won't be used again in this call
            global solution, best_path
            if solution > path_cost:  # Update the best solution
                solution = path_cost
                best_path = path[:]
    else:
        for i in range(n):
            if i not in visited and cost[path[-1]][i] != -1:  # For all unvisited neighbors
                path_cost_i = path_cost + cost[path[-1]][i]
                bound_i = bound - smallest[path[-1]]

                # Prune nodes that have minimum expected cost higher than found solution
                if bound_i + path_cost_i < solution:
                    visited.add(i)
                    path.append(i)
                    tsp(cost, bound_i, path_cost_i, path)
                    # Undo operations
                    path.pop()
                    visited.remove(i)
# Starting with no edge => cost is 0
tsp(c, bound, 0, current_path)
if best_path:
    best_path.append(0)
    print(solution)
    print('Path:', best_path)
else:
    print('No cycle exists')