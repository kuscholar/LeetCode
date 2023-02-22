# Given a string s and an integer k, reverse the first k characters for every 2
# k characters counting from the start of the string. 
# 
#  If there are fewer than k characters left, reverse all of them. If there are 
# less than 2k but greater than or equal to k characters, then reverse the first 
# k characters and leave the other as original. 
# 
#  
#  Example 1: 
#  Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
#  
#  Example 2: 
#  Input: s = "abcd", k = 2
# Output: "bacd"
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of only lowercase English letters. 
#  1 <= k <= 10⁴ 
#  
# 
#  Related Topics Two Pointers String 👍 1446 👎 3005

"""
input: s="abcdefghijk", k=3
output: "cbadefihgjk"
"""
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if not s or not k:
            return
        string = []
        for char in s:
            string.append(char)
        times = len(s) // (2*k)
        left = len(s) % (2*k)
        for i in range(times):
            j, l = i * 2 * k, i * 2 * k + k - 1
            while j < l:
                string[j], string[l] = string[l], string[j]
                j += 1
                l -= 1
        if left < k:
            j, l = times * 2 * k, len(s) - 1
        else:
            j, l = times * 2 * k, times * 2 * k + k - 1

        while j < l:
            string[j], string[l] = string[l], string[j]
            j += 1
            l -= 1

        return "".join(string)
# leetcode submit region end(Prohibit modification and deletion)
