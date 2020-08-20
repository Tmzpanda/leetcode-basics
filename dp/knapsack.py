# Knapsack
def knapsack1(weights, values, weightLimit):
    size = len(weights)
    opt = [[0 for _ in range(weightLimit + 1)] for _ in range(size + 1)]

    for i in range(size + 1):
        for w in range(weightLimit + 1):
            if i == 0 or w == 0:    # initialization
                opt[i][w] = 0
            if w < weights[i - 1]:
                opt[i][w] = opt[i - 1][w]
            else:
                A = values[i - 1] + opt[i - 1][w - weights[i - 1]]
                B = opt[i - 1][w]
                opt[i][w] = max(A, B)

    return opt[-1][-1]


def knapsack2(weights, values, weightLimit):
    size = len(weights)
    dp = [0 for _ in range(weightLimit + 1)]

    for i in range(size):
        for j in range(weightLimit, weights[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

    return dp[weightLimit]


# Subset Sum Equals K
def subsetSum1(nums, K):
    n = len(nums)
    subset = [[False for _ in range(K + 1)] for _ in range(n)]
    for i in range(len(subset)):
        subset[i][0] = True
    subset[0][K] = True

    for i in range(1, n):
        for s in range(1, K + 1):
            if nums[i] > s:     # only positive integers
                subset[i][s] = subset[i - 1][s]
            else:
                A = subset[i - 1][s - nums[i]]
                B = subset[i - 1][s]
                subset[i][s] = A or B

    return subset[-1][-1]


def subsetSum2(nums, K):
    dp = [False for _ in range(K + 1)]
    dp[0] = True
    for x in nums:
        for i in range(K, x - 1, -1):
            dp[i] = dp[i] or dp[i - x]
    return dp[K]


if __name__ == '__main__':

    size = 3
    weights = [10, 20, 30]
    values = [60, 100, 120]
    weightLimit = 50
    print("Knapsack Largest Value: %s" % knapsack1(weights, values, weightLimit))
    print("Knapsack Largest Value: %s" % knapsack2(weights, values, weightLimit))

    nums = [34, 4, 15, 5, 2]
    K = 40
    print("Subset Sum Equals K exists: %s" % subsetSum1(nums, K))
    print("Subset Sum Equals K exists: %s" % subsetSum2(nums, K))









# Maximum Sum of Two Non-Overlapping Subarrays
# N-sum
# coin change
# LIS 具体方案？？

# dimension reduction

