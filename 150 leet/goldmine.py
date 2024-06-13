def maxGold(mine):
    if not mine:
        return -1

    m = len(mine)
    n = len(mine[0])
    
    # Initialize the DP table
    dp = [[0] * n for _ in range(m)]
    
    # Fill the DP table
    for col in range(n - 1, -1, -1):
        for row in range(m):
            # Gold collected on going to the cell on the right (col+1, row)
            right = dp[row][col + 1] if col < n - 1 else 0
            # Gold collected on going to the cell to right up (col+1, row-1)
            right_up = dp[row - 1][col + 1] if row > 0 and col < n - 1 else 0
            # Gold collected on going to the cell to right down (col+1, row+1)
            right_down = dp[row + 1][col + 1] if row < m - 1 and col < n - 1 else 0
            
            # Update dp[row][col]
            dp[row][col] = mine[row][col] + max(right, right_up, right_down)
    
    # The maximum amount of gold collected will be the maximum value in the first column
    return max(dp[row][0] for row in range(m))

