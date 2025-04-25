from collections import defaultdict
from typing import List

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        prefix_count = 0
        count_map = defaultdict(int)
        count_map[0] = 1
        result = 0

        for num in nums:
            if num % modulo == k:
                prefix_count += 1
            key = (prefix_count - k) % modulo
            result += count_map[key]
            count_map[prefix_count % modulo] += 1

        return result
