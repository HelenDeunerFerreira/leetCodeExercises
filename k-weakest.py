class Solution:
    def kWeakestRows(self, mat, k):
        rows = []
        response = []

        for i in range(len(mat)):
            rows.append([mat[i].count(1), i])

        rows.sort()

        for i in range(k):
            response.append(rows[i][1])

        return response
