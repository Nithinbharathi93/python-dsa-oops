def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

n = int(input("Enter number of items: "))
weights = list(map(int, input("Enter weights of items: ").split()))
values = list(map(int, input("Enter values of items: ").split()))
capacity = int(input("Enter capacity of knapsack: "))
print("Maximum value in Knapsack =", knapsack(weights, values, capacity))
