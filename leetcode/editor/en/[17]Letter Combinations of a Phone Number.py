# Given a string containing digits from 2-9 inclusive, return all possible 
# letter combinations that the number could represent. Return the answer in any order. 
# 
# 
#  A mapping of digits to letters (just like on the telephone buttons) is given 
# below. Note that 1 does not map to any letters. 
#  
#  
#  Example 1: 
# 
#  
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#  
# 
#  Example 2: 
# 
#  
# Input: digits = ""
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: digits = "2"
# Output: ["a","b","c"]
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= digits.length <= 4 
#  digits[i] is a digit in the range ['2', '9']. 
#  
# 
#  Related Topics Hash Table String Backtracking 👍 14182 👎 814


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.path = []
        self.result = []
        self.map = {'1': [],
                    '2': ['a','b','c'],
                    '3': ['d','e','f'],
                    '4': ['g','h','i'],
                    '5': ['j','k','l'],
                    '6': ['m','n','o'],
                    '7': ['p','q','r','s'],
                    '8': ['t','u','v'],
                    '9': ['w','x','y','z']}
    def letterCombinations(self, digits: str) -> List[str]:
        # 1. parameters: digits, digit, return: None
        # 2. ending: len(path) == len(digits)
        # 3. each level: traverse
        if not digits:
            return []
        length = len(digits)
        self.backtracking(digits, 0, length)
        return self.result
    def backtracking(self, digits, index, length):
        if len(self.path) == length:
            self.result.append(''.join(self.path[:]))
            return
        for char in self.map[digits[index]]:
            self.path.append(char)
            self.backtracking(digits, index+1, length)
            self.path.pop()
# leetcode submit region end(Prohibit modification and deletion)
