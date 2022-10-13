class Solution:
    def kWeakestRows(self, mat, k):
        rows = []

        for i in mat:
            ones = 0
            for j in i:
                if j == 1:
                    ones += 1
            rows.append(ones)

        weak = sorted(rows)

        print(weak[0:k])


# A row i is weaker than a row j if one of the following is true:
# The number of soldiers in row i is less than the number of soldiers in row j.
# Both rows have the same number of soldiers and i < j.
# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

s = Solution()
s.kWeakestRows([[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]], 2)
