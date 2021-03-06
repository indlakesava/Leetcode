https://leetcode.com/problems/sum-of-two-integers/
#371
public class Solution {
    public int GetSum(int a, int b) {
        while(b!=0)
        {
            int carry = a&b;
            a = a^b;
            b = carry<<1;
        }
        return a;
    }
}
