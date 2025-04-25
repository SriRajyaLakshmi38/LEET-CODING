class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn_pri = float('inf') 
        mx_pro = 0             

        for i in prices:
            if i < mn_pri:
                mn_pri = i
            else:
                profit = i - mn_pri
                mx_pro = max(mx_pro, profit)  
        return mx_pro