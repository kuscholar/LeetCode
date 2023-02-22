# Given an input string s, reverse the order of the words. 
# 
#  A word is defined as a sequence of non-space characters. The words in s will 
# be separated by at least one space. 
# 
#  Return a string of the words in reverse order concatenated by a single space.
#  
# 
#  Note that s may contain leading or trailing spaces or multiple spaces 
# between two words. The returned string should only have a single space separating the 
# words. Do not include any extra spaces. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "the sky is blue"
# Output: "blue is sky the"
#  
# 
#  Example 2: 
# 
#  
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing 
# spaces.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single 
# space in the reversed string.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s contains English letters (upper-case and lower-case), digits, and spaces ' 
# '. 
#  There is at least one word in s. 
#  
# 
#  
#  Follow-up: If the string data type is mutable in your language, can you 
# solve it in-place with O(1) extra space? 
# 
#  Related Topics Two Pointers String 👍 5438 👎 4483


# leetcode submit region begin(Prohibit modification and deletion)

"""
This method uses O(n) time and O(n) space.
To use O(1) space, we can do:
1. remove extra spaces -> "the sky is blue"
2. reverse the whole string -> "eulb si yks eht"
3. reverse each word -> "blue is sky the"
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""
        result = []
        word = []
        for char in s:
            if char == " ":
                if word:
                    result.append(''.join(word))
                word = []
                continue
            word.append(char)
        if word:
            result.append("".join(word))
        return ' '.join(result[::-1])
# leetcode submit region end(Prohibit modification and deletion)
