#!/usr/bin/env python
# coding: utf-8
"""
@File   : 统计数字
@Remarks: 计算数字 k 在 0 到 n 中的出现的次数，k 可能是 0~9 的一个值。
@Author : ZhaoBin
@Date   : 2019-05-30 16:05:10
@Last Modified by   : ZhaoBin
@Last Modified time : 2019-05-30 16:05:10
"""


class Solution:
    """
    @param k: An integer
    @param n: An integer
    @return: An integer denote the count of digit k in 1..n
    """

    def digitCounts(self, k: int, n: int) -> int:
        # write your code here
        str_k = str(k)
        num = 0
        for i in range(n + 1):
            for j in str(i):
                if str_k == j:
                    num += 1
        return num


if __name__ == "__main__":
    s = Solution()
    print(s.digitCounts(1, 12))
