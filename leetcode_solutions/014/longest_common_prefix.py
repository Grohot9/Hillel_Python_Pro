from typing import List


# Link: https://leetcode.com/problems/longest-common-prefix/
class Solution:
    @staticmethod
    def longestCommonPrefix(strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        i = 0
        for i, chars in enumerate(zip(*strs), 1):
            if len(set(chars)) != 1:
                i -= 1
                break
        return strs[0][:i]
