import timeit
class Knapsack:
    def __init__(self, weights, values, capacity):
        self.weights = weights
        self.values = values
        self.capacity = capacity
        self.n = len(weights)
        self.dp = [[0] * (capacity + 1) for _ in range(self.n + 1)]
    
    def dynamicSolve (self):
        for i in range(1, self.n + 1):
            for j in range(self.capacity + 1):
                if self.weights[i - 1] <= j:
                    self.dp[i][j] = max(self.dp[i - 1][j], self.dp[i - 1][j - self.weights[i - 1]] + self.values[i - 1])
                else:
                    self.dp[i][j] = self.dp[i - 1][j]
        return self.dp[self.n][self.capacity]
    def greedySolve(self):
        x = [0] * self.n
        isi = self.capacity
        for i in range(self.n):
            if self.weights[i] > isi:
                break
            x[i] = 1
            isi -= self.weights[i]
        if i < self.n:
            x[i] = isi / self.weights[i]
        return x

    def display_with_Greedy(self):
        x = self.greedySolve()
        total_value = sum(x[i] * self.values[i] for i in range(self.n))
        total_weight = sum(x[i] * self.weights[i] for i in range(self.n))
        print("Greedy Solution:")
        print("Item   Fraction   Value   Weight")
        for i in range(self.n):
            print(f"{i+1:4} {x[i]:9.2f} {x[i] * self.values[i]:7.2f} {x[i] * self.weights[i]:7.2f}")
        print(f"Total value: {total_value:.2f}")
        print(f"Total weight: {total_weight:.2f}")
    def display_table(self):
        for row in self.dp:
            print(' '.join(f'{x:3}' for x in row))
    
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

knapsack = Knapsack(weights, values, capacity)
max_value = knapsack.dynamicSolve()
setup_code = '''
from __main__ import Knapsack

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

knapsack = Knapsack(weights, values, capacity)
'''

statement = 'knapsack.dynamicSolve()'

execution_time = timeit.timeit(stmt=statement, setup=setup_code, number=1)

print(f"Execution time (Dynamic Programming): {execution_time:.10f} seconds")
print(f"Maximum value that can be taken: {max_value}")
print("DP Table:")
knapsack.display_table()
setup_code_greedy = '''
from __main__ import Knapsack

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

knapsack = Knapsack(weights, values, capacity)
'''

statement_greedy = 'knapsack.greedySolve()'

execution_time_greedy = timeit.timeit(stmt=statement_greedy, setup=setup_code_greedy, number=1)

print(f"\nExecution time (Greedy Algorithm): {execution_time_greedy:.10f} seconds")
knapsack.display_with_Greedy()
