class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        palindrom="".join(char for char in s if char.isalpha() or char.isdigit())
        return True if palindrom==palindrom[::-1] else False
        
    
