class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        # https://leetcode.com/problems/contains-duplicate-ii/description/

        # arr = []

        # for n in nums:
        #     reps = nums.count(n)
        #     arr.append([n, reps])
        # print(arr)
        # for a in arr:
        #     if a[1] > 0:
        #         result = arr[0][0] - arr[1][0]

        # if result <= k:
        #     print(True)
        # else:
        #     print(False)


# Return True if two values within k steps in the list are identical
# Find 2 numbers in the array that are equal and are at most k apart from each other

    def containsNearbyDuplicate(self, nums, k):
        pass


s = Solution()
s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], k=2)
