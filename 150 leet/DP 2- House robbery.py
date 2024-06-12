class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[-1]

#optimisation - O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

    prev1 = nums[0]
    prev2 = max(nums[0], nums[1])

    for i in range(2, n):
      current = max(prev2, nums[i] + prev1)
      prev1 = prev2
      prev2 = current

    return prev2
