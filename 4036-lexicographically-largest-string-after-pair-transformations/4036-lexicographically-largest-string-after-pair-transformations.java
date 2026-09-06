class Solution {
    public String[] largestString(int[] nums) {
        int n = nums.length;
        String[] ans = new String[n];

        int z = 1 << 25;

        for (int i = 0; i < n; i++) {
            int x = nums[i];
            StringBuilder curr = new StringBuilder();

            int nz = x / z;
            int r = x % z;

            for (int j = 1; j <= nz; j++) {
                curr.append('z');
            }

            for (int b = 24; b >= 0; b--) {
                if (((r >> b) & 1) == 1) {
                    curr.append((char)('a'+b));
                }
            }
            ans[i] = curr.toString();
        }
        return ans;
    }
}