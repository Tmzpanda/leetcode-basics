# dfs


# subset
class Solution1:
    def __init__(self):
        self.results = []

    def subsets(self, nums):
        if nums is None:
            return []

        nums = sorted(nums)
        self.dfs(nums, 0, [])
        return self.results

    def dfs(self, nums, index, subset):

        self.results.append(list(subset))   # deep copy
        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset)
            subset.pop()


# permutation
class Solution2:
    def __init__(self):
        self.results = []

    def permute(self, nums):
        if nums is None:
            return []

        self.dfs(nums, [False for i in range(len(nums))], [])
        return self.results

    def dfs(self, nums, visited, permutation):

        if len(nums) == len(permutation):
            self.results.append(list(permutation))
            return

        for i in range(0, len(nums)):
            if visited[i]:
                continue
            permutation.append(nums[i])
            visited[i] = True
            self.dfs(nums, visited, permutation)

            visited[i] = False   # backtracking
            permutation.pop()


if __name__ == '__main__':
    test1 = Solution1()
    print("Subsets of [1, 2, 3]: %s" % test1.subsets([1, 2, 3]))

    test2 = Solution2()
    print("Permutations of [1, 2, 3]: %s" % test2.permute([1, 2, 3]))
