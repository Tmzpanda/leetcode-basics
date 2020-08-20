# Longest Continuous Increasing Subsequence -> subarray
# sliding window
def findLengthOfLCIS(nums):
    result = 0
    anchor = 0

    for i in range(len(nums)):
        if i > 0 and nums[i - 1] >= nums[i]:    # compare [i - 1] with [i], not [i] with [i + 1], out of boundary
            anchor = i
        result = max(result, i - anchor + 1)

    return result
