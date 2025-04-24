from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d = {}
        for num in arr:
            d[num] = d.get(num, 0) + 1
        
        threshold = len(arr) // 4
        for k, v in d.items():
            if v > threshold:
                return k

    

