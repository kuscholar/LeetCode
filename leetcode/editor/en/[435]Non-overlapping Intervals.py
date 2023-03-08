# Given an array of intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of intervals you need to remove to make the rest of the 
# intervals non-overlapping. 
# 
#  
#  Example 1: 
# 
#  
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-
# overlapping.
#  
# 
#  Example 2: 
# 
#  
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals 
# non-overlapping.
#  
# 
#  Example 3: 
# 
#  
# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're 
# already non-overlapping.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= intervals.length <= 10⁵ 
#  intervals[i].length == 2 
#  -5 * 10⁴ <= starti < endi <= 5 * 10⁴ 
#  
# 
#  Related Topics Array Dynamic Programming Greedy Sorting 👍 5562 👎 155


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        result = 0
        intervals.sort(key=lambda x: (x[0],x[1]))
        right = intervals[0][1]
        print(intervals)
        for i in range(1, len(intervals)):
            print(i, right, result)
            if intervals[i][0] < right:
                result += 1
                right = min(right, intervals[i][1]) # need to update the smallest right end
            else:
                right = intervals[i][1]
        return result
        # if len(intervals) == 0: return 0
        # intervals.sort(key=lambda x: x[1])
        # count = 1  # 记录非交叉区间的个数
        # end = intervals[0][1]  # 记录区间分割点
        # print(intervals)
        # for i in range(1, len(intervals)):
        #     if end <= intervals[i][0]:
        #         count += 1
        #         end = intervals[i][1]
        # return len(intervals) - count
# leetcode submit region end(Prohibit modification and deletion)
