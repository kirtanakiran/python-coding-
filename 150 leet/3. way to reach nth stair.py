def PossibleWays(n, m):
    if n == 0:
        return 1  # There's one way to stay at the ground (doing nothing)
    if n < 0:
        return 0  # No way to climb negative stairs
    
    # Initialize the dp array with zeros
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: one way to reach the 0th stair
    
    for i in range(1, n + 1):
        dp[i] = 0
        for j in range(1, m + 1):
            if i - j >= 0:
                dp[i] += dp[i - j]
    
    return dp[n]
