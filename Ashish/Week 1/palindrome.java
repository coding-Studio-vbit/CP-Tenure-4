class Solution {
    public boolean isPalindrome(int x) {
        if(x >= 0)
        {
            StringBuffer s1 = new StringBuffer();
            s1.append(x);
            String s3 = new String(s1);
            String s2 = new String(s1.reverse());
            if(s3.equals(s2))
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        else
        {
            return false;
        }
    }
}