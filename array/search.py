# Find K Closest in a Sorted Array
class Solution:
    def findKClosestNumbers(self, A, target, k):
        right = self.findUpperClosest(A, target)
        left = right - 1

        # merge
        result = []
        for _ in range(k):
            if self.isLeftCloser(A, left, right, target):
                result.append(A[left])
                left -= 1
            else:
                result.append(A[right])
                right += 1

        return result

    @staticmethod
    def findUpperClosest(nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return start

    @staticmethod
    def isLeftCloser(A, left, right, target):
        if left < 0:
            return False
        if right > len(A) - 1:
            return True
        return target - A[left] <= A[right] - target


# Median of two Sorted Arrays
def findMedianSortedArrays(A, B):

    def isFirstSmaller(A, p1, B, p2):
        if p1 > len(A) - 1:
            return False
        if p2 > len(B) - 1:
            return False
        return A[p1] <= B[p2]

    # merge
    m, n = len(A), len(B)
    p1, p2 = 0, 0
    left, right = -1, -1
    for i in range((m + n) // 2 + 1):    # binary search: mid = (start + end) // 2
        left = right
        if isFirstSmaller(A, p1, B, p2):
            right = A[p1]
            p1 += 1
        else:
            right = B[p2]
            p2 += 1

    if (m + n) % 2 == 1:
        return right
    return (left + right) / 2


# quick select O(n)
# partition
def quickSelect(nums, start, end, k):

    left, right = start, end
    pivot = nums[(start + end) // 2]

    while left <= right:
        while left <= right and nums[left] < pivot:
            left += 1
        while left <= right and nums[right] > pivot:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    # search
    if k <= right:
        return quickSelect(nums, start, right, k)
    if k >= left:
        return quickSelect(nums, left, end, k)
    return nums[k]


# Find Kth Smallest
def findKthSmallest(nums, k):
    n = len(nums)
    return quickSelect(nums, 0, n - 1, k - 1)


if __name__ == '__main__':

    A = [1, 4, 6, 8]
    target = 3
    k = 3
    test = Solution()
    print("K Closest Numbers to Target in Array: %s" % test.findKClosestNumbers(A, target, k))

    A = [1, 4, 6, 8]
    B = [2, 3, 5, 6]
    print(A, end='\n')
    print(B)
    print("Find Median of Two Sorted Arrays: %s" % findMedianSortedArrays(A, B))

    nums = [2, 4, 5, 3, 1, 6]
    print("Kth Smallest Element in %s: %s" % (nums, findKthSmallest(nums, 3)))




