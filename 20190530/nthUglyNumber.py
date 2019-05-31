#!/usr/bin/env python
# coding: utf-8
"""
@File   : 丑数 II
@Remarks: 设计一个算法，找出只含素因子2，3，5 的第 n 小的数。 符合条件的数如：1, 2, 3, 4, 5, 6, 8, 9, 10, 12...
@Author : ZhaoBin
@Date   : 2019-05-30 16:06:47
@Last Modified by   : ZhaoBin
@Last Modified time : 2019-05-30 16:06:47
"""
import heapq


class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """

    def nthUglyNumber(self, n):
        # init heap with 1 element
        heap = [1]
        # n - 1 more ugly numbers to find
        ls = []
        for i in range(n - 1):
            cur = heapq.heappop(heap)
            print("cur :", cur)
            print("heap:", heap)
            ls.append(cur)
            print("ls  :", ls)
            for factor in [2, 3, 5]:
                temp = cur * factor
                if temp not in heap:
                    heapq.heappush(heap, temp)
                    print("heap:", heap)
        return heapq.heappop(heap)


if __name__ == "__main__":
    s = Solution()
    print(s.nthUglyNumber(9))
