# Link: https://leetcode.com/problems/palindrome-number/
class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        return str(x) == str(x)[::-1]
