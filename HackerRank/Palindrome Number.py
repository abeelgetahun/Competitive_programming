#https://leetcode.com/problems/palindrome-number/submissions/1212011435
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]
