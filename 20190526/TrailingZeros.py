class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """

    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        # =============================#
        # ============ 7 ==============#
        # =============================#
        lam = lambda x: (x + lam(x // 5)) if x >= 5 else x
        num = lam(n // 5)
        # =============================#
        # ============ 6 ==============#
        # =============================#
        # lam = lambda x: (len(x) + lam(x[4::5])) if len(x) >= 5 else len(x)
        # num = lam(range(5, n + 1, 5))
        # =============================#
        # ============ 5 ==============#
        # =============================#
        # num = 0
        # pows = lambda x, y: pows(x, y + 1) if x % pow(5, y) == 0 else (y - 1)
        # for i in [x for x in range(0, n + 1, 5)][1:]:
        #     num = num + pows(i, 1)
        # =============================#
        # ============ 4 ==============#
        # =============================#
        # num = 0
        # cif = 1
        # x = 0
        # for i in [x for x in range(0, n + 1, 5)][1:]:
        #     x += 1
        #     if i >= pow(5, cif):
        #         cif += 1
        #     if x % 5 == 0:
        #         num = num + cif - 1
        #     num += 1
        # =============================#
        # ============ 3 ==============#
        # =============================#
        # num = 0
        # for i in [x for x in range(0, n + 1, 5)][1:]:
        #     s = i
        #     while 1:
        #         if s % 5 == 0:
        #             num += 1
        #             s //= 5
        #         else:
        #             break
        # =============================#
        # ============ 2 ==============#
        # =============================#
        # num = 0
        # sums = 1
        # ls = [x for x in range(0, n + 1, 5)][1:]
        # x = True
        # i = 0
        # while i < len(ls):
        #     if x:
        #         sums *= ls[i]
        #         x = False
        #     if sums % 5 == 0:
        #         sums *= 2
        #     if sums % 10 == 0:
        #         num += 1
        #         sums //= 10
        #     elif sums % 5 != 0:
        #         x = True
        #         i += 1
        # =============================#
        # ============ 1 ==============#
        # =============================#
        # num = 0
        # sums = 1
        # ls = [x for x in range(0, n + 1, 5)][1:]
        # for i in range(2, n + 1):
        #     sums *= i

        #     while sums >= 10:
        #         if sums % 10 == 0:
        #             num += 1
        #             sums //= 10
        #         else:
        #             break
        # =============================#
        # =============================#
        return num


if __name__ == "__main__":
    import time
    st = time.time()
    s = Solution()
    print(s.trailingZeros(1000000000000))
    # print([x for x in range(0, 101, 5)])
    # print([s.trailingZeros(x) for x in range(0, 101, 5)])
    # print(time.time() - st)
