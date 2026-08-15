class Solution:
    def isPalindrome(self, s: str) -> bool:

        s=s.lower()

        clean_s = "".join(c for c in s if c.isalnum())

        for i in range(int(len(clean_s)/2)):
            if clean_s[i]!=clean_s[len(clean_s)-i-1]:
                return False
        return True
        