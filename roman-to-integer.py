class Solution(object):
    def romanToInt(self, s):
        roman = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        answer = 0
        last_add = 0

        for letter in s[::-1]:
            if last_add > roman[letter]:
                answer -= roman[letter]
            else:
                answer += roman[letter]
            last_add = roman[letter]

        return answer
