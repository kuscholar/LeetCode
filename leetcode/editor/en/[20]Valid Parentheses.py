# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']
# ', determine if the input string is valid. 
# 
#  An input string is valid if: 
# 
#  
#  Open brackets must be closed by the same type of brackets. 
#  Open brackets must be closed in the correct order. 
#  Every close bracket has a corresponding open bracket of the same type. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "()"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: s = "()[]{}"
# Output: true
#  
# 
#  Example 3: 
# 
#  
# Input: s = "(]"
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of parentheses only '()[]{}'. 
#  
# 
#  Related Topics String Stack 👍 17961 👎 1015


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        for char in s:
            if stack and self.sameType(stack[-1],char):
                stack.pop()
            else:
                stack.append(char)
        return not stack

    def sameType(self, left, right):
        if left == '(':
            if right == ')':
                return True
        elif left == '[':
            if right == ']':
                return True
        elif left == '{':
            if right == '}':
                return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
