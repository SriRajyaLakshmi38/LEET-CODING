from collections import defaultdict
from typing import List

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        prefix_count = 0
        count_map = defaultdict(int)
        count_map[0] = 1  # Initialize with prefix sum 0
        result = 0

        for num in nums:
            # Increment prefix count if condition is satisfied
            if num % modulo == k:
                prefix_count += 1
            
            # Calculate the key we want to match from previous prefix sums
            key = (prefix_count - k) % modulo
            result += count_map[key]

            # Update map with current prefix modulo
            count_map[prefix_count % modulo] += 1

        return result
