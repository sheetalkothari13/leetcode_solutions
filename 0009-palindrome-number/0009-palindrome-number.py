class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        original = x
        reverse = 0
        while x>0:
            reverse = reverse *10 + x%10
            x//=10
        return original == reverse
        