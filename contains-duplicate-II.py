class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        arr = []

        for n in nums:
            reps = nums.count(n)
            arr.append([n, reps])
        print(arr)
        for a in arr:
            if a[1] > 0:
                result = arr[0][0] - arr[1][0]

        if result <= k:
            print(True)
        else:
            print(False)


s = Solution()
s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], k=2)


# Return True if two values within k steps in the list are identical
# estudar esses códigos
# dic = {}
# for i, n in enumerate(nums):
#     if n in dic and i <= dic[n]:
#         return True
#     dic[n] = i + k
# return False

# def containsNearbyDuplicate(self, nums, k):
#     dic = {}
#     for i, v in enumerate(nums):
#         if v in dic and i - dic[v] <= k:
#             return True
#         dic[v] = i
#     return False
