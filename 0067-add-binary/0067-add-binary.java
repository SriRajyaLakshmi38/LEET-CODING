class Solution {
    public String addBinary(String a, String b) {
        StringBuilder result = new StringBuilder();
        
        int i = a.length() - 1;  // Pointer for string a
        int j = b.length() - 1;  // Pointer for string b
        int carry = 0;  // Carry to handle overflow
        
        // Add bit by bit from right to left
        while (i >= 0 || j >= 0 || carry != 0) {
            int sum = carry;  // Start with the carry from the previous iteration
            
            if (i >= 0) {
                sum += a.charAt(i) - '0';  // Add bit from string a
                i--;
            }
            
            if (j >= 0) {
                sum += b.charAt(j) - '0';  // Add bit from string b
                j--;
            }
            
            carry = sum / 2;  // Calculate new carry
            result.append(sum % 2);  // Append the current bit to the result
        }
        
        return result.reverse().toString();  // Reverse the result and return it
    }
}