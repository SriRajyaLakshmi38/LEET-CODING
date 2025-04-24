

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        step = n // 4
        for i in range(n - step):
            if arr[i] == arr[i + step]:
                return arr[i]


    

