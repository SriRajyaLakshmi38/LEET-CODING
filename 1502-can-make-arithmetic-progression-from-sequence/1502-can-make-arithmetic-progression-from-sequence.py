class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        k = arr

        diff = k[1] - k[0]

        for i in range(len(k) - 1):
            if k[i + 1] - k[i] != diff:
                return False   
        return True