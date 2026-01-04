class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0

        for num in nums:
            divisors = {}

            for i in range(1, int(num ** 0.5) + 1):
                if num % i == 0:
                    divisors[i] = True
                    divisors[num // i] = True

            if len(divisors) == 4:
                total_sum += sum(divisors.keys())

        return total_sum
