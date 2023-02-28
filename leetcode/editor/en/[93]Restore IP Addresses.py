# A valid IP address consists of exactly four integers separated by single dots.
#  Each integer is between 0 and 255 (inclusive) and cannot have leading zeros. 
# 
#  
#  For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011
# .255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 
#  
# 
#  Given a string s containing only digits, return all possible valid IP 
# addresses that can be formed by inserting dots into s. You are not allowed to reorder 
# or remove any digits in s. You may return the valid IP addresses in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
#  
# 
#  Example 2: 
# 
#  
# Input: s = "0000"
# Output: ["0.0.0.0"]
#  
# 
#  Example 3: 
# 
#  
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 20 
#  s consists of digits only. 
#  
# 
#  Related Topics String Backtracking 👍 4571 👎 742


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        # 1. parameter: s, startIndex; return: None
        # 2. ending: startIndex >= len(s)
        # 3. each level: determine if substring is valid IP
        if not s:
            return []
        self.backtracking(list(s), 0)
        return self.result
    def backtracking(self, s, startIndex):
        # if len(self.path) > 4:
        #     return
        if startIndex >= len(s) and len(self.path) == 4:
            self.result.append('.'.join(self.path))
            return
        for i in range(startIndex, len(s)):
            if self.isValidIP(s[startIndex:i+1]):
                self.path.append(''.join(s[startIndex:i+1]))
            else:
                continue
            self.backtracking(s, i+1)
            self.path.pop()

    def isValidIP(self, subString):
        if len(subString) > 1 and subString[0] == '0':
            return False
        if len(subString) > 3:
            return False
        return 0 <= int(''.join(subString)) <= 255
# leetcode submit region end(Prohibit modification and deletion)
