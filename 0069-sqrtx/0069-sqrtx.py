class Solution:
    def mySqrt(self, x: int) -> int:
        odd = 1
        n = 0

        # itrate till x becomes 0 or negative
        while (x > 0):
            x -= odd
            odd += 2 # next odd number on each iteration, odd = 1, 3, 5,...
            n += 1

        # if x is a perfect suare then subtracting n odd numbers would result in 0
        if (x == 0):
            return n

        # if x is not a perfect square then 
        return n - 1