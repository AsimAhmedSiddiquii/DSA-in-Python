dp = {1:1, 2:2, 3:6}

def factorial(n):
    if n in dp:
        return dp[n]
    else:
        dp[n] = n * factorial(n-1)
        return dp[n] 

print(factorial(5))
print(factorial(4))
print(factorial(6))
print(factorial(1))
print(dp)
