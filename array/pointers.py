# Leetcode 674. Longest Continuous Increasing Subsequence -> subarray
# sliding window
""""
[1, 3, 5, 2, 4, 7, 9]

"""""
def findLengthOfLCIS(nums):
    result = 0
    anchor = 0

    for i in range(len(nums)):
        if i > 0 and nums[i] <= nums[i - 1]:    # compare [i - 1] with [i], not [i] with [i + 1], out of boundary
            anchor = i
        result = max(result, i - anchor + 1)

    return result
