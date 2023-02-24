# Link: https://leetcode.com/problems/reverse-integer/
class Solution:
    @staticmethod
    def reverse(x: int) -> int:
        reversed_x = int(str(abs(x))[::-1])
        return (reversed_x if x >= 0 else -reversed_x) if reversed_x < 2 ** 31 else 0
