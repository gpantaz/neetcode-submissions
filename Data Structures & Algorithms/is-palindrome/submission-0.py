class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([chara.lower() for chara in s if chara.isalnum()])
        return s == s[::-1]