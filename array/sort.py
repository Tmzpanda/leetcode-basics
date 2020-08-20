

# merge sort
# merge
class Solution1:
    def __init__(self):
        self.temp = [0 for i in range(len(nums))]

    def sortArray(self, nums):
        if nums is None or len(nums) == 0:
            return

        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def mergeSort(self, nums, start, end):
        if start >= end:
            return

        middle = (start + end) // 2
        self.mergeSort(nums, start, middle)
        self.mergeSort(nums, middle + 1, end)
        self.merge(nums, start, end)

    def merge(self, nums, start, end):
        middle = (start + end) // 2
        left, right = start, middle + 1
        index = left

        while left <= middle and right <= end:
            if nums[left] < nums[right]:
                self.temp[index] = nums[left]
                left += 1
            else:
                self.temp[index] = nums[right]
                right += 1
            index += 1

        # either not done yet
        while left <= middle:
            self.temp[index] = nums[left]
            index += 1
            left += 1

        while right <= end:
            self.temp[index] = nums[right]
            index += 1
            right += 1

        for i in range(start, end + 1):
            nums[i] = self.temp[i]


# quick sort
# partition
def quickSort(nums, start, end):
    # break condition
    if start >= end:
        return

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

    quickSort(nums, start, right)
    quickSort(nums, left, end)


if __name__ == '__main__':
    nums = [7, 2, 1, 6, 8, 5, 3, 4]
    print("Array: %s" % nums)

    nums.reverse()
    print("Reversed Array: %s" % nums)

    nums.sort(reverse=True)
    print("Sorted Array in Descending Order: %s" % nums)

    nums = [7, 2, 1, 6, 8, 5, 3, 4]
    test1 = Solution1()
    print("Merge Sort Result: %s" % test1.sortArray(nums))

    nums = [7, 2, 1, 6, 8, 5, 3, 4]
    nums = [1,2,4,4,7,3,6]
    quickSort(nums, 0, len(nums) - 1)
    print("Quick Sort Result: %s" % nums)


