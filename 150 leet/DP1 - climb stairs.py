class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

#Optimised code - O(1)
#class Solution:
    #def climbStairs(self, n: int) -> int:
        #if n == 0 or n == 1:
            #return 1

        #prev1 , prev2 = 1, 1

    #for i in range(2, n+1):
        #current = prev1 + prev2
        #prev2 = prev1
        #prev1 = current
    #return prev1
