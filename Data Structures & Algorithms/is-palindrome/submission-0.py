class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not self.alphaNum(s[left]):
                left = left + 1
            while left< right and not self.alphaNum(s[right]):
                right = right - 1
            if s[left].lower() == s[right].lower():
                left = left + 1
                right = right - 1
            else:
                return False
        return True
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))