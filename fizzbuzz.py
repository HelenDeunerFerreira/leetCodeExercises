class Solution:
    def fizzBuzz(self, n: int):
        answer = []

        for number in list(range(1, n+1)):

            if number % 15 == 0:
                answer.append("FizzBuzz")
            elif number % 3 == 0:
                answer.append("Fizz")
            elif number % 5 == 0:
                answer.append("Buzz")
            else:
                stringNumber = str(number)
                answer.append(stringNumber)

        return answer
