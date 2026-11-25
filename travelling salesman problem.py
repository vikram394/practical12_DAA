
from itertools import permutations

n = 4

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

vertices = [1, 2, 3]
min_cost = float('inf')

for p in permutations(vertices):
    cost = 0
    k = 0

    for j in p:
        cost += graph[k][j]
        k = j

    cost += graph[k][0]

    if cost < min_cost:
        min_cost = cost
        best_path = (0,) + p + (0,)

print("Travelling Salesman Problem")
print("Minimum Cost:", min_cost)
print("Optimal Path:", best_path)
