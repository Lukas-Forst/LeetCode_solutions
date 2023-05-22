class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ext = []
        for i in range(1,n+1,1):
            if i % 3 == 0 and i % 5 == 0:
                ext.append("FizzBuzz")
            elif i % 3 == 0:
                ext.append("Fizz")
            elif i % 5 == 0:
                ext.append("Buzz")
            else:
                ext.append(str(i))
        return ext
