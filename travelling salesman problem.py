
from itertools import permutations

n = 4

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

start = 0
vertices = [i for i in range(n) if i != start]

min_cost = float('inf')

for p in permutations(vertices):
    cost = 0
    k = start

    for j in p:
        cost += graph[k][j]
        k = j

    cost += graph[k][start]

    min_cost = min(min_cost, cost)

print("Minimum travelling cost:", min_cost)
