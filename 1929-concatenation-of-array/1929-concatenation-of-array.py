class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        k = []
        for i in nums:
            k.append(i)
        m = nums + k
        return m