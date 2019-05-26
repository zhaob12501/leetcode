class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        ans = -1000000
        num = 0
        for i in nums:
            num += i
            if num > ans:
                ans = num
            if num < 0:
                num = 0
        return ans
