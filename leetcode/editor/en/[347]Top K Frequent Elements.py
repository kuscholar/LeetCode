# Given an integer array nums and an integer k, return the k most frequent 
# elements. You may return the answer in any order. 
# 
#  
#  Example 1: 
#  Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#  
#  Example 2: 
#  Input: nums = [1], k = 1
# Output: [1]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  k is in the range [1, the number of unique elements in the array]. 
#  It is guaranteed that the answer is unique. 
#  
# 
#  
#  Follow up: Your algorithm's time complexity must be better than O(n log n), 
# where n is the array's size. 
# 
#  Related Topics Array Hash Table Divide and Conquer Sorting Heap (Priority 
# Queue) Bucket Sort Counting Quickselect 👍 12642 👎 465


# leetcode submit region begin(Prohibit modification and deletion)
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or not k:
            return []
        Map = {}
        for num in nums:
            Map[num] = Map.get(num,0) + 1
        result = [0] * k
        minHeap = []
        for key, freq in Map.items():
            heapq.heappush(minHeap, (freq,key))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(minHeap)[1]
        return result
# leetcode submit region end(Prohibit modification and deletion)
