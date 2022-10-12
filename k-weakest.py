class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        ones = 1
        rows = []

        for i in mat:
            for j in i:
                if j == 1:
                    ones += 1
            rows.append(ones)

        for soldiers in rows:
            pass
