class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        listSum = []
        wealth = 0

        for i in accounts:
            sum = 0

            for j in i:
                sum += j
            listSum.append(sum)

        for i in listSum:
            if i > wealth:
                wealth = i

        return wealth
