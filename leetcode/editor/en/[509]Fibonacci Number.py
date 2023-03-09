# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the 
# Fibonacci sequence, such that each number is the sum of the two preceding ones, 
# starting from 0 and 1. That is, 
# 
#  
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
#  
# 
#  Given n, calculate F(n). 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
#  
# 
#  Example 3: 
# 
#  
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= n <= 30 
#  
# 
#  Related Topics Math Dynamic Programming Recursion Memoization 👍 6317 👎 309


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fib(self, n: int) -> int:
        # 1. dp array: fib numbers, index: the ith fib number
        # 2. function: dp[i] = dp[i-1] + dp[i-2]
        # 3. init: dp[0] = 0, dp[1] = 1
        # 4. order: left to right
        # 5. eg: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
        if n <= 1:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# leetcode submit region end(Prohibit modification and deletion)
