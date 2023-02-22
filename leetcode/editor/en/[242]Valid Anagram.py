# Given two strings s and t, return true if t is an anagram of s, and false 
# otherwise. 
# 
#  An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once. 
# 
#  
#  Example 1: 
#  Input: s = "anagram", t = "nagaram"
# Output: true
#  
#  Example 2: 
#  Input: s = "rat", t = "car"
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length, t.length <= 5 * 10⁴ 
#  s and t consist of lowercase English letters. 
#  
# 
#  
#  Follow up: What if the inputs contain Unicode characters? How would you 
# adapt your solution to such a case? 
# 
#  Related Topics Hash Table String Sorting 👍 8161 👎 263


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t or len(s) != len(t):
            return False
        wordMap = {}
        for char in s:
            if char not in wordMap:
                wordMap[char] = 1
            else:
                wordMap[char] += 1
        for char in t:
            if char not in wordMap:
                return False
            if wordMap[char] == 0:
                return False
            wordMap[char] -= 1

        for val in wordMap.values():
            if val != 0:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
