class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        print(hashmap)
        for i in range(len(nums)):
            complement = target - nums[i]
            print(complement)
            if complement in hashmap:
                return [i, hashmap[complement]]
                print(i)
            hashmap[nums[i]] = i
        return []
