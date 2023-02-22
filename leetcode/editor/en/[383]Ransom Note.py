# Given two strings ransomNote and magazine, return true if ransomNote can be 
# constructed by using the letters from magazine and false otherwise. 
# 
#  Each letter in magazine can only be used once in ransomNote. 
# 
#  
#  Example 1: 
#  Input: ransomNote = "a", magazine = "b"
# Output: false
#  
#  Example 2: 
#  Input: ransomNote = "aa", magazine = "ab"
# Output: false
#  
#  Example 3: 
#  Input: ransomNote = "aa", magazine = "aab"
# Output: true
#  
#  
#  Constraints: 
# 
#  
#  1 <= ransomNote.length, magazine.length <= 10⁵ 
#  ransomNote and magazine consist of lowercase English letters. 
#  
# 
#  Related Topics Hash Table String Counting 👍 3618 👎 400


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not magazine:
            return False
        if not ransomNote:
            return True
        magazineMap = {}
        for char in magazine:
            if char not in magazineMap:
                magazineMap[char] = 1
            else:
                magazineMap[char] += 1
        for char in ransomNote:
            if char not in magazineMap:
                return False
            if magazineMap[char] == 0:
                return False
            magazineMap[char] -= 1
        return True

# leetcode submit region end(Prohibit modification and deletion)
