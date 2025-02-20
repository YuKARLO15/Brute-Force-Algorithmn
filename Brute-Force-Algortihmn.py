#Karlo Robert C. Wagan
#BSCS - 3
#ITP 6 - Algorithm And Complexity

from itertools import permutations

def brute_force_search(arr, target):
    print(f"Searching for {target} in {arr}")
    for num in arr:
        print(f"Checking {num}")
        if num == target:
            print("Found target!")
            return True
    print("Target not found.")
    return False

def tsp(graph):
    n = len(graph)
    min_cost = float('inf')
    best_path = []
    
    for perm in permutations(range(1, n)):
        cost = 0
        k = 0  # Start from city 0
        path = [0] + list(perm)
        print(f"Checking path: {path}")
        
        for j in path:
            print(f"Moving from {k} to {j} with cost {graph[k][j]}")
            cost += graph[k][j]
            k = j
        cost += graph[k][0]  # Return to start
        print(f"Returning to 0 with cost {graph[k][0]}, Total Cost: {cost}")
        
        if cost < min_cost:
            min_cost = cost
            best_path = path
            print(f"New best path: {best_path} with cost {min_cost}")
    
    return min_cost, best_path

def knapsack(weights, values, capacity, n):
    print(f"Checking items: {weights} with values {values} and capacity {capacity}")
    if n == 0 or capacity == 0:
        print("Base case reached.")
        return 0
    
    if weights[n-1] > capacity:
        print(f"Skipping item {n} with weight {weights[n-1]} as it exceeds capacity")
        return knapsack(weights, values, capacity, n-1)
    
    print(f"Including item {n} with weight {weights[n-1]} and value {values[n-1]}")
    include = values[n-1] + knapsack(weights, values, capacity - weights[n-1], n-1)
    print(f"Excluding item {n}")
    exclude = knapsack(weights, values, capacity, n-1)
    
    result = max(include, exclude)
    print(f"Best value at this stage: {result}")
    return result

# Example usage:
print("Brute Force Algorithm")
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 9
print("Brute Force Search:", brute_force_search(arr, target))
print("---------------------------------------------------------------------------------------------\n")

print("Travelling Salesman Problem")
graph = [[0, 10, 15, 20],
         [10, 0, 35, 25],
         [15, 35, 0, 30],
         [20, 25, 30, 0]]
print("TSP Solution:", tsp(graph))
print("---------------------------------------------------------------------------------------------\n")

print("Knapsack Problem")
weights = [10, 20, 30, 40, 50]
values = [60, 100, 120, 240, 150]
capacity = 80
n = len(weights)
print("Knapsack Solution:", knapsack(weights, values, capacity, n))