# Template

## Combination

### Basic: [77. Combinations](day-24/77.-combinations.md)

```python
class Solution:
    def __init__(self):
        # we can have either global variables or pass them in the backtracking func
        self.path = []
        self.result = []
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not k or not n:
            return []
        self.backtracking(n, k, 1)
        return self.result

    def backtracking(self, n, k, startIndex):
        # 1. parameters: n, k, startIndex, return: None
        # 2. ending: len(path) == k
        # 3. each level, use for loop to traverse
        if len(self.path) == k:
            self.result.append(self.path[:])
            return
        for i in range(startIndex, n+1):
            self.path.append(i)
            self.backtracking(n, k, i+1)
            self.path.pop()
```

### if has duplicate: [90. Subsets II](day-28/90.-subsets-ii.md)

```python
class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 1. parameter: nums, index; return: None
        # 2. ending: every step append
        # 3. each level: remove duplicate
        if not nums:
            return []
        nums.sort()
        self.backtracking(nums, 0)
        return self.result

    def backtracking(self, nums, index):
        self.result.append(self.path[:])
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()
```

### Cutting: [131. Palindrome Partitioning](day-27/131.-palindrome-partitioning.md)

```python
class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def partition(self, s: str) -> List[List[str]]:
        # 1. parameters: s, startIndex, return: None
        # 2. ending: startIndex >= len(s)
        # 3. each level: determine if so far path is palindrome
        if not s:
            return []
        self.backtracking(list(s), 0)
        return self.result

    def backtracking(self, s, startIndex):
        if startIndex >= len(s):
            self.result.append(self.path[:])
            return
        for i in range(startIndex, len(s)):
            if self.isPalindrome(s[startIndex:i+1]):
                self.path.append(''.join(s[startIndex:i+1]))
            else:
                continue
            # if the program reaches here, it means path already added previous substring
            self.backtracking(s, i+1)
            self.path.pop()

    def isPalindrome(self, subString):
        return subString == subString[::-1]

if __name__ == "__main__":
    test = "aab"
    print(Solution().partition(test))
```

## Permutation

### Basic: [46. Permutations](day-29/46.-permutations.md)

```python
class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        # 1. parameters: nums, used; return: None
        # 2. ending: len(self.path) == len(nums)
        # 3. each level: traverse
        if not nums:
            return []
        self.backtracking(nums, [False]*len(nums))
        return self.result

    def backtracking(self, nums, used):
        if len(self.path) == len(nums):
            self.result.append(self.path[:])
            return
        for i in range(len(nums)):
            if used[i] == True:
                continue
            self.path.append(nums[i])
            used[i] = True
            self.backtracking(nums, used)
            used[i] = False
            self.path.pop()
```

### If has duplicate: [47. Permutations II](day-29/47.-permutations-ii.md)

```python
class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        self.backtracking(nums, [False]*len(nums))
        return self.result

    def backtracking(self, nums, used):
        if len(self.path) == len(nums):
            self.result.append(self.path[:])
            return
        for i in range(len(nums)):
            if used[i] == True:
                continue
            if i > 0 and nums[i] == nums[i-1] and used[i-1] == False:
                continue
            self.path.append(nums[i])
            used[i] = True
            self.backtracking(nums, used)
            used[i] = False
            self.path.pop()
```
