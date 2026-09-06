class Solution {
    public int maxValidSplits(int[] nums) {
        int n = nums.length;
        int ans = 0;
        for(int i=-1;i<n;i++)
        {
            List<Integer> list = new ArrayList<>();
            int score = 0;

            for(int j=0;j<n;j++)
            {
                if(j==i)continue;
                list.add(nums[j]);
            }

            int m = list.size();
            if(m<2)continue;

            int prefix[] = new int[m];
            int suffix[] = new int[m];

            prefix[0]=list.get(0);
            for(int j=1;j<m;j++)
            {
                prefix[j]=gcd(prefix[j-1],list.get(j));
            }

            suffix[m-1]=list.get(m-1);
            for(int j=m-2;j>=0;j--)
            {
                suffix[j]=gcd(suffix[j+1],list.get(j));
            }

            for(int j=0;j<m-1;j++)
            {
                if(prefix[j]==suffix[j+1])score++;
            }

            ans = Math.max(ans,score);
        }
        return ans;
    }
    private int gcd(int a,int b)
    {
        return b==0 ? a : gcd(b,a%b);
    }
}