class Solution(object):
    def twoSum(self, nums, target):  # ANALISANDO ESSES CÓDIGOS
        # dic = {}
        # for i, n in enumerate(nums):
        #     if n in dic:
        #         print([dic[n], i])
        #     dic[target-n] = i

        residual = {}
        for i, n in enumerate(nums):
            if n in residual:
                return [i, residual[n]]
            else:
                residual[target - n] = i

        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                # dificuldade para entender essa parte de dicionários
                print([lookup[target - num], i])
                print(lookup[target - num])
                print(i)
            lookup[num] = i


s = Solution()
s.twoSum([3, 2, 4], 6)
