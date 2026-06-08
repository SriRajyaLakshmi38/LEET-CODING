class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l = []
        m = []
        n = []
        for i in nums:
            if i < pivot:
                #print(i,pivot)
                l.append(i)
                #print(l)
            elif i>pivot:
                #print(i,pivot)
                m.append(i)
                #print(m)
            else:
                #print(i)
                n.append(i)
                #print(n)
                
        k = l+n+m
        #print(k)
        return k
