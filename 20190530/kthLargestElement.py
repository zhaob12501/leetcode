#!/usr/bin/env python
# coding: utf-8
"""
@File   : 第k大元素
@Remarks: 在数组中找到第 k 大的元素。
@Author : ZhaoBin
@Date   : 2019-05-30 16:48:39
@Last Modified by   : ZhaoBin
@Last Modified time : 2019-05-30 16:48:39
"""


class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def kthLargestElement(self, n, nums):
        # write your code here
        new_nums = sorted(nums, reverse=True)
        return new_nums[n - 1]


if __name__ == "__main__":
    s = Solution()
    answer = s.kthLargestElement(2, [1, 5, 21, 3, 52, 21, 1])
    print(answer)
