#Karlo Robert C. Wagan
#BSCS - 3
#ITP 6 - Algorithm And Complexity

from itertools import permutations

def brute_force_search(arr, target):
    for num in arr:
        if num == target:
            return True
    return False

# Example usage:
arr = [1, 2, 3, 4, 5]
target = 3
print("Brute Force Search:", brute_force_search(arr, target))

# Travelling Salesman Problem (TSP) - Brute Force Approach
def tsp(graph):
    n = len(graph)
    min_cost = float('inf')
    best_path = []
    
    for perm in permutations(range(1, n)):
        cost = 0
        k = 0  # Start from city 0
        path = [0] + list(perm)
        
        for j in path:
            cost += graph[k][j]
            k = j
        cost += graph[k][0]  # Return to start
        
        if cost < min_cost:
            min_cost = cost
            best_path = path
    
    return min_cost, best_path

# Example usage
graph = [[0, 10, 15, 20],
         [10, 0, 35, 25],
         [15, 35, 0, 30],
         [20, 25, 30, 0]]
print("TSP Solution:", tsp(graph))

# Knapsack Problem - Brute Force Approach
def knapsack(weights, values, capacity, n):
    if n == 0 or capacity == 0:
        return 0
    
    if weights[n-1] > capacity:
        return knapsack(weights, values, capacity, n-1)
    
    include = values[n-1] + knapsack(weights, values, capacity - weights[n-1], n-1)
    exclude = knapsack(weights, values, capacity, n-1)
    
    return max(include, exclude)

# Example usage:
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
n = len(weights)
print("Knapsack Solution:", knapsack(weights, values, capacity, n))
