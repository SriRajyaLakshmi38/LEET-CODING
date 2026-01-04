class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        def isPrime(x):
            if x < 2:
                return False
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True

        total = 0

        for n in nums:
            # 🔹 Case 1: p^3
            p = round(n ** (1/3))
            if p ** 3 == n and isPrime(p):
                total += 1 + p + p * p + n
                continue

            # 🔹 Case 2: p * q
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    j = n // i
                    if i != j and isPrime(i) and isPrime(j):
                        total += 1 + i + j + n
                    break

        return total
