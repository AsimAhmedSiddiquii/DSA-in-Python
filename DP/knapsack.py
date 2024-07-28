weights = [1, 2, 3]
profits = [10, 15, 40]
capacity = 6

#    0   1   2   3   4   5   6
# 0  0   0   0   0   0   0   0
# 1  0  10  10  10  10  10  10
# 2  0  10  15  25  25  25  25
# 3  0  10  15  40  50  55  65

dp = [[0 for i in range(capacity+1)] for j in range(len(weights)+1)]

for i in range(len(weights)+1):
    for w in range(capacity+1):
        if i == 0 or w == 0:
            dp[i][w] == 0
        elif weights[i-1] <= w:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + profits[i-1])
        else:
            dp[i][w] = dp[i-1][w]
print(dp[len(weights)-1][capacity])