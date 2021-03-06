# binary search
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Specific Target 

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# iteration
def binary_search_iteration(nums, target):
    start, end = 0, len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# another template
def binary_search(nums, target):
    l, r = 0, len(nums) - 1

    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            l = mid
        else:
            r = mid

    if nums[l] == target:
        return l
    if nums[r] == target:
        return r
    return -1

# recursion
def binary_search_recursion(nums, target):

    def dfs(nums, start, end, target):
        if start > end:
            return -1
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return dfs(nums, mid + 1, end, target)
        return dfs(nums, start, mid - 1, target)

    return dfs(nums, 0, len(nums) - 1, target)


# Search in Rotated Sorted Array
def search(nums, target):
    if not nums:
        return -1

    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if target == nums[mid]:
            return mid

        if nums[mid] >= nums[start]:
            if nums[start] <= target <= nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

        else:
            if nums[mid] <= target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
No Specific Target 

Case 1:
array = [1, 2, 3, 5, 6]      target = 4
               ^  ^
               r  l
               
Case 2:
array = [1, 2, 3, 5, 6]      target = 7
                     ^  ^
                     r  l    OUT OF BOUNDARY!
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Last Position of Target
# Database
def lastPosition(nums, target):
    if not nums:
        return -1

    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] <= target:     # treat '=' '<' equally
            start = mid + 1
        else:
            end = mid - 1
    if nums[end] == target:
        return end          # return r
    else:
        return -1


# Search Insert Position
def searchInsert(nums, target):

    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        if target > nums[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return start            # return l

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Template preventing OUT OF BOUNDARY - " while l + 1 < r "
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Mountain Sequence
# 左指针排除递增 右指针排除递减 夹的部分交界处最值
def mountainSequence(nums):
    l, r = 0, len(nums) - 1
    while l + 1 < r:
        mid = l + (r - l) // 2
        if nums[mid] < nums[mid + 1]:   # judgement
            l = mid
        else:
            r = mid

    return max(nums[l], nums[r])


# Rotated Sorted Array
# 左指针排除左半边 右指针排除右半边 夹的部分交界处最值
def findMin(nums):

    l, r = 0, len(nums) - 1
    while l + 1 < r:
        mid = l + (r - l) // 2
        if nums[mid] > nums[r]:     # must compare with r
            l = mid
        else:
            r = mid
    return min(nums[l], nums[r])


if __name__ == '__main__':

    nums, target = [1, 3, 4, 6, 7, 8, 10, 13, 14], 4
    print("Index Found by binary search iteration: %s" % binary_search_iteration(nums, target))
    print("Index Found by binary search iteration: %s" % binary_search(nums, target))
    print("Index Found by binary search recursion: %s" % binary_search_recursion(nums, target))

    nums, target = [1, 2, 3, 3, 3, 3, 4], 3
    print("Last Position of Target: %s" % lastPosition(nums, target))

    nums, target = [4, 5, 1, 2, 3, 3], 3
    print("Search in Rotated Sorted Array: %s" % search(nums, target))

