class Solution {
    public int minBishopMoves(int[] source, int[] target) {
        // Check color first
        boolean isSourceWhite = (source[0] + source[1]) % 2 == 0;
        boolean isTargetWhite = (target[0] + target[1]) % 2 == 0;
        if(isSourceWhite != isTargetWhite) return -1;

        // We can Add/Subtract x to each coordinate each turn
        // For 8,1 -> 1,8 we have -x and +x
        // For 4,2 -> 1,3 we have -x and -x, then -x and +x
        // Intuition: Always maximum 2 turns? YES Because we can "mark each possible square after 1 turn"
        if(Math.abs(source[0] - target[0]) == Math.abs(source[1] - target[1])) return 1;
        return 2;
    }
}