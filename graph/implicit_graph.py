# dfs


# subset
# combination
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
            if i != 0 and nums[i] == nums[i - 1] and i != index:    # deduplicate
                continue

            subset.append(nums[i])
            self.dfs(nums, i + 1, subset)
            subset.pop()


# combination sum
# target restriction
class Solution3:

    def __init__(self):
        self.results = []

    def combinationSum2(self, nums, target):

        nums = sorted(nums)
        self.dfs(nums, 0, [], target)
        return self.results

    def dfs(self, nums, index, subset, target):
        if target == 0:
            self.results.append(list(subset))

        if target < 0:                 # target restriction
            return

        for i in range(index, len(nums)):
            if i != 0 and nums[i] == nums[i - 1] and i != index:  # deduplicate
                continue
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, target - nums[i])
            subset.pop()


# combination sum
# repeated use
class Solution4:

    def combinationSum(self, nums, target):
        results = []

        if len(nums) == 0:
            return results

        nums = sorted(list(set(nums)))      # doesn't matter
        self.dfs(nums, 0, [], target, results)
        return results

    def dfs(self, nums, index, subset, target, results):
        if target == 0:
            return results.append(list(subset))

        if target < 0:
            return

        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i, subset, target - nums[i], results)    # repeated use
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

            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:  # deduplicate
                continue

            permutation.append(nums[i])
            visited[i] = True
            self.dfs(nums, visited, permutation)

            visited[i] = False          # backtracking
            permutation.pop()


# N Queens
class Solution5:
    def solveNQueens(self, n):
        results = []
        self.dfs(n, 0, [], results)
        return results

    def dfs(self, n, row, cols, results):
        if row == n:
            results.append(self.draw(cols))
            return

        for col in range(n):
            if not self.isValid(row, col, cols):    # isValid(3, 2, [1, 3, 0])
                continue

            cols.append(col)    # [1, 3, 0, 2]
            self.dfs(n, row + 1, cols, results)     # dfs(4, 4, [1, 3, 0, 2], [])
            cols.pop()

    def isValid(self, row, col, cols):
        for r, c in enumerate(cols):
            if c == col:
                return False
            if abs(r - row) == abs(c - col):
                return False
        return True

    def draw(self, cols):    # transform cols to board
        n = len(cols)
        board = []
        for i in range(n):
            row = ['Q' if j == cols[i] else '.' for j in range(n)]
            board.append(''.join(row))

        return board


# World Ladder II
""""
e.g.
          lot - log 
         / |     | \
hit - hot  |     | cog 
         \ |     | /
          dot - dog 
          
e.g.
            A
           / \
          B   C
         / \  |
        E  F  D     A -> C -> D
         \/  /
         G  /
         | /
         H   
           
"""""
from collections import defaultdict, deque
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """

    def findLadders(self, start, end, dict):
        self.dictionary = set(dict)
        self.dictionary.add(start)
        self.dictionary.add(end)

        word_to_distance = self.build_graph(end)

        result = []
        self.dfs(start, end, word_to_distance, [start], result)
        return result


    def build_graph(self, start):

        queue = deque([start])
        word_to_distance = defaultdict(int)

        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word):
                if next_word not in word_to_distance:
                        queue.append(next_word)
                        word_to_distance[next_word] = word_to_distance[word] + 1

        return word_to_distance


    def get_next_words(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = left + char + right
                if next_word != word and next_word in self.dictionary:
                    words.append(next_word)
        return words


    def dfs(self, word, end, word_to_distance, path, result):
        print(word)
        if word == end:
            result.append(path[:])
            return

        for next_word in self.get_next_words(word):
            if word_to_distance[next_word] != word_to_distance[word] - 1:  # shortest
                continue
            path.append(next_word)
            self.dfs(next_word, end, word_to_distance, path, result)
            path.pop()


if __name__ == '__main__':
    test1 = Solution1()
    print("Subsets of [1, 2, 3]: %s" % test1.subsets([1, 2, 3]))

    test2 = Solution2()
    print("Permutations of [1, 2, 3]: %s" % test2.permute([1, 2, 3]))
