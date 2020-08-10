import sys

# Fibonacci
def fibonacci(n):
    dp = [0 for _ in range(n + 1)]
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# Maximum Sum of Non-adjacent Elements
def maxSumNoAdjacent(nums):
    opt = [0 for _ in range(len(nums))]
    opt[0] = nums[0]
    opt[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        A = opt[i - 2] + nums[i]
        B = opt[i - 1]
        opt[i] = max(A, B)

    return opt[len(nums) - 1]


# Coin Change
def coinChange(coins, amount):
    MAX = sys.maxsize
    dp = [MAX for i in range(amount + 1)]
    dp[0] = 0

    for s in range(1, amount + 1):
        for coin in coins:
            if s < coin:
                continue
            dp[s] = min(dp[s], dp[s - coin] + 1)

    if dp[amount] == MAX:
        return -1
    return dp[amount]


# Longest Increasing Subsequence
def lengthOfLIS(nums):
    n = len(nums)
    dp = [1 for i in range(n)]

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
